<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
  <ClientOnly>
    <ReviewMode />
  </ClientOnly>
</template>

<script setup>
import { useI18n } from "@/i18n";
import ReviewMode from "@/components/review/ReviewMode.vue";

const { locale } = useI18n();
useHead({ htmlAttrs: { lang: locale } });
</script>
