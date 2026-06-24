<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
import { useI18n } from "@/i18n";

const { locale } = useI18n();
useHead({ htmlAttrs: { lang: locale } });
</script>
