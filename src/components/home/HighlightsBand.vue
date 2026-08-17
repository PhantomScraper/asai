<template>
  <section class="hband" aria-label="LEAPS highlights">
    <div class="container hband__grid">
      <article v-for="(item, i) in tm('home.highlights')" :key="item.title" class="hband__item">
        <span class="hband__icon" aria-hidden="true">
          <!-- Robust Accuracy: crosshair pin -->
          <svg v-if="i === 0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="7" />
            <circle cx="12" cy="12" r="2.5" />
            <path d="M12 2v3M12 19v3M2 12h3M19 12h3" />
          </svg>
          <!-- Proven Record: ribbon medal -->
          <svg v-else-if="i === 1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="9" r="6" />
            <path d="M8.5 14.5 7 22l5-3 5 3-1.5-7.5" />
          </svg>
          <!-- Uniqueness: layered modules -->
          <svg v-else-if="i === 2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="m12 2 9 5-9 5-9-5z" />
            <path d="m3 12 9 5 9-5" />
            <path d="m3 17 9 5 9-5" />
          </svg>
          <!-- 100% In-House: engineer's home/chip -->
          <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <rect x="6" y="6" width="12" height="12" rx="2" />
            <path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4" />
          </svg>
        </span>
        <h3>{{ item.title }}</h3>
        <p>{{ item.text }}</p>
      </article>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'

const { tm } = useI18n()
</script>

<style scoped>
.hband {
  background: white;
  border-bottom: 1px solid var(--color-border-light);
  padding: clamp(2rem, 4vw, 3rem) 0;
}

.hband__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: clamp(1.5rem, 3vw, 2.5rem);
}

.hband__icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--tint-brand-soft);
  color: var(--color-primary);
  margin-bottom: 0.875rem;
}

.hband__icon svg {
  width: 24px;
  height: 24px;
}

.hband__item h3 {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: 0.375rem;
}

.hband__item p {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.6;
}

@media (max-width: 900px) {
  .hband__grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 560px) {
  .hband__grid {
    grid-template-columns: 1fr;
  }
}
</style>
