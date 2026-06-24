<template>
  <div class="products">
    <HeroSection
      :title="t('products.heroTitle')"
      :subtitle="t('products.heroSubtitle')"
      :cta-text="t('products.ctaUdk')"
      :cta-link="docsLink('udk-start')"
      :showcase-primary="productImages.udkBanner"
      :showcase-secondary="productImages.udkKit"
      showcase-primary-alt="All-in-One Ultra-Wideband Development Kit"
      showcase-secondary-alt="UDK kit packaging and devices"
    />
    <section class="section products__overview">
      <div class="container products__overview-grid">
        <img :src="productImages.udkKit" alt="" class="products__photo" loading="lazy" />
        <div>
          <span class="section-label">{{ t('products.demosLabel') }}</span>
          <h2 class="section-title">{{ t('products.demosTitle') }}</h2>
          <p class="products__lead">{{ tm('productData.description') }}</p>
          <ul class="products__demo-list">
            <li v-for="demo in tm('productData.demos')" :key="demo">{{ demo }}</li>
          </ul>
          <NuxtLink :to="docsLink('udk')" class="btn btn-outline">{{ t('products.readUdk') }}</NuxtLink>
        </div>
      </div>
    </section>
    <section class="section products__kit">
      <div class="container products__kit-grid">
        <img :src="productImages.udkBanner" alt="" class="products__kit-image" loading="lazy" />
        <div>
          <span class="section-label">{{ t('products.kitLabel') }}</span>
          <h2 class="section-title">{{ t('products.kitTitle') }}</h2>
          <ul class="products__list">
            <li v-for="(item, i) in tm('productData.kitContent')" :key="'k'+i">{{ item }}</li>
          </ul>
          <h3 class="products__subheading">{{ t('products.alsoIncluded') }}</h3>
          <ul class="products__list products__list--check">
            <li v-for="(item, i) in tm('productData.kitIncludes')" :key="'i'+i">{{ item }}</li>
          </ul>
        </div>
      </div>
    </section>
    <section class="section products__visual">
      <div class="container">
        <ProductShowcase
          :primary-image="productImages.rtlsStack"
          primary-alt="LEAPS RTLS architecture with UDK hardware"
          variant="banner"
        />
      </div>
    </section>
    <section class="section products__distributors">
      <div class="container">
        <span class="section-label">{{ t('products.distributorsLabel') }}</span>
        <h2 class="section-title">{{ t('products.distributorsTitle') }}</h2>
        <p class="section-subtitle">{{ t('products.partNumber') }}</p>
        <div class="products__distributor-grid">
          <a v-for="dist in distributors" :key="dist.name" :href="dist.url" target="_blank" rel="noopener noreferrer" class="products__distributor-card card">
            <img :src="dist.logo" :alt="dist.name" class="products__distributor-logo" loading="lazy" />
          </a>
        </div>
        <div class="products__order card">
          <h3>{{ t('products.orderTitle') }}</h3>
          <p><strong>{{ t('products.partNumber') }}</strong></p>
          <p>{{ t('products.orderText') }}</p>
          <RouterLink to="/about#contact" class="btn btn-primary">{{ t('common.getInTouch') }}</RouterLink>
        </div>
      </div>
    </section>
    <CtaBanner />
  </div>
</template>

<script setup>
import HeroSection from '@/components/ui/HeroSection.vue'
import CtaBanner from '@/components/ui/CtaBanner.vue'
import ProductShowcase from '@/components/ui/ProductShowcase.vue'
import { useI18n } from '@/i18n'
import { distributors, externalLinks } from '@/data/site'
import { productImages } from '@/data/images'

const { t, tm } = useI18n()
const { docsLink } = useDocs()
</script>

<style scoped>
.products__overview { background: white; }
.products__overview-grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.1fr); gap: clamp(2rem, 5vw, 3.5rem); align-items: start; }
.products__photo { width: 100%; border-radius: var(--radius-lg); box-shadow: var(--shadow-md); border: 1px solid var(--color-border-light); background: #111; object-fit: contain; }
.products__lead { color: var(--color-text-muted); line-height: 1.75; margin: 1rem 0 1.5rem; }
.products__demo-list { display: grid; gap: 0.625rem; margin-bottom: 1.75rem; }
.products__demo-list li { position: relative; padding-left: 1.25rem; color: var(--color-text-muted); font-size: 0.9375rem; }
.products__demo-list li::before { content: ''; position: absolute; left: 0; top: 0.55em; width: 7px; height: 7px; border-radius: 50%; background: var(--color-primary); }
.products__kit { background: var(--color-bg); }
.products__kit-grid { display: grid; grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr); gap: clamp(2rem, 5vw, 3.5rem); align-items: center; }
.products__kit-image { width: 100%; max-width: 520px; margin: 0 auto; display: block; border-radius: var(--radius-lg); background: white; padding: 0.75rem; border: 1px solid var(--color-border-light); box-shadow: var(--shadow-md); }
.products__visual { background: white; padding-top: 2rem; padding-bottom: 2rem; }
.products__subheading { font-family: var(--font-display); font-size: 1rem; font-weight: 600; margin: 1.5rem 0 0.75rem; }
.products__list { display: grid; gap: 0.75rem; }
.products__list li { color: var(--color-text-muted); line-height: 1.65; font-size: 0.9375rem; }
.products__list--check li { position: relative; padding-left: 1.5rem; }
.products__list--check li::before { content: '✓'; position: absolute; left: 0; color: var(--color-primary); font-weight: 700; }
.products__distributors { background: var(--color-bg); }
.products__distributor-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 1rem; margin: 2rem 0 2.5rem; }
.products__distributor-card { display: flex; align-items: center; justify-content: center; min-height: 88px; padding: 1rem 1.25rem; }
.products__distributor-logo { max-width: 100%; max-height: 44px; object-fit: contain; }
.products__order { padding: clamp(1.5rem, 3vw, 2.5rem); background: white; }
.products__order h3 { font-family: var(--font-display); font-size: 1.25rem; margin-bottom: 1rem; }
.products__order p { color: var(--color-text-muted); margin-bottom: 0.75rem; line-height: 1.6; }
.products__order .btn { margin-top: 1.25rem; }
@media (max-width: 900px) { .products__overview-grid, .products__kit-grid { grid-template-columns: 1fr; } }
</style>
