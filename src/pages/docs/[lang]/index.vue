<template>
  <DocsArticle :lang="lang" slug="index" />
</template>

<script setup>
import { computed } from "vue";

const route = useRoute();
const lang = computed(() => String(route.params.lang));

if (!["en", "ja", "zh"].includes(lang.value)) {
  throw createError({ statusCode: 404, statusMessage: "Unknown documentation language", fatal: true });
}
</script>
