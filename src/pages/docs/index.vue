<template>
  <div />
</template>

<script setup>
import { useI18n } from "@/i18n";

// /docs -> /docs/<ui-locale> (docs exist in en/ja/zh; cs falls back to en)
const { locale } = useI18n();
const lang = ["en", "ja", "zh"].includes(locale.value) ? locale.value : "en";
await navigateTo(`/docs/${lang}`, { redirectCode: 302 });
</script>
