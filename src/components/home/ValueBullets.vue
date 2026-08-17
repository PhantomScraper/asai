<template>
  <section class="vbul section">
    <div class="container vbul__inner">
      <div class="vbul__text">
        <span class="section-label">{{ t('home.values.label') }}</span>
        <h2 class="section-title section-title--lg">{{ t('home.values.title') }}</h2>
        <ul class="vbul__list">
          <li v-for="(item, i) in tm('home.values.items')" :key="i">
            <span class="vbul__check" aria-hidden="true">✓</span>
            <span>{{ item }}</span>
          </li>
        </ul>
        <RouterLink to="/projects" class="btn btn-primary">{{ t('home.values.cta') }}</RouterLink>
      </div>
      <div class="vbul__visual">
        <img :src="productImages.solutionsIsometric" alt="Assets and people tracked in real time across a facility" loading="lazy" />
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
.vbul {
  background: var(--color-bg);
}

.vbul__inner {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  align-items: center;
  gap: clamp(2rem, 5vw, 4rem);
}

.vbul__list {
  display: grid;
  gap: 0.875rem;
  margin: 1.25rem 0 1.75rem;
}

.vbul__list li {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.65;
}

.vbul__check {
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

.vbul__visual img {
  width: 100%;
  -webkit-mask-image: linear-gradient(270deg, black 65%, transparent 100%);
  mask-image: linear-gradient(270deg, black 65%, transparent 100%);
}

@media (max-width: 900px) {
  .vbul__inner {
    grid-template-columns: 1fr;
  }

  .vbul__visual {
    order: -1;
  }

  .vbul__visual img {
    max-height: 280px;
    object-fit: contain;
    -webkit-mask-image: none;
    mask-image: none;
  }
}
</style>
