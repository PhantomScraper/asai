// https://nuxt.com/docs/api/configuration/nuxt-config
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { readdirSync, statSync } from "node:fs";

const rootDir = dirname(fileURLToPath(import.meta.url));
const docsDir = join(rootDir, "src/content/docs");

// Collect /docs/<lang>/<slug> routes so `nuxt generate` prerenders every doc page (SEO).
function docsRoutes(): string[] {
  const routes: string[] = [];
  let langs: string[] = [];
  try {
    langs = readdirSync(docsDir).filter((d) => statSync(join(docsDir, d)).isDirectory());
  } catch {
    return routes;
  }
  for (const lang of langs) {
    const walk = (dir: string, prefix: string) => {
      for (const entry of readdirSync(dir)) {
        const full = join(dir, entry);
        if (statSync(full).isDirectory()) {
          walk(full, prefix ? `${prefix}/${entry}` : entry);
        } else if (entry.endsWith(".md")) {
          const slug = (prefix ? `${prefix}/` : "") + entry.replace(/\.md$/, "");
          routes.push(`/docs/${lang}/${slug === "index" ? "" : slug}`);
        }
      }
    };
    walk(join(docsDir, lang), "");
  }
  return routes;
}

export default defineNuxtConfig({
  compatibilityDate: "2025-01-01",
  srcDir: "src/",
  // With srcDir set, point public/ at the real folder (project root) explicitly.
  dir: { public: join(rootDir, "public") },
  devtools: { enabled: true },
  css: [
    "~/assets/styles/main.css",
    "~/assets/styles/pygments.css",
    "~/assets/styles/sphinx-design.css",
  ],
  app: {
    head: {
      htmlAttrs: { lang: "en" },
      meta: [
        { charset: "utf-8" },
        { name: "viewport", content: "width=device-width, initial-scale=1" },
      ],
      link: [
        { rel: "icon", type: "image/png", href: "/favicon.png" },
        { rel: "preconnect", href: "https://fonts.googleapis.com" },
        { rel: "preconnect", href: "https://fonts.gstatic.com", crossorigin: "" },
        {
          rel: "stylesheet",
          href: "https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700&family=Roboto:wght@400;500;700&display=swap",
        },
      ],
    },
  },
  runtimeConfig: {
    // Server-only secrets, populated from .env (Nuxt auto-loads .env in dev).
    geminiApiKey: process.env.GEMINI_API_KEY || "",
    voyageApiKey: process.env.VOYAGE_API_KEY || "",
    qdrantUrl: process.env.QDRANT_URL || "http://localhost:6333",
    qdrantApiKey: process.env.QDRANT_API_KEY || "",
    chatModel: process.env.CHAT_MODEL || "gemini-2.5-flash",
    // Only used by the optional `npm run translate` (Claude) script.
    anthropicApiKey: process.env.ANTHROPIC_API_KEY || "",
  },
  routeRules: {
    // Legacy URLs from before the Products/Services merge and the /projects rename.
    "/our-products": { redirect: { to: "/products-services", statusCode: 301 } },
    "/our-services": { redirect: { to: "/products-services", statusCode: 301 } },
    "/our-projects": { redirect: { to: "/projects", statusCode: 301 } },
  },
  nitro: {
    serverAssets: [{ baseName: "docs", dir: docsDir }],
    prerender: {
      // Only enumerate the 876 doc routes during `nuxt generate` — keeping them
      // out of the dev manifest avoids a route-rules matcher stack overflow.
      routes: process.env.npm_lifecycle_event === "generate" ? docsRoutes() : [],
      crawlLinks: false,
    },
  },
});
