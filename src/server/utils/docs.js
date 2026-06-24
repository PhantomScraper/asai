// Server-side docs access: reads crawled markdown from Nitro server assets
// (mounted at "assets:docs" -> src/content/docs), parses frontmatter, renders
// markdown to HTML, and builds the sidebar navigation tree per language.
import matter from "gray-matter";
import MarkdownIt from "markdown-it";

export const DOC_LANGS = ["en", "ja", "zh"];

const md = new MarkdownIt({ html: true, linkify: true, breaks: false });

// unstorage uses ":" as the path separator within a mount.
const storage = () => useStorage("assets:docs");

function slugToKey(lang, slug) {
  const clean = (slug || "index").replace(/^\/+|\/+$/g, "") || "index";
  return `${lang}:${clean.split("/").join(":")}.md`;
}

function keyToSlug(lang, key) {
  // "en:leaps-rtls:quick-start-guide.md" -> "leaps-rtls/quick-start-guide"
  return key
    .slice(lang.length + 1)
    .replace(/\.md$/, "")
    .split(":")
    .join("/");
}

function plainText(html) {
  return html
    .replace(/<(script|style)[\s\S]*?<\/\1>/gi, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/&[a-z#0-9]+;/gi, " ")
    .replace(/\s+/g, " ")
    .trim();
}

export async function getDocPage(lang, slug) {
  if (!DOC_LANGS.includes(lang)) return null;
  const raw = await storage().getItem(slugToKey(lang, slug));
  if (raw == null) return null;
  const { data, content } = matter(typeof raw === "string" ? raw : String(raw));
  return {
    title: data.title || slug || "Documentation",
    section: data.section || "",
    sourceUrl: data.sourceUrl || "",
    lang,
    slug: (slug || "index").replace(/^\/+|\/+$/g, "") || "index",
    description: plainText(content).slice(0, 155),
    html: content,
  };
}

const navCache = new Map(); // lang -> tree

export async function getDocsNav(lang) {
  if (!DOC_LANGS.includes(lang)) return [];
  if (navCache.has(lang)) return navCache.get(lang);

  const s = storage();
  const keys = (await s.getKeys()).filter(
    (k) => k.startsWith(`${lang}:`) && k.endsWith(".md")
  );

  // Read frontmatter (title + order) for every page in this language.
  const entries = await Promise.all(
    keys.map(async (k) => {
      const slug = keyToSlug(lang, k);
      const raw = await s.getItem(k);
      const { data } = matter(typeof raw === "string" ? raw : String(raw));
      return { slug, title: data.title || slug, order: Number(data.order ?? 999) };
    })
  );

  // Build a tree from slug path segments. A segment may itself be a page.
  const root = { children: new Map() };
  for (const e of entries) {
    if (e.slug === "index") continue; // landing page, not in the sidebar tree
    const segs = e.slug.split("/");
    let node = root;
    let acc = "";
    segs.forEach((seg, i) => {
      acc = acc ? `${acc}/${seg}` : seg;
      if (!node.children.has(seg)) {
        node.children.set(seg, { slug: acc, title: seg, order: 999, isPage: false, children: new Map() });
      }
      node = node.children.get(seg);
      if (i === segs.length - 1) {
        node.title = e.title;
        node.order = e.order;
        node.isPage = true;
      }
    });
  }

  const toArray = (node) =>
    [...node.children.values()]
      .sort((a, b) => a.order - b.order || a.title.localeCompare(b.title))
      .map((n) => ({
        title: n.title,
        slug: n.isPage ? n.slug : null,
        children: n.children.size ? toArray(n) : [],
      }));

  const tree = toArray(root);
  navCache.set(lang, tree);
  return tree;
}
