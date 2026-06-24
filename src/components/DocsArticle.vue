<template>
  <div class="docs container">
    <aside class="docs__sidebar">
      <div class="docs__langs">
        <NuxtLink
          v-for="l in docLangs"
          :key="l.code"
          :to="`/docs/${l.code}/${slugPath}`"
          class="docs__lang"
          :class="{ 'docs__lang--active': l.code === lang }"
        >
          {{ l.label }}
        </NuxtLink>
      </div>
      <NuxtLink
        :to="`/docs/${lang}`"
        class="docs__home"
        :class="{ 'docs__home--active': slug === 'index' }"
      >
        Documentation
      </NuxtLink>
      <nav class="docs__nav">
        <DocsNavTree :items="nav || []" :lang="lang" :current="slug" />
      </nav>
    </aside>

    <article class="docs__main">
      <div class="docs-content" v-html="page.html" />
      <p v-if="page.sourceUrl" class="docs__source">
        Source:
        <a :href="page.sourceUrl" target="_blank" rel="noopener noreferrer">{{ page.sourceUrl }}</a>
      </p>
    </article>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  lang: { type: String, required: true },
  slug: { type: String, default: "index" },
});

const docLangs = [
  { code: "en", label: "EN" },
  { code: "ja", label: "日本語" },
  { code: "zh", label: "中文" },
];

const slugPath = computed(() => (props.slug === "index" ? "" : props.slug));

const { data: page, error } = await useAsyncData(
  `doc-${props.lang}-${props.slug}`,
  () => $fetch("/api/docs/page", { query: { lang: props.lang, slug: props.slug } }),
  { watch: [() => props.lang, () => props.slug] }
);

if (error.value || !page.value) {
  throw createError({ statusCode: 404, statusMessage: "Documentation page not found", fatal: true });
}

const { data: nav } = await useAsyncData(
  `docnav-${props.lang}`,
  () => $fetch("/api/docs/nav", { query: { lang: props.lang } }),
  { watch: [() => props.lang] }
);

const SITE = "https://leapslabs.com";
useHead(() => ({
  title: `${page.value?.title} | LEAPS Docs`,
  meta: [{ name: "description", content: page.value?.description || "LEAPS documentation" }],
  link: [
    { rel: "canonical", href: `${SITE}/docs/${props.lang}/${slugPath.value}` },
    ...docLangs.map((l) => ({
      rel: "alternate",
      hreflang: l.code,
      href: `${SITE}/docs/${l.code}/${slugPath.value}`,
    })),
  ],
}));
</script>

