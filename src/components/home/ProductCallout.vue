<template>
  <section class="callout">
    <div class="container callout__inner">
      <div class="callout__text">
        <h2 class="section-title section-title--lg">{{ t('home.whyTitle') }}</h2>
        <p class="callout__subtitle">{{ t('home.whySubtitle') }}</p>
        <ul class="callout__checklist">
          <li v-for="(item, i) in tm('home.checklist')" :key="i">
            <span class="callout__check" aria-hidden="true">✓</span>
            <span>{{ item }}</span>
          </li>
        </ul>
        <div class="callout__actions">
          <RouterLink to="/our-products" class="btn btn-primary">{{ t('common.tryLeaps') }}</RouterLink>
          <RouterLink to="/solutions" class="btn btn-outline">{{ t('common.learnMore') }}</RouterLink>
        </div>
      </div>
      <div class="callout__visual">
        <img :src="productImages.solutionsIsometric" class="recolor-blue" alt="LEAPS RTLS tracking across industrial facilities" loading="lazy" />
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'
import { productImages } from '@/data/images'

const { t, tm } = useI18n()
</script>

<style scoped>
.callout {
  background: var(--color-bg);
  padding: clamp(3rem, 6vw, 5rem) 0;
}

.callout__inner {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  align-items: center;
  gap: clamp(2rem, 5vw, 4rem);
}

.callout__subtitle {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.7;
  max-width: 520px;
  margin-bottom: 1.5rem;
}

.callout__checklist {
  display: grid;
  gap: 0.75rem;
  margin-bottom: 1.75rem;
}

.callout__checklist li {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.6;
}

.callout__check {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  background: var(--color-primary);
  color: white;
  border-radius: 50%;
  font-size: 0.6875rem;
  font-weight: 700;
  margin-top: 2px;
}

.callout__actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.callout__visual img {
  width: 100%;
  /* Fade the illustration into the section background, Qorvo-style */
  -webkit-mask-image: linear-gradient(270deg, black 65%, transparent 100%);
  mask-image: linear-gradient(270deg, black 65%, transparent 100%);
}

@media (max-width: 900px) {
  .callout__inner {
    grid-template-columns: 1fr;
  }

  .callout__visual {
    order: -1;
  }

  .callout__visual img {
    max-height: 280px;
    object-fit: contain;
    -webkit-mask-image: none;
    mask-image: none;
  }
}
</style>
