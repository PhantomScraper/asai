<template>
  <section class="tbanner">
    <div class="container tbanner__inner">
      <div class="tbanner__text">
        <h2>{{ t('home.techBanner.title') }}</h2>
        <p>{{ t('home.techBanner.text') }}</p>
        <RouterLink to="/our-products" class="btn btn-light">{{ t('home.techBanner.cta') }}</RouterLink>
      </div>
      <div class="tbanner__visual">
        <img :src="productImages.udkKit" alt="UDK Ultra-Wideband development kit" loading="lazy" />
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'
import { productImages } from '@/data/images'

const { t } = useI18n()
</script>

<style scoped>
.tbanner {
  background: var(--gradient-gray);
  color: white;
  overflow: hidden;
}

.tbanner__inner {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  align-items: center;
  gap: clamp(2rem, 5vw, 4rem);
  padding-top: clamp(2.5rem, 5vw, 3.5rem);
  padding-bottom: clamp(2.5rem, 5vw, 3.5rem);
}

.tbanner__text h2 {
  font-family: var(--font-display);
  font-size: clamp(1.375rem, 2.5vw, 1.625rem);
  font-weight: 400;
  margin-bottom: 0.75rem;
}

.tbanner__text p {
  font-size: 0.9375rem;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.8);
  max-width: 460px;
  margin-bottom: 1.5rem;
}

.tbanner__visual {
  /* Qorvo's signature one-sided pill crop */
  border-radius: 999px 0 0 999px;
  overflow: hidden;
  max-height: 280px;
}

.tbanner__visual img {
  width: 100%;
  height: 280px;
  object-fit: cover;
}

@media (max-width: 900px) {
  .tbanner__inner {
    grid-template-columns: 1fr;
  }

  .tbanner__visual {
    border-radius: var(--radius-md);
    max-height: 220px;
  }

  .tbanner__visual img {
    height: 220px;
  }
}
</style>
