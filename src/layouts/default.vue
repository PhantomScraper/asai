<template>
  <div class="app">
    <AppHeader />
    <main class="app__main">
      <slot />
    </main>
    <AppFooter />
    <DocsChat />
  </div>
</template>

<script setup>
import AppHeader from "@/components/layout/AppHeader.vue";
import AppFooter from "@/components/layout/AppFooter.vue";
</script>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app__main {
  flex: 1;
}
</style>
