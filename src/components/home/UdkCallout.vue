<template>
  <section id="udk" class="udkc">
    <div class="container udkc__inner">
      <div class="udkc__text">
        <span class="udkc__label">{{ t('home.udk.label') }}</span>
        <h2>{{ t('home.udk.title') }}</h2>
        <p>{{ t('home.udk.text') }}</p>
        <ul class="udkc__list">
          <li v-for="(item, i) in tm('home.udk.bullets')" :key="i">{{ item }}</li>
        </ul>
        <div class="udkc__actions">
          <RouterLink to="/products-services#udk" class="btn btn-primary">{{ t('home.udk.details') }}</RouterLink>
          <a :href="datasheets.udk" target="_blank" rel="noopener noreferrer" class="btn btn-light">{{ t('home.udk.datasheet') }}</a>
          <a :href="externalLinks.store" target="_blank" rel="noopener noreferrer" class="btn btn-light">{{ t('home.udk.store') }}</a>
        </div>
      </div>
      <div class="udkc__visual">
        <img :src="productImages.udkKit" alt="UDK Ultra-Wideband demo kit" loading="lazy" />
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'
import { productImages } from '@/data/images'
import { datasheets, externalLinks } from '@/data/site'

const { t, tm } = useI18n()
</script>

<style scoped>
.udkc {
  background: var(--gradient-gray);
  color: white;
  overflow: hidden;
}

.udkc__inner {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  align-items: center;
  gap: clamp(2rem, 5vw, 4rem);
  padding-top: clamp(2.5rem, 5vw, 3.5rem);
  padding-bottom: clamp(2.5rem, 5vw, 3.5rem);
}

.udkc__label {
  display: block;
  font-family: var(--font-display);
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--color-primary-light);
  margin-bottom: 0.75rem;
}

.udkc__text h2 {
  font-family: var(--font-display);
  font-size: clamp(1.375rem, 2.5vw, 1.75rem);
  font-weight: 400;
  margin-bottom: 0.75rem;
}

.udkc__text p {
  font-size: 0.9375rem;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.8);
  max-width: 520px;
  margin-bottom: 1.25rem;
}

.udkc__list {
  display: grid;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.udkc__list li {
  position: relative;
  padding-left: 1.25rem;
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.85);
  line-height: 1.6;
}

.udkc__list li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.55em;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-primary-light);
}

.udkc__actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.udkc__visual {
  border-radius: 999px 0 0 999px;
  overflow: hidden;
  max-height: 300px;
}

.udkc__visual img {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

@media (max-width: 900px) {
  .udkc__inner {
    grid-template-columns: 1fr;
  }

  .udkc__visual {
    border-radius: var(--radius-md);
    max-height: 220px;
  }

  .udkc__visual img {
    height: 220px;
  }
}
</style>
