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
        <a href="#pillars">{{ tm('solutions.pillars')[0].label }}</a>
        <a href="#use-cases">{{ t('solutions.useCasesLabel') }}</a>
        <a href="#uniqueness">{{ t('solutions.uniqueLabel') }}</a>
        <a href="#stack">{{ t('solutions.stackLabel') }}</a>
        <a href="#technology">{{ t('solutions.techLabel') }}</a>
      </div>
    </nav>

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
            <img :src="pillarImages[i]" :alt="pillar.title" :class="{ 'recolor-blue': needsRecolor(pillarImages[i]) }" loading="lazy" />
          </div>
        </article>
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
        <ComparisonChart
          :src="productImages.uwbComparison"
          :alt="t('solutions.comparisonTitle')"
          :title="t('solutions.comparisonTitle')"
          :hint="t('solutions.comparisonHint')"
          :enlarge-label="t('solutions.comparisonEnlarge')"
        />
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
import { productImages, solutionPillarImages, needsRecolor } from '@/data/images'

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

.solutions__use-cases {
  background: white;
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
  border-radius: var(--radius-lg);
  background: white;
  border: 1px solid var(--color-border-light);
  box-shadow: var(--shadow-md);
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
