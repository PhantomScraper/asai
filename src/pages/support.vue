<template>
  <SupportView />
</template>

<script setup>
import { computed } from "vue";
import SupportView from "@/views/SupportView.vue";
import { useI18n, getPageTitle } from "@/i18n";

const { locale } = useI18n();
useHead({ title: computed(() => getPageTitle("meta.support", locale.value)) });
</script>
