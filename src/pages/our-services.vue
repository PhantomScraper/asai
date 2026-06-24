<template>
  <ServicesView />
</template>

<script setup>
import { computed } from "vue";
import ServicesView from "@/views/ServicesView.vue";
import { useI18n, getPageTitle } from "@/i18n";

const { locale } = useI18n();
useHead({ title: computed(() => getPageTitle("meta.services", locale.value)) });
</script>
