<template>
  <div class="ps">
    <HeroSection
      :title="t('productsServices.heroTitle')"
      :subtitle="t('productsServices.heroSubtitle')"
      :showcase-primary="productImages.udkBanner"
      showcase-primary-alt="LEAPS UWB products"
    />

    <!-- Sticky in-page subnav -->
    <nav class="ps__subnav" aria-label="Page sections">
      <div class="container ps__subnav-row">
        <a href="#overview">{{ t('productsServices.subnav.overview') }}</a>
        <a href="#hardware">{{ t('productsServices.subnav.hardware') }}</a>
        <a href="#udk">{{ t('productsServices.subnav.udk') }}</a>
        <a href="#software">{{ t('productsServices.subnav.software') }}</a>
        <a href="#licensing">{{ t('productsServices.subnav.licensing') }}</a>
        <a href="#services">{{ t('productsServices.subnav.services') }}</a>
      </div>
    </nav>

    <!-- Ecosystem overview with network structure diagram -->
    <section id="overview" class="section ps__ecosystem">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('productsServices.ecosystem.label') }}</span>
          <h2 class="section-title section-title--lg">{{ t('productsServices.ecosystem.title') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('productsServices.ecosystem.text') }}</p>
        </div>
        <figure class="ps__diagram">
          <img :src="productImages.rtlsArchitecture" alt="LEAPS UWB RTLS network structure" loading="lazy" />
          <figcaption>{{ t('productsServices.ecosystem.imageCaption') }}</figcaption>
        </figure>
      </div>
    </section>

    <!-- What we offer (PT-LEAPS slide 3) -->
    <section class="section ps__offer">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('productsServices.offer.label') }}</span>
          <h2 class="section-title">{{ t('productsServices.offer.title') }}</h2>
        </div>
        <div class="grid-4 ps__offer-grid">
          <article v-for="item in tm('productsServices.offer.items')" :key="item.title" class="card ps__offer-card">
            <h3>{{ item.title }}</h3>
            <ul>
              <li v-for="(point, i) in item.points" :key="i">{{ point }}</li>
            </ul>
            <a :href="item.link" class="btn-ghost ps__offer-link">
              {{ item.cta }}
              <span class="arrow" aria-hidden="true">→</span>
            </a>
          </article>
        </div>
      </div>
    </section>

    <!-- Hardware: anchors & tags -->
    <section id="hardware" class="section ps__hardware">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('productsServices.hardware.label') }}</span>
          <h2 class="section-title section-title--lg">{{ t('productsServices.hardware.title') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('productsServices.hardware.note') }}</p>
        </div>

        <h3 class="ps__hw-heading">{{ t('productsServices.hardware.anchorsTitle') }}</h3>
        <p class="ps__hw-intro">{{ t('productsServices.hardware.anchorsIntro') }}</p>
        <div class="ps__hw-grid">
          <article v-for="(anchor, i) in tm('productsServices.hardware.anchors')" :key="anchor.id" class="card ps__product">
            <div class="ps__product-photo">
              <img :src="anchorSpecs[i].image" :alt="anchor.name" loading="lazy" />
            </div>
            <h4>{{ anchor.name }}</h4>
            <p class="ps__product-text">{{ anchor.text }}</p>
            <dl class="ps__specs">
              <template v-for="(value, key) in anchorSpecs[i].specs" :key="key">
                <div v-if="value && value !== '—'" class="ps__spec-row">
                  <dt>{{ t(`productsServices.hardware.specLabels.${key}`) }}</dt>
                  <dd>{{ value }}</dd>
                </div>
              </template>
              <div class="ps__spec-row">
                <dt>{{ t('productsServices.hardware.specLabels.partNumber') }}</dt>
                <dd>{{ anchorSpecs[i].partNumber }}</dd>
              </div>
            </dl>
            <a
              v-if="anchorSpecs[i].datasheet"
              :href="anchorSpecs[i].datasheet"
              target="_blank"
              rel="noopener noreferrer"
              class="btn btn-outline btn-sm ps__datasheet"
            >
              {{ t('common.datasheet') }}
            </a>
            <span v-else class="ps__datasheet ps__datasheet--soon">{{ t('common.datasheetSoon') }}</span>
          </article>
        </div>

        <h3 class="ps__hw-heading">{{ t('productsServices.hardware.tagsTitle') }}</h3>
        <p class="ps__hw-intro">{{ t('productsServices.hardware.tagsIntro') }}</p>
        <div class="ps__hw-grid ps__hw-grid--tags">
          <article v-for="(tag, i) in tm('productsServices.hardware.tags')" :key="tag.id" class="card ps__product">
            <div class="ps__product-photo">
              <img :src="tagSpecs[i].image" :alt="tag.name" loading="lazy" />
            </div>
            <h4>{{ tag.name }}</h4>
            <p class="ps__product-text">{{ tag.text }}</p>
            <dl class="ps__specs">
              <template v-for="(value, key) in tagSpecs[i].specs" :key="key">
                <div v-if="value && value !== '—'" class="ps__spec-row">
                  <dt>{{ t(`productsServices.hardware.specLabels.${key}`) }}</dt>
                  <dd>{{ value }}</dd>
                </div>
              </template>
              <div class="ps__spec-row">
                <dt>{{ t('productsServices.hardware.specLabels.partNumber') }}</dt>
                <dd>{{ tagSpecs[i].partNumber }}</dd>
              </div>
            </dl>
            <a
              :href="tagSpecs[i].datasheet"
              target="_blank"
              rel="noopener noreferrer"
              class="btn btn-outline btn-sm ps__datasheet"
            >
              {{ t('common.datasheet') }}
            </a>
          </article>
        </div>
      </div>
    </section>

    <!-- UDK evaluation kit -->
    <section id="udk" class="section ps__udk">
      <div class="container">
        <div class="ps__udk-grid">
          <img :src="productImages.udkKit" alt="UDK — All-in-One UWB Development Kit" class="ps__udk-photo" loading="lazy" />
          <div>
            <span class="section-label">{{ t('productsServices.udk.label') }}</span>
            <h2 class="section-title">{{ t('productsServices.udk.title') }}</h2>
            <p class="ps__lead">{{ t('productsServices.udk.description') }}</p>
            <h3 class="ps__subheading">{{ t('productsServices.udk.demosTitle') }}</h3>
            <ul class="ps__bullets">
              <li v-for="demo in tm('productsServices.udk.demos')" :key="demo">{{ demo }}</li>
            </ul>
            <div class="ps__udk-actions">
              <a :href="datasheets.udk" target="_blank" rel="noopener noreferrer" class="btn btn-primary">{{ t('productsServices.udk.datasheet') }}</a>
              <NuxtLink :to="docsLink('udk-start')" class="btn btn-outline">{{ t('productsServices.udk.quickStart') }}</NuxtLink>
            </div>
          </div>
        </div>

        <div class="ps__udk-kit card">
          <h3>{{ t('productsServices.udk.kitTitle') }}</h3>
          <ul class="ps__bullets ps__bullets--check">
            <li v-for="(item, i) in tm('productsServices.udk.kitContent')" :key="i">{{ item }}</li>
          </ul>
        </div>

        <div class="ps__distributors">
          <h3 class="ps__subheading">{{ t('productsServices.udk.distributorsTitle') }}</h3>
          <p class="ps__part-number">{{ t('productsServices.udk.partNumber') }}</p>
          <div class="ps__distributor-grid">
            <a
              v-for="dist in distributors"
              :key="dist.name"
              :href="dist.url"
              target="_blank"
              rel="noopener noreferrer"
              class="card ps__distributor"
            >
              <img :src="dist.logo" :alt="dist.name" loading="lazy" />
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Software -->
    <section id="software" class="section ps__software">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('productsServices.software.label') }}</span>
          <h2 class="section-title section-title--lg">{{ t('productsServices.software.title') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('productsServices.software.intro') }}</p>
        </div>
        <div class="grid-4 ps__software-grid">
          <article v-for="comp in tm('productsServices.software.components')" :key="comp.name" class="card ps__software-card">
            <h3>{{ comp.name }}</h3>
            <p>{{ comp.text }}</p>
          </article>
        </div>
        <div class="ps__software-actions">
          <a :href="datasheets.rtls" target="_blank" rel="noopener noreferrer" class="btn btn-primary">{{ t('productsServices.software.datasheet') }}</a>
          <a :href="externalLinks.docs" target="_blank" rel="noopener noreferrer" class="btn btn-outline">{{ t('productsServices.software.docs') }}</a>
        </div>
      </div>
    </section>

    <!-- Technology licensing -->
    <section id="licensing" class="section ps__licensing">
      <div class="container ps__licensing-grid">
        <div>
          <span class="section-label">{{ t('productsServices.licensing.label') }}</span>
          <h2 class="section-title">{{ t('productsServices.licensing.title') }}</h2>
          <p class="ps__lead">{{ t('productsServices.licensing.text') }}</p>
          <ul class="ps__bullets ps__bullets--check">
            <li v-for="(point, i) in tm('productsServices.licensing.points')" :key="i">{{ point }}</li>
          </ul>
          <RouterLink to="/about#contact" class="btn btn-primary">{{ t('productsServices.licensing.cta') }}</RouterLink>
        </div>
        <img :src="productImages.rtlsIllustrations" alt="LEAPS UWB technology illustration" class="ps__licensing-image" loading="lazy" />
      </div>
    </section>

    <!-- Design services & support -->
    <section id="services" class="section ps__services">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('productsServices.services.label') }}</span>
          <h2 class="section-title section-title--lg">{{ t('productsServices.services.title') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('productsServices.services.text') }}</p>
        </div>
        <div class="grid-3">
          <article v-for="card in tm('productsServices.services.cards')" :key="card.title" class="card ps__service-card">
            <h3>{{ card.title }}</h3>
            <p>{{ card.text }}</p>
          </article>
        </div>
        <div class="ps__support card">
          <div>
            <h3>{{ t('productsServices.services.supportTitle') }}</h3>
            <p>{{ t('productsServices.services.supportText') }}</p>
          </div>
          <RouterLink to="/about#contact" class="btn btn-primary">{{ t('productsServices.services.cta') }}</RouterLink>
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
import { anchorSpecs, tagSpecs, datasheets, distributors, externalLinks } from '@/data/site'
import { productImages } from '@/data/images'

