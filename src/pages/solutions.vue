<template>
  <SolutionsView />
</template>

<script setup>
import { computed } from "vue";
import SolutionsView from "@/views/SolutionsView.vue";
import { useI18n, getPageTitle } from "@/i18n";

const { locale } = useI18n();
useHead({ title: computed(() => getPageTitle("meta.solutions", locale.value)) });
</script>
