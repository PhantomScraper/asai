<template>
  <HomeView />
</template>

<script setup>
import { computed } from "vue";
import HomeView from "@/views/HomeView.vue";
import { useI18n, getPageTitle } from "@/i18n";

const { locale } = useI18n();
useHead({ title: computed(() => getPageTitle("meta.home", locale.value)) });
</script>
