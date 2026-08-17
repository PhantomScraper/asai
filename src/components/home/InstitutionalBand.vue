<template>
  <section class="inst">
    <div class="inst__bg" aria-hidden="true">
      <svg class="inst__rings" viewBox="0 0 600 600" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="300" cy="300" r="140" stroke="rgba(217,71,90,0.35)" stroke-width="1.5" />
        <circle cx="300" cy="300" r="220" stroke="rgba(217,71,90,0.2)" stroke-width="1.5" />
        <circle cx="300" cy="300" r="295" stroke="rgba(217,71,90,0.12)" stroke-width="1.5" />
      </svg>
    </div>
    <div class="container inst__inner">
      <div class="inst__copy">
        <span class="inst__kicker">{{ t('home.aboutBand.kicker') }}</span>
        <h2>{{ t('home.aboutBand.title') }}</h2>
        <p>{{ t('home.aboutBand.text') }}</p>
        <RouterLink to="/about" class="inst__link">
          {{ t('home.aboutBand.cta') }}
          <span aria-hidden="true">→</span>
        </RouterLink>
      </div>
      <div class="inst__points">
        <article v-for="point in tm('home.aboutBand.points')" :key="point.title" class="inst__point">
          <h3>{{ point.title }}</h3>
          <p>{{ point.text }}</p>
        </article>
      </div>
    </div>
    <div class="container inst__stats">
      <div v-for="stat in tm('home.aboutBand.stats')" :key="stat.label" class="inst__stat">
        <span class="inst__stat-value">{{ stat.value }}</span>
        <span class="inst__stat-label">{{ stat.label }}</span>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'

const { t, tm } = useI18n()
</script>

<style scoped>
.inst {
  position: relative;
  background: var(--color-ink);
  border-radius: var(--radius-corner-xl) 0 0 0;
  color: white;
  overflow: hidden;
}

.inst::before {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--gradient-ink);
  pointer-events: none;
}

.inst__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.inst__rings {
  position: absolute;
  top: 40%;
  right: -8%;
  width: min(40vw, 520px);
  height: min(40vw, 520px);
  transform: translateY(-50%);
}

.inst__inner {
  position: relative;
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: clamp(2rem, 5vw, 4rem);
  padding-top: clamp(3rem, 6vw, 5rem);
  padding-bottom: clamp(2rem, 4vw, 3rem);
}

.inst__kicker {
  display: block;
  font-family: var(--font-display);
  font-size: 0.9375rem;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 0.75rem;
}

.inst h2 {
  font-family: var(--font-display);
  font-size: clamp(1.625rem, 3vw, 2.125rem);
  font-weight: 400;
  line-height: 1.25;
  margin-bottom: 1rem;
  max-width: 640px;
}

.inst__copy > p {
  font-size: 0.9375rem;
  line-height: 1.75;
  color: rgba(255, 255, 255, 0.8);
  max-width: 560px;
  margin-bottom: 1.5rem;
}

.inst__link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-display);
  font-size: 0.9375rem;
  font-weight: 600;
  color: white;
}

.inst__link:hover {
  text-decoration: underline;
}

.inst__points {
  display: grid;
  gap: 1.25rem;
  align-content: center;
}

.inst__point {
  border-left: 3px solid var(--color-primary-light);
  padding-left: 1.25rem;
}

.inst__point h3 {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.inst__point p {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.75);
  line-height: 1.6;
}

.inst__stats {
  position: relative;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  padding-top: clamp(1.5rem, 3vw, 2rem);
  padding-bottom: clamp(2.5rem, 5vw, 3.5rem);
  border-top: 1px solid rgba(255, 255, 255, 0.15);
}

.inst__stat-value {
  display: block;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 3vw, 2rem);
  font-weight: 600;
  color: var(--color-primary-light);
  margin-bottom: 0.25rem;
}

.inst__stat-label {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.7);
}

@media (max-width: 900px) {
  .inst__inner {
    grid-template-columns: 1fr;
  }

  .inst__stats {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
