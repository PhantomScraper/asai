<template>
  <ProjectsView />
</template>

<script setup>
import { computed } from "vue";
import ProjectsView from "@/views/ProjectsView.vue";
import { useI18n, getPageTitle } from "@/i18n";

const { locale } = useI18n();
useHead({ title: computed(() => getPageTitle("meta.projects", locale.value)) });
</script>
