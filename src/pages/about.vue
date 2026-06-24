<template>
  <AboutView />
</template>

<script setup>
import { computed } from "vue";
import AboutView from "@/views/AboutView.vue";
import { useI18n, getPageTitle } from "@/i18n";

const { locale } = useI18n();
useHead({ title: computed(() => getPageTitle("meta.about", locale.value)) });
</script>
