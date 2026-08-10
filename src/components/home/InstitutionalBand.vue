<template>
  <section class="inst">
    <div class="inst__bg" aria-hidden="true">
      <svg class="inst__rings" viewBox="0 0 600 600" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="300" cy="300" r="140" stroke="rgba(0,160,223,0.3)" stroke-width="1.5" />
        <circle cx="300" cy="300" r="220" stroke="rgba(0,160,223,0.18)" stroke-width="1.5" />
        <circle cx="300" cy="300" r="295" stroke="rgba(0,160,223,0.1)" stroke-width="1.5" />
      </svg>
    </div>
    <div class="container inst__inner">
      <span class="inst__kicker">{{ t('home.institutional.kicker') }}</span>
      <h2>{{ t('home.institutional.title') }}</h2>
      <p>{{ t('home.institutional.text') }}</p>
      <RouterLink to="/about" class="inst__link">
        {{ t('home.institutional.cta') }}
        <span aria-hidden="true">→</span>
      </RouterLink>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'

const { t } = useI18n()
</script>

<style scoped>
.inst {
  position: relative;
  background: var(--color-navy);
  border-radius: var(--radius-corner-xl) 0 0 0;
  color: white;
  overflow: hidden;
}

.inst::before {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--gradient-navy);
  pointer-events: none;
}

.inst__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.inst__rings {
  position: absolute;
  top: 50%;
  right: -8%;
  width: min(40vw, 520px);
  height: min(40vw, 520px);
  transform: translateY(-50%);
}

.inst__inner {
  position: relative;
  padding-top: clamp(3rem, 6vw, 5rem);
  padding-bottom: clamp(3rem, 6vw, 5rem);
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

.inst p {
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
</style>
