<template>
  <div class="solutions">
    <HeroSection
      :title="t('solutions.heroTitle')"
      :subtitle="t('solutions.heroSubtitle')"
      :cta-text="t('common.contactUs')"
      cta-link="/about#contact"
      :showcase-primary="productImages.solutionsIsometric"
      showcase-primary-alt="LEAPS RTLS isometric solution overview"
    />

    <!-- Qorvo-style sticky in-page subnav -->
    <nav class="solutions__subnav" aria-label="Page sections">
      <div class="container solutions__subnav-row">
        <a href="#applications">{{ t('solutions.appsLabel') }}</a>
        <a href="#use-cases">{{ t('solutions.useCasesLabel') }}</a>
        <a href="#comparison">{{ t('solutions.rtlsComparison.label') }}</a>
        <a href="#pillars">{{ tm('solutions.pillars')[0].label }}</a>
        <a href="#uniqueness">{{ t('solutions.uniqueLabel') }}</a>
        <a href="#stack">{{ t('solutions.stackLabel') }}</a>
        <a href="#technology">{{ t('solutions.techLabel') }}</a>
      </div>
    </nav>

    <!-- Application examples from real deployments — details live on the Projects page -->
    <section id="applications" class="section solutions__apps">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('solutions.appsLabel') }}</span>
          <h2 class="section-title">{{ t('solutions.appsTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('solutions.appsSubtitle') }}</p>
        </div>
        <div class="grid-3">
          <RouterLink
            v-for="(example, i) in tm('solutions.appExamples')"
            :key="example.title"
            :to="`/projects#uc-${appExampleSlugs[i]}`"
            class="card solutions__app"
          >
            <span class="solutions__app-media">
              <img :src="appExampleImages[i]" :alt="example.title" loading="lazy" />
            </span>
            <span class="solutions__app-body">
              <h3>{{ example.title }}</h3>
              <ul class="solutions__app-highlights">
                <li v-for="(hl, j) in example.highlights" :key="j">{{ hl }}</li>
              </ul>
              <span class="solutions__app-more">
                {{ t('common.readMore') }}
                <span class="arrow-circle" aria-hidden="true">→</span>
              </span>
            </span>
          </RouterLink>
        </div>
      </div>
    </section>

    <section id="use-cases" class="section solutions__use-cases">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('solutions.useCasesLabel') }}</span>
          <h2 class="section-title">{{ t('solutions.useCasesTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('solutions.useCasesSubtitle') }}</p>
        </div>
        <ProductShowcase
          :primary-image="productImages.rtlsUseCases"
          primary-alt="Object tracking, indoor navigation, and geofencing with LEAPS RTLS"
          variant="banner"
        />
      </div>
    </section>

    <!-- LEAPS RTLS vs PANS PRO RTLS vs PANS RTLS comparison table -->
    <section id="comparison" class="section solutions__comparison">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('solutions.rtlsComparison.label') }}</span>
          <h2 class="section-title">{{ t('solutions.rtlsComparison.title') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('solutions.rtlsComparison.subtitle') }}</p>
        </div>
        <div class="solutions__table-wrap">
          <table class="solutions__table">
            <thead>
              <tr>
                <th v-for="(col, i) in tm('solutions.rtlsComparison.columns')" :key="i" :class="{ 'solutions__table-leaps': i === 1 }">
                  {{ col }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="row in tm('solutions.rtlsComparison.rows')" :key="row.label">
                <th scope="row">{{ row.label }}</th>
                <td v-for="(value, i) in row.values" :key="i" :class="{ 'solutions__table-leaps': i === 0 }">
                  {{ value }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <ul class="solutions__table-notes">
          <li v-for="(note, i) in tm('solutions.rtlsComparison.notes')" :key="i">{{ note }}</li>
        </ul>
        <a :href="externalLinks.comparison" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">
          {{ t('solutions.rtlsComparison.source') }}
        </a>
      </div>
    </section>

    <!-- Alternating callout rows (Qorvo interior-page idiom) -->
    <section id="pillars" class="section solutions__pillars">
      <div class="container solutions__pillars-list">
        <article
          v-for="(pillar, i) in tm('solutions.pillars')"
          :key="pillar.title"
          class="solutions__pillar"
          :class="{ 'solutions__pillar--flip': i % 2 === 1 }"
        >
          <div class="solutions__pillar-text">
            <span class="section-label">{{ pillar.label }}</span>
            <h2 class="section-title section-title--lg">{{ pillar.title }}</h2>
            <p>{{ pillar.description }}</p>
            <RouterLink v-if="i === 0" to="/about#contact" class="btn btn-primary">{{ pillar.linkText }}</RouterLink>
            <a v-else :href="i === 1 ? '#uniqueness' : '#technology'" class="btn btn-outline">{{ pillar.linkText }}</a>
          </div>
          <div class="solutions__pillar-visual">
            <img :src="pillarImages[i]" :alt="pillar.title" loading="lazy" />
          </div>
        </article>
      </div>
    </section>

    <!-- Airy borderless feature grid -->
    <section id="uniqueness" class="section solutions__uniqueness">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('solutions.uniqueLabel') }}</span>
          <h2 class="section-title">{{ t('solutions.uniqueTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('solutions.uniqueSubtitle') }}</p>
        </div>
        <div class="solutions__features-grid">
          <article v-for="item in tm('solutions.uniquenessFeatures')" :key="item.title" class="solutions__feature">
            <h4>{{ item.title }}</h4>
            <p>{{ item.description }}</p>
          </article>
        </div>
      </div>
    </section>

    <section id="stack" class="section solutions__stack">
      <div class="container solutions__stack-grid">
        <div>
          <span class="section-label">{{ t('solutions.stackLabel') }}</span>
          <h2 class="section-title">{{ t('solutions.stackTitle') }}</h2>
          <p class="solutions__stack-text">{{ t('solutions.stackSubtitle') }}</p>
          <NuxtLink :to="docsLink('leaps-rtls')" class="btn btn-light">{{ t('common.learnMore') }}</NuxtLink>
        </div>
        <img :src="productImages.rtlsStack" alt="" class="solutions__stack-image" loading="lazy" />
      </div>
    </section>

    <section id="technology" class="section solutions__technology">
      <div class="container">
        <div class="solutions__tech-intro">
          <span class="section-label">{{ t('solutions.techLabel') }}</span>
          <h2 class="section-title">{{ t('solutions.techTitle') }}</h2>
          <p class="solutions__tech-text">{{ t('solutions.techText') }}</p>
          <a :href="externalLinks.qorvoUwb" target="_blank" rel="noopener noreferrer" class="btn btn-outline">{{ t('solutions.techButton') }}</a>
        </div>
        <div class="solutions__tech-chart">
          <ComparisonChart
            :src="productImages.uwbComparison"
            :alt="t('solutions.comparisonTitle')"
            :title="t('solutions.comparisonTitle')"
            :hint="t('solutions.comparisonHint')"
            :enlarge-label="t('solutions.comparisonEnlarge')"
          />
          <p class="solutions__tech-source">
            <a :href="externalLinks.qorvoUwb" target="_blank" rel="noopener noreferrer">{{ t('solutions.comparisonSource') }}</a>
          </p>
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
import ComparisonChart from '@/components/ui/ComparisonChart.vue'
import { useI18n } from '@/i18n'
import { externalLinks } from '@/data/site'
import { productImages, solutionPillarImages, appExampleImages, appExampleSlugs } from '@/data/images'

const { t, tm } = useI18n()
const { docsLink } = useDocs()
const pillarImages = solutionPillarImages
</script>

<style scoped>
/* Sticky in-page subnav */
.solutions__subnav {
  position: sticky;
  top: var(--header-height);
  z-index: 500;
  background: white;
  border-bottom: 1px solid var(--color-border);
}

.solutions__subnav-row {
  display: flex;
  align-items: center;
  gap: 2rem;
  overflow-x: auto;
  scrollbar-width: none;
}

.solutions__subnav-row::-webkit-scrollbar {
  display: none;
}

.solutions__subnav-row a {
  font-family: var(--font-display);
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--color-text-muted);
  padding: 0.875rem 0;
  white-space: nowrap;
  transition: color var(--transition);
}

.solutions__subnav-row a:hover {
  color: var(--color-primary-dark);
}

/* Application examples — clickable cards leading to the Projects detail blocks */
.solutions__apps {
  background: white;
}

.solutions__app {
  padding: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.solutions__app-media {
  display: block;
  aspect-ratio: 16 / 10;
  background: var(--color-bg);
  overflow: hidden;
}

.solutions__app-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition);
}

.solutions__app:hover .solutions__app-media img {
  transform: scale(1.03);
}

.solutions__app-body {
  display: flex;
  flex-direction: column;
  flex: 1;
  padding: 1.25rem 1.5rem 1.5rem;
}

.solutions__app h3 {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--color-primary-dark);
  margin-bottom: 0.875rem;
}

.solutions__app-highlights {
  display: grid;
  gap: 0.5rem;
  flex: 1;
  margin-bottom: 1.25rem;
}

.solutions__app-highlights li {
  position: relative;
  padding-left: 1.375rem;
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.6;
}

.solutions__app-highlights li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: var(--color-primary);
  font-weight: 700;
}

.solutions__app-more {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  font-family: var(--font-display);
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--color-primary-dark);
}

