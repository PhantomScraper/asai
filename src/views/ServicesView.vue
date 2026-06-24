<template>
  <div class="services">
    <HeroSection
      :title="t('services.heroTitle')"
      :subtitle="t('services.heroSubtitle')"
      :cta-text="t('common.contactUs')"
      cta-link="/about#contact"
      :image-src="productImages.rtlsArchitecture"
      image-alt="LEAPS RTLS system architecture"
    />
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('services.introLabel') }}</span>
          <h2 class="section-title">{{ t('services.introTitle') }}</h2>
        </div>
        <div class="grid-3">
          <article v-for="cat in tm('services.categories')" :key="cat.title" class="card services__category-card">
            <h3>{{ cat.title }}</h3>
            <p>{{ cat.description }}</p>
            <RouterLink to="/about#contact" class="btn btn-outline">{{ t('common.contactUs') }}</RouterLink>
          </article>
        </div>
      </div>
    </section>
    <section class="section services__custom">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('services.customLabel') }}</span>
          <h2 class="section-title">{{ t('services.customTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('services.customSubtitle') }}</p>
        </div>
        <div class="grid-3">
          <article v-for="service in tm('services.customizations')" :key="service.title" class="card services__service-card">
            <h3>{{ service.title }}</h3>
            <p>{{ service.description }}</p>
          </article>
        </div>
      </div>
    </section>
    <CtaBanner />
  </div>
</template>

<script setup>
import HeroSection from '@/components/ui/HeroSection.vue'
import CtaBanner from '@/components/ui/CtaBanner.vue'
import { useI18n } from '@/i18n'
import { productImages } from '@/data/images'
const { t, tm } = useI18n()
</script>

<style scoped>
.services__category-card { text-align: center; display: flex; flex-direction: column; align-items: center; }
.services__category-card h3 { font-family: var(--font-display); font-size: 1.5rem; font-weight: 700; color: var(--color-primary); margin-bottom: 1rem; text-transform: uppercase; }
.services__category-card p { color: var(--color-text-muted); line-height: 1.65; margin-bottom: 1.5rem; flex: 1; }
.services__custom { background: var(--color-bg); }
.services__service-card h3 { font-family: var(--font-display); font-size: 1.25rem; font-weight: 600; margin-bottom: 0.75rem; }
.services__service-card p { font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.65; }
</style>