<style scoped>
.docs {
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr);
  gap: 2.5rem;
  align-items: start;
  padding-top: calc(var(--header-height, 80px) + 1.5rem);
  padding-bottom: 4rem;
}
.docs__sidebar {
  position: sticky;
  top: calc(var(--header-height, 80px) + 1rem);
  max-height: calc(100vh - var(--header-height, 80px) - 2rem);
  overflow-y: auto;
  padding-right: 0.5rem;
}
.docs__langs {
  display: flex;
  gap: 0.375rem;
  margin-bottom: 1rem;
}
.docs__lang {
  padding: 0.25rem 0.6rem;
  font-size: 0.8125rem;
  border: 1px solid var(--color-border, #ddd);
  border-radius: var(--radius-sm, 6px);
  color: var(--color-text-muted, #555);
  text-decoration: none;
}
.docs__lang--active {
  background: var(--color-primary, #b83232);
  border-color: var(--color-primary, #b83232);
  color: #fff;
}
.docs__home {
  display: block;
  font-family: var(--font-display, inherit);
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--color-text, #222);
  text-decoration: none;
  margin-bottom: 0.75rem;
}
.docs__home--active {
  color: var(--color-primary, #b83232);
}
.docs__main {
  min-width: 0;
}
.docs__source {
  margin-top: 2.5rem;
  padding-top: 1rem;
  border-top: 1px solid var(--color-border-light, #eee);
  font-size: 0.8125rem;
  color: var(--color-text-muted, #888);
  word-break: break-all;
}

/* Rendered markdown ("prose") */
.docs-content {
  font-size: 1rem;
  line-height: 1.7;
  color: var(--color-text, #222);
}
.docs-content :deep(h1) {
  font-size: 2rem;
  font-weight: 700;
  margin: 0 0 1.25rem;
  line-height: 1.2;
}
.docs-content :deep(h2) {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 2.25rem 0 1rem;
  padding-bottom: 0.35rem;
  border-bottom: 1px solid var(--color-border-light, #eee);
}
.docs-content :deep(h3) {
  font-size: 1.2rem;
  font-weight: 600;
  margin: 1.75rem 0 0.75rem;
}
.docs-content :deep(p) {
  margin: 0 0 1rem;
}
.docs-content :deep(a) {
  color: var(--color-primary, #b83232);
  text-decoration: underline;
}
.docs-content :deep(ul) {
  list-style: disc;
  margin: 0 0 1rem 1.5rem;
}
.docs-content :deep(ol) {
  list-style: decimal;
  margin: 0 0 1rem 1.5rem;
}
.docs-content :deep(ul ul) {
  list-style: circle;
}
.docs-content :deep(li) {
  margin: 0.3rem 0;
}
.docs-content :deep(li > p) {
  margin: 0;
}
.docs-content :deep(img) {
  max-width: 100%;
  height: auto;
  border-radius: var(--radius-md, 8px);
  border: 1px solid var(--color-border-light, #eee);
  margin: 1rem 0;
}
.docs-content :deep(code) {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.875em;
  background: var(--color-bg, #f4f4f4);
  padding: 0.15em 0.4em;
  border-radius: 4px;
}
.docs-content :deep(pre) {
  padding: 1rem 1.25rem;
  border-radius: var(--radius-md, 8px);
  overflow-x: auto;
  margin: 0 0 1.25rem;
  background: #f6f8fa;
  font-size: 0.85rem;
  line-height: 1.5;
}
/* Sphinx/pygments highlighted code: .highlight wraps <pre> with token spans */
.docs-content :deep(.highlight) {
  border-radius: var(--radius-md, 8px);
  overflow: hidden;
  margin: 0 0 1.25rem;
}
.docs-content :deep(.highlight pre) {
  margin: 0;
  background: transparent;
}
.docs-content :deep(pre code) {
  background: none;
  padding: 0;
  color: inherit;
}
.docs-content :deep(table) {
  width: 100%;
  border-collapse: collapse;
  margin: 0 0 1.25rem;
  font-size: 0.9rem;
}
.docs-content :deep(th),
.docs-content :deep(td) {
  border: 1px solid var(--color-border, #ddd);
  padding: 0.5rem 0.75rem;
  text-align: left;
}
.docs-content :deep(th) {
  background: var(--color-bg, #f6f6f6);
  font-weight: 600;
}
.docs-content :deep(blockquote) {
  margin: 0 0 1.25rem;
  padding: 0.5rem 1rem;
  border-left: 3px solid var(--color-primary, #b83232);
  background: var(--color-bg, #f9f9f9);
  color: var(--color-text-muted, #555);
}
.docs-content :deep(hr) {
  border: none;
  border-top: 1px solid var(--color-border-light, #eee);
  margin: 2rem 0;
}

/* Sphinx admonitions (note / warning / tip / ...) kept as HTML */
.docs-content :deep(.admonition) {
  margin: 0 0 1.25rem;
  padding: 0.75rem 1rem;
  border-radius: var(--radius-md, 8px);
  border-left: 4px solid #0277bd;
  background: #e6f4fb;
}
.docs-content :deep(.admonition-title) {
  font-weight: 700;
  margin: 0 0 0.5rem;
  text-transform: capitalize;
}
.docs-content :deep(.admonition > :last-child) {
  margin-bottom: 0;
}
.docs-content :deep(.admonition.warning),
.docs-content :deep(.admonition.caution) {
  border-left-color: #f0a000;
  background: #fff8e6;
}
.docs-content :deep(.admonition.danger),
.docs-content :deep(.admonition.error) {
  border-left-color: #d32f2f;
  background: #fdecea;
}
.docs-content :deep(.admonition.tip),
.docs-content :deep(.admonition.hint),
.docs-content :deep(.admonition.important) {
  border-left-color: #2e7d32;
  background: #edf7ed;
}

@media (max-width: 1023px) {
  .docs {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  .docs__sidebar {
    position: static;
    max-height: none;
    border-bottom: 1px solid var(--color-border-light, #eee);
    padding-bottom: 1rem;
  }
}
</style>
