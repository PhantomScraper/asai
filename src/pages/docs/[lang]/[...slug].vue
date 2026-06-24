<template>
  <DocsArticle :lang="lang" :slug="slug" />
</template>

<script setup>
import { computed } from "vue";

const route = useRoute();
const lang = computed(() => String(route.params.lang));
const slug = computed(() => {
  const s = route.params.slug;
  return (Array.isArray(s) ? s.join("/") : String(s || "")) || "index";
});

if (!["en", "ja", "zh"].includes(lang.value)) {
  throw createError({ statusCode: 404, statusMessage: "Unknown documentation language", fatal: true });
}
</script>
