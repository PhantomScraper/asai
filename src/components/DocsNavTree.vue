<template>
  <ul class="docs-nav">
    <li v-for="item in items" :key="item.title + (item.slug || '')" class="docs-nav__item">
      <NuxtLink
        v-if="item.slug"
        :to="`/docs/${lang}/${item.slug}`"
        class="docs-nav__link"
        :class="{ 'docs-nav__link--active': item.slug === current }"
      >
        {{ item.title }}
      </NuxtLink>
      <span v-else class="docs-nav__group">{{ item.title }}</span>
      <DocsNavTree
        v-if="item.children && item.children.length"
        :items="item.children"
        :lang="lang"
        :current="current"
      />
    </li>
  </ul>
</template>

<script setup>
defineProps({
  items: { type: Array, default: () => [] },
  lang: { type: String, required: true },
  current: { type: String, default: "" },
});
</script>

<style scoped>
.docs-nav {
  list-style: none;
  margin: 0;
  padding: 0;
}
.docs-nav .docs-nav {
  margin-left: 0.75rem;
  padding-left: 0.5rem;
  border-left: 1px solid var(--color-border-light, #eee);
}
.docs-nav__item {
  margin: 0.1rem 0;
}
.docs-nav__link,
.docs-nav__group {
  display: block;
  padding: 0.3rem 0.5rem;
  border-radius: var(--radius-sm, 6px);
  font-size: 0.875rem;
  line-height: 1.4;
  color: var(--color-text-muted, #555);
  text-decoration: none;
}
.docs-nav__link:hover {
  background: var(--color-bg, #f6f6f6);
  color: var(--color-primary, #b83232);
}
.docs-nav__link--active {
  background: rgba(184, 50, 50, 0.08);
  color: var(--color-primary, #b83232);
  font-weight: 600;
}
.docs-nav__group {
  color: var(--color-text, #222);
  font-weight: 600;
  text-transform: none;
}
</style>
