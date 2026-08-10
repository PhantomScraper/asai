<template>
  <section class="dhub">
    <div class="container">
      <div class="dhub__header">
        <h2>{{ t('home.designHub.title') }}</h2>
        <NuxtLink :to="docsLink()" class="dhub__link">
          {{ t('home.designHub.linkText') }}
          <span aria-hidden="true">→</span>
        </NuxtLink>
      </div>
      <div class="grid-4 dhub__grid">
        <div v-for="item in tm('home.designHub.items')" :key="item.id" class="dhub__item">
          <span class="dhub__icon" aria-hidden="true">
            <FeatureIcon :name="item.id" />
          </span>
          <h3>{{ item.title }}</h3>
          <p>{{ item.text }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'
import FeatureIcon from '@/components/ui/FeatureIcon.vue'

const { t, tm } = useI18n()
const { docsLink } = useDocs()
</script>

<style scoped>
.dhub {
  background: var(--gradient-blue);
  border-radius: var(--radius-corner-lg) 0 0 0;
  padding: clamp(2.5rem, 5vw, 4rem) 0;
  color: white;
}

.dhub__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 2.5rem;
}

.dhub__header h2 {
  font-family: var(--font-display);
  font-size: clamp(1.375rem, 2.5vw, 1.625rem);
  font-weight: 400;
}

.dhub__link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-display);
  font-size: 0.9375rem;
  font-weight: 500;
  color: white;
}

.dhub__link:hover {
  text-decoration: underline;
}

.dhub__icon {
  display: inline-flex;
  color: white;
  margin-bottom: 1rem;
}

.dhub__icon :deep(svg) {
  width: 28px;
  height: 28px;
}

.dhub__item h3 {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.dhub__item p {
  font-size: 0.875rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.85);
}
</style>
