<template>
  <ProductsView />
</template>

<script setup>
import { computed } from "vue";
import ProductsView from "@/views/ProductsView.vue";
import { useI18n, getPageTitle } from "@/i18n";

const { locale } = useI18n();
useHead({ title: computed(() => getPageTitle("meta.products", locale.value)) });
</script>
