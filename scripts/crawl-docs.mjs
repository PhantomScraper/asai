// Crawl docs.leapslabs.com (Sphinx / Read-the-Docs theme) into Markdown + frontmatter.
//
// Output: src/content/docs/<lang>/<slug>.md   (lang = en | ja | zh)
// Images: public/docs-assets/...  (referenced by /docs-assets/... in the markdown)
//
// Usage:
//   node scripts/crawl-docs.mjs                 # crawl all languages
//   node scripts/crawl-docs.mjs en              # crawl only English
//   CRAWL_LIMIT=3 node scripts/crawl-docs.mjs en  # quick test: stop after 3 pages
//
// Deps: cheerio, turndown, turndown-plugin-gfm

import "./polyfill-file.mjs"; // must precede cheerio (loads undici, needs global File)
import { writeFile, mkdir } from "node:fs/promises";
import { existsSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import * as cheerio from "cheerio";
import TurndownService from "turndown";
import { strikethrough, taskListItems } from "turndown-plugin-gfm";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const BASE = "https://docs.leapslabs.com";
const OUT_DOCS = join(ROOT, "src/content/docs");
const OUT_ASSETS = join(ROOT, "public/docs-assets");

// language -> path prefix on the docs site
const LANGS = { en: "/", ja: "/ja/", zh: "/zh-cn/" };

// In-site route the migrated docs will live under: /docs/<lang>/<slug>
const DOCS_ROUTE_BASE = "/docs";

const LIMIT = process.env.CRAWL_LIMIT ? Number(process.env.CRAWL_LIMIT) : Infinity;
const ONLY_LANGS = process.argv.slice(2).filter((a) => LANGS[a]);
const TARGET_LANGS = ONLY_LANGS.length ? ONLY_LANGS : Object.keys(LANGS);

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const turndown = new TurndownService({
  headingStyle: "atx",
  codeBlockStyle: "fenced",
  bulletListMarker: "-",
});
turndown.use([strikethrough, taskListItems]);
// Keep complex Sphinx structures as raw HTML (rendered via markdown-it html:true):
// - table: multi-header tables GFM markdown can't represent
// - pre / div.highlight: pygments code blocks (no <code> child -> turndown mangles them)
turndown.keep(
  (node) =>
    node.nodeName === "TABLE" ||
    node.nodeName === "PRE" ||
    (node.nodeName === "DIV" &&
      (node.classList?.contains("highlight") || node.classList?.contains("admonition")))
);
// Drop Sphinx permalink anchors (the ¶ next to headings)
turndown.remove(["script", "style"]);
turndown.addRule("stripHeaderlink", {
  filter: (node) => node.nodeName === "A" && node.classList?.contains("headerlink"),
  replacement: () => "",
});

const downloadedImages = new Map(); // resolvedUrl -> public path (/docs-assets/...)

function langOf(pathname) {
  if (pathname.startsWith("/ja/")) return "ja";
  if (pathname.startsWith("/zh-cn/")) return "zh";
  return "en";
}

// Normalize to a canonical, directory-style pathname for dedupe.
function normalizePath(pathname) {
  let p = pathname.split("#")[0].split("?")[0];
  if (!p.startsWith("/")) p = "/" + p;
  // Sphinx pages are directory-style; ensure trailing slash for non-asset pages.
  const last = p.split("/").pop();
  if (last && last.includes(".")) return p; // it's a file (asset), leave as-is
  if (!p.endsWith("/")) p += "/";
  return p;
}

const SKIP_RE = /\/(_static|_sources|_images|search|genindex)\b|\.(inv|js|css|map|txt|zip|pdf)$/i;

function isCrawlable(u, lang) {
  if (u.origin !== BASE) return false;
  const p = u.pathname;
  if (SKIP_RE.test(p)) return false;
  return langOf(p) === lang;
}

// Rewrite an internal docs URL to its in-site route, else return null.
function internalDocHref(abs, lang) {
  if (abs.origin !== BASE) return null;
  if (SKIP_RE.test(abs.pathname)) return null;
  if (langOf(abs.pathname) !== lang) return null;
  const slug = slugFor(lang, normalizePath(abs.pathname));
  return `${DOCS_ROUTE_BASE}/${lang}/${slug}${abs.hash || ""}`;
}

function slugFor(lang, pathname) {
  const prefix = LANGS[lang]; // '/', '/ja/', '/zh-cn/'
  let rel = pathname;
  if (prefix !== "/" && rel.startsWith(prefix)) rel = rel.slice(prefix.length);
  else if (prefix === "/") rel = rel.slice(1);
  rel = rel.replace(/\/+$/, ""); // drop trailing slash
  return rel === "" ? "index" : rel;
}

function fmEscape(s) {
  return String(s).replace(/"/g, '\\"');
}

async function fetchText(url) {
  const res = await fetch(url, { headers: { "User-Agent": "leaps-docs-migrator/1.0" } });
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${url}`);
  return res.text();
}

async function downloadImage(absUrl) {
  if (downloadedImages.has(absUrl)) return downloadedImages.get(absUrl);
  const u = new URL(absUrl);
  // keep the site path under public/docs-assets, e.g. /_images/x.png -> /docs-assets/_images/x.png
  const rel = u.pathname.replace(/^\/+/, "");
  const publicPath = "/docs-assets/" + rel;
  const filePath = join(OUT_ASSETS, rel);
  try {
    if (existsSync(filePath)) {
      downloadedImages.set(absUrl, publicPath);
      return publicPath;
    }
    const res = await fetch(absUrl, { headers: { "User-Agent": "leaps-docs-migrator/1.0" } });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const buf = Buffer.from(await res.arrayBuffer());
    await mkdir(dirname(filePath), { recursive: true });
    await writeFile(filePath, buf);
    downloadedImages.set(absUrl, publicPath);
    return publicPath;
  } catch (e) {
    console.warn(`  ! image failed ${absUrl}: ${e.message}`);
    downloadedImages.set(absUrl, absUrl); // fall back to remote URL
    return absUrl;
  }
}

async function crawlLang(lang) {
  const rootUrl = BASE + LANGS[lang];
  const queue = [normalizePath(LANGS[lang])];
  const seen = new Set(queue);
  const order = new Map(); // pathname -> discovery index
  order.set(queue[0], 0);
  let count = 0;

  console.log(`\n=== ${lang.toUpperCase()} (${rootUrl}) ===`);

  while (queue.length && count < LIMIT) {
    const path = queue.shift();
    const pageUrl = BASE + path;
    let html;
    try {
      html = await fetchText(pageUrl);
    } catch (e) {
      console.warn(`  ! skip ${pageUrl}: ${e.message}`);
      continue;
    }
    const $ = cheerio.load(html);

    // Discover links (sidebar nav + in-content) before stripping anything.
    $("a[href]").each((_, el) => {
      const href = $(el).attr("href");
      if (!href || href.startsWith("mailto:") || href.startsWith("#")) return;
      let abs;
      try {
        abs = new URL(href, pageUrl);
      } catch {
        return;
      }
      if (!isCrawlable(abs, lang)) return;
      const np = normalizePath(abs.pathname);
      if (!seen.has(np)) {
        seen.add(np);
        order.set(np, order.size);
        queue.push(np);
      }
    });

    // Extract main content.
    const main = $('[role="main"]').first();
    const scope = main.length ? main : $(".document").first();
    if (!scope.length) {
      console.warn(`  ! no content node at ${pageUrl}`);
      continue;
    }
    // Remove chrome: breadcrumbs, prev/next, edit links, version banners.
    scope
      .find(
        "script, style, .wy-breadcrumbs, .rst-footer-buttons, .rst-versions, .headerlink, " +
          '.wy-breadcrumbs-aside, [role="navigation"], .ethical-sidebar, footer'
      )
      .remove();

    const title =
      scope.find("h1").first().text().replace(/[¶#]\s*$/, "").trim() ||
      $("title").text().split("—")[0].trim() ||
      slugFor(lang, path);

    // Rewrite internal doc links -> in-site routes (keep external links/anchors).
    scope.find("a[href]").each((_, el) => {
      const href = $(el).attr("href");
      if (!href || href.startsWith("mailto:") || href.startsWith("#")) return;
      let abs;
      try {
        abs = new URL(href, pageUrl);
      } catch {
        return;
      }
      const internal = internalDocHref(abs, lang);
      if (internal) $(el).attr("href", internal);
    });

    // Rewrite images -> local, download them.
    const imgs = scope.find("img[src]").toArray();
    for (const el of imgs) {
      const src = $(el).attr("src");
      if (!src) continue;
      let abs;
      try {
        abs = new URL(src, pageUrl).href;
      } catch {
        continue;
      }
      const local = await downloadImage(abs);
      $(el).attr("src", local);
    }

    // Store the cleaned content HTML verbatim (faithful clone; rendered via v-html).
    // Markdown conversion was lossy for Sphinx tables/code/notes/cards.
    const body = (scope.html() || "").trim();
    const slug = slugFor(lang, path);
    const section = slug === "index" ? "home" : slug.split("/")[0];

    const frontmatter =
      `---\n` +
      `title: "${fmEscape(title)}"\n` +
      `lang: ${lang}\n` +
      `slug: "${slug}"\n` +
      `section: "${section}"\n` +
      `sourceUrl: "${pageUrl}"\n` +
      `order: ${order.get(path) ?? 999}\n` +
      `---\n\n`;

    const filePath = join(OUT_DOCS, lang, `${slug}.md`);
    await mkdir(dirname(filePath), { recursive: true });
    await writeFile(filePath, frontmatter + body + "\n");
    count++;
    console.log(`  [${count}] ${slug}  (${body.length} chars)  <- ${path}`);

    await sleep(150); // be polite
  }

  console.log(`  done: ${count} pages`);
  return count;
}

(async () => {
  let total = 0;
  for (const lang of TARGET_LANGS) total += await crawlLang(lang);
  console.log(
    `\nTotal: ${total} pages across [${TARGET_LANGS.join(", ")}], ${downloadedImages.size} images.`
  );
})();