.solutions__use-cases {
  background: var(--color-bg);
}

/* RTLS generations comparison table */
.solutions__comparison {
  background: white;
}

.solutions__table-wrap {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: white;
  box-shadow: var(--shadow-sm);
}

.solutions__table {
  width: 100%;
  min-width: 760px;
  border-collapse: collapse;
  font-size: 0.875rem;
}

.solutions__table thead th {
  font-family: var(--font-display);
  font-weight: 600;
  text-align: left;
  padding: 0.875rem 1rem;
  background: var(--color-ink);
  color: white;
  white-space: nowrap;
}

.solutions__table thead th.solutions__table-leaps {
  background: var(--color-primary);
}

.solutions__table tbody th {
  text-align: left;
  font-weight: 500;
  color: var(--color-text);
  padding: 0.625rem 1rem;
  border-top: 1px solid var(--color-border-light);
  background: var(--tint-brand-faint);
  min-width: 200px;
}

.solutions__table tbody td {
  padding: 0.625rem 1rem;
  border-top: 1px solid var(--color-border-light);
  color: var(--color-text-muted);
  vertical-align: top;
}

.solutions__table tbody td.solutions__table-leaps {
  color: var(--color-text);
  font-weight: 500;
  background: var(--tint-brand-soft);
}

.solutions__table-notes {
  display: grid;
  gap: 0.25rem;
  margin: 1rem 0 1.25rem;
}

