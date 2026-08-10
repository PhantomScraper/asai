<template>
  <div class="chips__wrapper">
    <section class="chips">
      <div class="container chips__inner">
        <h2 class="chips__title">{{ t('home.chips.title') }}</h2>
        <div class="chips__list">
          <RouterLink v-for="(item, i) in tm('home.chips.items')" :key="i" :to="item.path" class="chip">
            {{ item.label }}
          </RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useI18n } from '@/i18n'

const { t, tm } = useI18n()
</script>

<style scoped>
/* Light-gray wrapper lets the tinted band carve its Qorvo signature corner */
.chips__wrapper {
  background: var(--color-bg);
}

.chips {
  background: var(--tint-blue);
  border-radius: 0 0 var(--radius-corner-lg) 0;
  padding: clamp(2rem, 4vw, 3rem) 0;
}

.chips__inner {
  display: flex;
  align-items: center;
  gap: clamp(1.5rem, 4vw, 3.5rem);
}

.chips__title {
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 2vw, 1.5rem);
  font-weight: 400;
  color: var(--color-text);
  white-space: nowrap;
}

.chips__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

@media (max-width: 768px) {
  .chips__inner {
    flex-direction: column;
    align-items: flex-start;
  }

  .chips__title {
    white-space: normal;
  }
}
</style>