const { t, tm } = useI18n()
const { docsLink } = useDocs()
</script>

<style scoped>
/* Sticky in-page subnav */
.ps__subnav {
  position: sticky;
  top: var(--header-height);
  z-index: 500;
  background: white;
  border-bottom: 1px solid var(--color-border);
}

.ps__subnav-row {
  display: flex;
  align-items: center;
  gap: 2rem;
  overflow-x: auto;
  scrollbar-width: none;
}

.ps__subnav-row::-webkit-scrollbar {
  display: none;
}

.ps__subnav-row a {
  font-family: var(--font-display);
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--color-text-muted);
  padding: 0.875rem 0;
  white-space: nowrap;
  transition: color var(--transition);
}

.ps__subnav-row a:hover {
  color: var(--color-primary-dark);
}

.ps__ecosystem {
  background: white;
}

.ps__diagram {
  max-width: 880px;
  margin: 0 auto;
}

.ps__diagram img {
  width: 100%;
  border: 1px solid var(--color-border-light);
  border-radius: var(--radius-lg);
  background: white;
  padding: clamp(0.75rem, 2vw, 1.5rem);
  box-shadow: var(--shadow-md);
}

.ps__diagram figcaption {
  margin-top: 0.75rem;
  text-align: center;
  font-size: 0.875rem;
  color: var(--color-text-light);
}