.solutions__table-notes li {
  font-size: 0.8125rem;
  color: var(--color-text-light);
}

/* Alternating callout rows */
.solutions__pillars {
  background: var(--color-bg);
}

.solutions__pillars-list {
  display: grid;
  gap: clamp(3rem, 7vw, 5.5rem);
}

.solutions__pillar {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  align-items: center;
  gap: clamp(2rem, 5vw, 4rem);
}

.solutions__pillar-text p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.7;
  max-width: 520px;
  margin: 1rem 0 1.75rem;
}

.solutions__pillar-visual img {
  width: 100%;
  /* Fade the illustration toward the text side, Qorvo-style */
  -webkit-mask-image: linear-gradient(270deg, black 65%, transparent 100%);
  mask-image: linear-gradient(270deg, black 65%, transparent 100%);
}

/* Flipped rows: image left, text right */
.solutions__pillar--flip .solutions__pillar-visual {
  order: -1;
}

.solutions__pillar--flip .solutions__pillar-visual img {
  -webkit-mask-image: linear-gradient(90deg, black 65%, transparent 100%);
  mask-image: linear-gradient(90deg, black 65%, transparent 100%);
}

/* Airy borderless feature grid */
.solutions__uniqueness {
  background: white;
}

.solutions__features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 2rem 2.5rem;
}

.solutions__feature::before {
  content: '';
  display: block;
  width: 24px;
  height: 3px;
  background: var(--color-primary);
  margin-bottom: 0.75rem;
}

.solutions__feature h4 {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-primary-dark);
  margin-bottom: 0.5rem;
}

.solutions__feature p {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.6;
}

/* Qorvo signature: dark gray gradient banner */
.solutions__stack {
  background: var(--gradient-gray);
  color: white;
}

.solutions__stack .section-label {
  color: var(--color-primary-light);
}

.solutions__stack .section-title {
  color: white;
}

.solutions__stack-grid {
  display: grid;
  grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr);
  gap: clamp(2rem, 5vw, 3.5rem);
  align-items: center;
}

.solutions__stack-text {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.75;
  margin: 1.25rem 0 1.75rem;
}

.solutions__stack-image {
  width: 100%;
  max-height: 520px;
  object-fit: contain;
  border-radius: var(--radius-lg);
  background: white;
  border: 1px solid var(--color-border-light);
  box-shadow: var(--shadow-md);
  padding: 1rem;
}

.solutions__technology {
  background: var(--color-bg);
}

.solutions__tech-intro {
  max-width: 720px;
  margin-bottom: clamp(2rem, 4vw, 3rem);
}

.solutions__tech-text {
  color: var(--color-text-muted);
  line-height: 1.75;
  margin: 1.25rem 0 1.75rem;
}

/* Keep the Qorvo technology chart compact within the layout */
.solutions__tech-chart {
  max-width: 880px;
  margin: 0 auto;
}

.solutions__tech-source {
  margin-top: 0.875rem;
  font-size: 0.8125rem;
  color: var(--color-text-light);
}

.solutions__tech-source a:hover {
  text-decoration: underline;
}

@media (max-width: 900px) {
  .solutions__pillar {
    grid-template-columns: 1fr;
  }

  .solutions__pillar-visual {
    order: -1;
  }

  .solutions__pillar--flip .solutions__pillar-visual {
    order: -1;
  }

  .solutions__pillar-visual img,
  .solutions__pillar--flip .solutions__pillar-visual img {
    max-height: 280px;
    object-fit: contain;
    -webkit-mask-image: none;
    mask-image: none;
  }

  .solutions__stack-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .solutions__subnav-row {
    gap: 1.5rem;
  }
}
</style>
