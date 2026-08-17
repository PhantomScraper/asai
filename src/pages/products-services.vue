<template>
  <ProductsServicesView />
</template>

<script setup>
import { computed } from "vue";
import ProductsServicesView from "@/views/ProductsServicesView.vue";
import { useI18n, getPageTitle } from "@/i18n";

const { locale } = useI18n();
useHead({ title: computed(() => getPageTitle("meta.productsServices", locale.value)) });
</script>
