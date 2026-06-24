// Translate the English docs (src/content/docs/en) into Czech (cs) with Claude.
// The docs site has no /cs/, so this fills the gap for the 4th site language.
//
// Usage:
//   npm run translate                 # translate all EN pages -> cs (skips existing)
//   npm run translate -- --limit 5    # test on 5 pages
//   npm run translate -- --force      # re-translate even if cs file exists
//
// Env (.env, loaded via `node --env-file=.env`):
//   ANTHROPIC_API_KEY, TRANSLATE_MODEL (default claude-sonnet-4-6)
import { readdirSync, statSync, readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { join, resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import matter from "gray-matter";
import Anthropic from "@anthropic-ai/sdk";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const EN_DIR = join(ROOT, "src/content/docs/en");
const CS_DIR = join(ROOT, "src/content/docs/cs");

const MODEL = process.env.TRANSLATE_MODEL || "claude-sonnet-4-6";
const CONCURRENCY = 4;
const LIMIT = (() => {
  const i = process.argv.indexOf("--limit");
  return i >= 0 ? Number(process.argv[i + 1]) : Infinity;
})();
const FORCE = process.argv.includes("--force");

if (!process.env.ANTHROPIC_API_KEY) {
  console.error("Missing ANTHROPIC_API_KEY. Add it to .env and run: npm run translate");
  process.exit(1);
}

const client = new Anthropic();

const SYSTEM =
  "You are a professional technical translator. Translate the given Markdown documentation " +
  "from English to Czech. Rules:\n" +
  "- Preserve ALL Markdown structure exactly (headings, lists, tables, blockquotes, horizontal rules).\n" +
  "- Do NOT translate or alter: code blocks, inline code, URLs, file paths, HTML, image references, " +
  "and technical identifiers (API/command/function names, product names like LEAPS RTLS, PANS PRO, UDK, Qorvo, FiRa, TDoA, TWR, MQTT).\n" +
  "- Translate only natural-language prose and headings.\n" +
  "- Keep the same number of lines/blocks; do not add commentary or remove content.\n" +
  "- Output ONLY the translated Markdown, nothing else.";

function walk(dir, prefix, out) {
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) walk(full, prefix ? `${prefix}/${entry}` : entry, out);
    else if (entry.endsWith(".md")) out.push({ file: full, slug: (prefix ? `${prefix}/` : "") + entry.replace(/\.md$/, "") });
  }
  return out;
}

async function translateBody(body) {
  const stream = client.messages.stream({
    model: MODEL,
    max_tokens: 16000,
    system: SYSTEM,
    messages: [{ role: "user", content: body }],
  });
  const msg = await stream.finalMessage();
  return msg.content.filter((b) => b.type === "text").map((b) => b.text).join("");
}

function fmEscape(s) {
  return String(s).replace(/"/g, '\\"');
}

async function translateFile({ file, slug }) {
  const outPath = join(CS_DIR, `${slug}.md`);
  if (!FORCE && existsSync(outPath)) return { slug, skipped: true };

  const { data, content } = matter(readFileSync(file, "utf8"));
  let translated = await translateBody(content);
  // Point internal links at the Czech tree.
  translated = translated.replace(/\/docs\/en\//g, "/docs/cs/");
  // Use the translated H1 as the title if present.
  const h1 = translated.match(/^#\s+(.+)$/m);
  const title = h1 ? h1[1].trim() : data.title || slug;

  const frontmatter =
    `---\n` +
    `title: "${fmEscape(title)}"\n` +
    `lang: cs\n` +
    `slug: "${data.slug || slug}"\n` +
    `section: "${data.section || slug.split("/")[0]}"\n` +
    `sourceUrl: "${data.sourceUrl || ""}"\n` +
    `order: ${data.order ?? 999}\n` +
    `---\n\n`;

  mkdirSync(dirname(outPath), { recursive: true });
  writeFileSync(outPath, frontmatter + translated.trim() + "\n");
  return { slug, ok: true };
}

async function main() {
  const files = walk(EN_DIR, "", []).slice(0, LIMIT);
  console.log(`Translating ${files.length} pages EN -> CS with ${MODEL} (concurrency ${CONCURRENCY})...`);

  let done = 0;
  let i = 0;
  async function worker() {
    while (i < files.length) {
      const item = files[i++];
      try {
        const r = await translateFile(item);
        done++;
        console.log(`  [${done}/${files.length}] ${r.skipped ? "skip" : "ok"} ${item.slug}`);
      } catch (e) {
        console.warn(`  ! ${item.slug}: ${e.message}`);
      }
    }
  }
  await Promise.all(Array.from({ length: CONCURRENCY }, worker));
  console.log(`Done. Czech docs in src/content/docs/cs/.`);
  console.log(`Next: add "cs" to docs language lists (nuxt.config docsRoutes is automatic; update RAG_LANGS, useDocs, page lang checks, DocsArticle docLangs) to surface it.`);
}

main().catch((e) => {
  console.error(e.message);
  process.exit(1);
});
