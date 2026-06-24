// RAG ingestion: chunk crawled docs -> Voyage embeddings -> Qdrant.
//
// Usage:
//   npm run ingest              # incremental upsert (idempotent)
//   npm run ingest -- --recreate  # drop & recreate the collection first
//
// Env (from .env, loaded via `node --env-file=.env`):
//   VOYAGE_API_KEY, QDRANT_URL (default http://localhost:6333), QDRANT_API_KEY
import { readdirSync, statSync, readFileSync } from "node:fs";
import { join, resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { createHash } from "node:crypto";
import matter from "gray-matter";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const DOCS_DIR = join(ROOT, "src/content/docs");
const LANGS = ["en", "ja", "zh"];

const COLLECTION = "leaps_docs";
const EMBED_MODEL = "voyage-3";
const EMBED_DIM = 1024;
// Small batch keeps each request under Voyage free-tier 10K tokens/min.
const BATCH = Number(process.env.VOYAGE_BATCH || 16);

const VOYAGE_API_KEY = process.env.VOYAGE_API_KEY;
const QDRANT_URL = (process.env.QDRANT_URL || "http://localhost:6333").replace(/\/+$/, "");
const QDRANT_API_KEY = process.env.QDRANT_API_KEY || "";
const RECREATE = process.argv.includes("--recreate");
const LIMIT = (() => {
  const i = process.argv.indexOf("--limit");
  return i >= 0 ? Number(process.argv[i + 1]) : Infinity;
})();
// --lang en   or   --lang en,ja   (default: all)
const ONLY_LANGS = (() => {
  const i = process.argv.indexOf("--lang");
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1].split(",").map((s) => s.trim()) : null;
})();
const TARGET_LANGS = ONLY_LANGS ? LANGS.filter((l) => ONLY_LANGS.includes(l)) : LANGS;

if (!VOYAGE_API_KEY) {
  console.error("Missing VOYAGE_API_KEY. Add it to .env and run: npm run ingest");
  process.exit(1);
}

const uuidFrom = (s) => {
  const h = createHash("sha1").update(s).digest("hex");
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-${h.slice(12, 16)}-${h.slice(16, 20)}-${h.slice(20, 32)}`;
};

function walk(dir, prefix, out) {
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) walk(full, prefix ? `${prefix}/${entry}` : entry, out);
    else if (entry.endsWith(".md")) out.push({ file: full, slug: (prefix ? `${prefix}/` : "") + entry.replace(/\.md$/, "") });
  }
  return out;
}

// Split markdown into heading-scoped chunks of ~targetLen chars.
function chunkMarkdown(md, targetLen = 1200) {
  const lines = md.split("\n");
  const chunks = [];
  let buf = [];
  let heading = "";
  let len = 0;
  const flush = () => {
    const text = buf.join("\n").trim();
    if (text.replace(/\s/g, "").length > 20) chunks.push({ heading, text });
    buf = [];
    len = 0;
  };
  for (const line of lines) {
    const h = line.match(/^#{1,4}\s+(.*)/);
    if (h) {
      flush();
      heading = h[1].replace(/[#`*]/g, "").trim();
    }
    buf.push(line);
    len += line.length + 1;
    if (len >= targetLen) flush();
  }
  flush();
  return chunks;
}

async function voyageEmbed(texts, inputType, attempt = 0) {
  const res = await fetch("https://api.voyageai.com/v1/embeddings", {
    method: "POST",
    headers: { "content-type": "application/json", authorization: `Bearer ${VOYAGE_API_KEY}` },
    body: JSON.stringify({ input: texts, model: EMBED_MODEL, input_type: inputType }),
  });
  // Free tier (no payment method) is throttled to ~3 RPM / 10K TPM -> 429.
  if (res.status === 429 || res.status >= 500) {
    if (attempt >= 8) throw new Error(`Voyage ${res.status} after retries: ${await res.text()}`);
    const wait = Math.min(60000, 20000 * (attempt + 1));
    console.log(`  rate-limited (${res.status}); waiting ${wait / 1000}s then retrying...`);
    await new Promise((r) => setTimeout(r, wait));
    return voyageEmbed(texts, inputType, attempt + 1);
  }
  if (!res.ok) throw new Error(`Voyage embeddings ${res.status}: ${await res.text()}`);
  const j = await res.json();
  return j.data.map((d) => d.embedding);
}

async function qdrant(path, method, body) {
  const res = await fetch(`${QDRANT_URL}${path}`, {
    method,
    headers: { "content-type": "application/json", ...(QDRANT_API_KEY ? { "api-key": QDRANT_API_KEY } : {}) },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) throw new Error(`Qdrant ${method} ${path} ${res.status}: ${await res.text()}`);
  return res.json();
}

async function ensureCollection() {
  if (RECREATE) {
    await fetch(`${QDRANT_URL}/collections/${COLLECTION}`, {
      method: "DELETE",
      headers: QDRANT_API_KEY ? { "api-key": QDRANT_API_KEY } : {},
    }).catch(() => {});
  }
  const exists = await fetch(`${QDRANT_URL}/collections/${COLLECTION}`, {
    headers: QDRANT_API_KEY ? { "api-key": QDRANT_API_KEY } : {},
  }).then((r) => r.ok);
  if (!exists) {
    await qdrant(`/collections/${COLLECTION}`, "PUT", {
      vectors: { size: EMBED_DIM, distance: "Cosine" },
    });
    await qdrant(`/collections/${COLLECTION}/index`, "PUT", {
      field_name: "lang",
      field_schema: "keyword",
    });
    console.log(`Created collection ${COLLECTION}`);
  }
}

async function main() {
  await ensureCollection();

  // Build all chunks with metadata.
  const points = [];
  let pages = 0;
  outer: for (const lang of TARGET_LANGS) {
    const langDir = join(DOCS_DIR, lang);
    let files = [];
    try {
      files = walk(langDir, "", []);
    } catch {
      console.warn(`No docs for lang ${lang}`);
      continue;
    }
    for (const { file, slug } of files) {
      if (pages >= LIMIT) break outer;
      pages++;
      const { data, content } = matter(readFileSync(file, "utf8"));
      const title = data.title || slug;
      const chunks = chunkMarkdown(content);
      chunks.forEach((c, i) => {
        points.push({
          id: uuidFrom(`${lang}:${slug}:${i}`),
          payload: {
            lang,
            slug,
            title,
            heading: c.heading || title,
            url: `/docs/${lang}/${slug === "index" ? "" : slug}`,
            text: c.text,
          },
          _text: c.text,
        });
      });
    }
  }
  console.log(`Prepared ${points.length} chunks across ${TARGET_LANGS.join(", ")}. Embedding...`);

  // Embed + upsert in batches.
  let done = 0;
  for (let i = 0; i < points.length; i += BATCH) {
    const batch = points.slice(i, i + BATCH);
    const vectors = await voyageEmbed(batch.map((p) => p._text), "document");
    const upsert = batch.map((p, j) => ({ id: p.id, vector: vectors[j], payload: p.payload }));
    await qdrant(`/collections/${COLLECTION}/points?wait=true`, "PUT", { points: upsert });
    done += batch.length;
    console.log(`  upserted ${done}/${points.length}`);
  }
  console.log(`Done. ${done} chunks indexed in Qdrant collection "${COLLECTION}".`);
}

main().catch((e) => {
  console.error(e.message);
  process.exit(1);
});