.ps__offer {
  background: var(--color-bg);
}

.ps__offer-card {
  display: flex;
  flex-direction: column;
}

.ps__offer-card h3 {
  font-family: var(--font-display);
  font-size: 1.0625rem;
  font-weight: 600;
  color: var(--color-primary-dark);
  margin-bottom: 0.875rem;
}

.ps__offer-card ul {
  display: grid;
  gap: 0.5rem;
  flex: 1;
  margin-bottom: 1rem;
}

.ps__offer-card li {
  position: relative;
  padding-left: 1.125rem;
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.6;
}

.ps__offer-card li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.55em;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-primary);
}

.ps__offer-link {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  font-family: var(--font-display);
  font-size: 0.875rem;
  font-weight: 600;
}

/* Hardware */
.ps__hardware {
  background: white;
}

.ps__hw-heading {
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 2.5vw, 1.5rem);
  font-weight: 500;
  margin: clamp(1.5rem, 4vw, 2.5rem) 0 0.5rem;
}

.ps__hw-intro {
  color: var(--color-text-muted);
  line-height: 1.7;
  max-width: 720px;
  margin-bottom: 1.5rem;
}

.ps__hw-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.ps__hw-grid--tags {
  grid-template-columns: repeat(4, 1fr);
}

.ps__product {
  display: flex;
  flex-direction: column;
  padding: 1.5rem;
}

.ps__product-photo {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 150px;
  margin-bottom: 1rem;
  background: var(--color-bg);
  border-radius: var(--radius-sm);
  overflow: hidden;
}

.ps__product-photo img {
  max-height: 130px;
  width: auto;
  object-fit: contain;
}

.ps__product h4 {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
  line-height: 1.4;
  margin-bottom: 0.5rem;
}

.ps__product-text {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.6;
  margin-bottom: 1rem;
}

.ps__specs {
  display: grid;
  gap: 0.375rem;
  margin-bottom: 1.25rem;
  flex: 1;
}

.ps__spec-row {
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
  gap: 0.5rem;
  font-size: 0.8125rem;
  padding-bottom: 0.375rem;
  border-bottom: 1px dashed var(--color-border-light);
}

.ps__spec-row dt {
  color: var(--color-text-light);
}

.ps__spec-row dd {
  color: var(--color-text);
}

.ps__datasheet {
  align-self: flex-start;
}

.ps__datasheet--soon {
  font-size: 0.8125rem;
  color: var(--color-text-light);
  font-style: italic;
}

/* UDK */
.ps__udk {
  background: var(--tint-brand);
  border-radius: 0 0 var(--radius-corner-lg) 0;
}

.ps__udk-grid {
  display: grid;
  grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr);
  gap: clamp(2rem, 5vw, 3.5rem);
  align-items: center;
  margin-bottom: clamp(1.5rem, 4vw, 2.5rem);
}

.ps__udk-photo {
  width: 100%;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  border: 1px solid var(--color-border-light);
  background: #111;
  object-fit: contain;
}

.ps__lead {
  color: var(--color-text-muted);
  line-height: 1.75;
  margin: 0.75rem 0 1.25rem;
}

.ps__subheading {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
}

.ps__bullets {
  display: grid;
  gap: 0.625rem;
  margin-bottom: 1.5rem;
}

.ps__bullets li {
  position: relative;
  padding-left: 1.25rem;
  color: var(--color-text-muted);
  font-size: 0.9375rem;
  line-height: 1.65;
}

.ps__bullets li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.55em;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--color-primary);
}

.ps__bullets--check li {
  padding-left: 1.5rem;
}

.ps__bullets--check li::before {
  content: '✓';
  background: none;
  width: auto;
  height: auto;
  top: 0;
  color: var(--color-primary);
  font-weight: 700;
}

.ps__udk-actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.ps__udk-kit {
  margin-bottom: clamp(1.5rem, 4vw, 2.5rem);
}

.ps__udk-kit h3 {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.ps__part-number {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  margin-bottom: 1.25rem;
}

.ps__distributor-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 1rem;
}

.ps__distributor {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 80px;
  padding: 1rem 1.25rem;
}

.ps__distributor img {
  max-width: 100%;
  max-height: 40px;
  object-fit: contain;
}

/* Software */
.ps__software {
  background: white;
}

.ps__software-card h3 {
  font-family: var(--font-display);
  font-size: 1.0625rem;
  font-weight: 600;
  color: var(--color-primary-dark);
  margin-bottom: 0.625rem;
}

.ps__software-card p {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.65;
}

.ps__software-actions {
  display: flex;
  justify-content: center;
  gap: 0.875rem;
  flex-wrap: wrap;
  margin-top: 2rem;
}

/* Licensing */
.ps__licensing {
  background: var(--color-bg);
}

.ps__licensing-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
  gap: clamp(2rem, 5vw, 3.5rem);
  align-items: center;
}

.ps__licensing-image {
  width: 100%;
  border-radius: var(--radius-lg);
  background: white;
  border: 1px solid var(--color-border-light);
  box-shadow: var(--shadow-md);
}

/* Services */
.ps__services {
  background: white;
}

.ps__service-card h3 {
  font-family: var(--font-display);
  font-size: 1.0625rem;
  font-weight: 600;
  color: var(--color-primary-dark);
  margin-bottom: 0.625rem;
}

.ps__service-card p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.65;
}

.ps__support {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  flex-wrap: wrap;
  margin-top: 2rem;
  background: var(--tint-brand-faint);
}

.ps__support h3 {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.ps__support p {
  color: var(--color-text-muted);
  line-height: 1.65;
  max-width: 640px;
}

@media (max-width: 1024px) {
  .ps__hw-grid,
  .ps__hw-grid--tags {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 900px) {
  .ps__udk-grid,
  .ps__licensing-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .ps__hw-grid,
  .ps__hw-grid--tags {
    grid-template-columns: 1fr;
  }
}
</style>
