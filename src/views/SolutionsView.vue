<template>
  <div class="solutions">
    <HeroSection
      :title="t('solutions.heroTitle')"
      :subtitle="t('solutions.heroSubtitle')"
      :cta-text="t('common.contactUs')"
      cta-link="/about#contact"
      :showcase-primary="productImages.solutionsIsometric"
      :showcase-secondary="productImages.rtlsIllustrations"
      showcase-primary-alt="LEAPS RTLS isometric solution overview"
      showcase-secondary-alt="LEAPS UWB module and tracking network"
    />
    <section class="section">
      <div class="container">
        <div class="solutions__pillars grid-3">
          <article v-for="(pillar, i) in tm('solutions.pillars')" :key="pillar.title" class="card solutions__pillar">
            <div class="solutions__pillar-visual">
              <img :src="pillarImages[i]" :alt="pillar.title" loading="lazy" />
            </div>
            <div class="solutions__pillar-body">
              <span class="solutions__pillar-label">{{ pillar.label }}</span>
              <h3>{{ pillar.title }}</h3>
              <p>{{ pillar.description }}</p>
              <RouterLink v-if="i === 0" to="/about#contact" class="btn-ghost solutions__pillar-link">{{ pillar.linkText }} <span class="arrow">{{ t('common.arrow') }}</span></RouterLink>
              <a v-else :href="i === 1 ? '#uniqueness' : '#technology'" class="btn-ghost solutions__pillar-link">{{ pillar.linkText }} <span class="arrow">{{ t('common.arrow') }}</span></a>
            </div>
          </article>
        </div>
      </div>
    </section>
    <section class="section solutions__use-cases">
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
    <section id="uniqueness" class="section solutions__uniqueness">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('solutions.uniqueLabel') }}</span>
          <h2 class="section-title">{{ t('solutions.uniqueTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('solutions.uniqueSubtitle') }}</p>
        </div>
        <div class="solutions__features-grid">
          <article v-for="item in tm('solutions.uniquenessFeatures')" :key="item.title" class="card solutions__feature">
            <h4>{{ item.title }}</h4>
            <p>{{ item.description }}</p>
          </article>
        </div>
      </div>
    </section>
    <section class="section solutions__stack">
      <div class="container solutions__stack-grid">
        <div>
          <span class="section-label">{{ t('solutions.stackLabel') }}</span>
          <h2 class="section-title">{{ t('solutions.stackTitle') }}</h2>
          <p class="solutions__stack-text">{{ t('solutions.stackSubtitle') }}</p>
          <NuxtLink :to="docsLink('leaps-rtls')" class="btn btn-outline">{{ t('common.learnMore') }}</NuxtLink>
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
import { productImages, solutionPillarImages } from '@/data/images'

const { t, tm } = useI18n()
const { docsLink } = useDocs()
const pillarImages = solutionPillarImages
</script>

<style scoped>
.solutions__pillars {
  align-items: stretch;
}

.solutions__pillar {
  display: flex;
  flex-direction: column;
  height: 100%;
  padding: 0;
  overflow: hidden;
}

.solutions__pillar-visual {
  flex-shrink: 0;
  aspect-ratio: 16 / 9;
  background: linear-gradient(180deg, #f4f6fa 0%, #eef2f8 100%);
  border-bottom: 1px solid var(--color-border-light);
  padding: 0.75rem;
}

.solutions__pillar-visual img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.solutions__pillar-body {
  display: flex;
  flex-direction: column;
  flex: 1;
  padding: 1.25rem 1.5rem 1.5rem;
}

.solutions__pillar-label {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--color-primary);
  margin-bottom: 0.75rem;
}

.solutions__pillar h3 {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
}

.solutions__pillar p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.65;
  flex: 1;
  margin-bottom: 1.25rem;
}

.solutions__pillar-link {
  margin-top: auto;
}
.solutions__use-cases { background: var(--color-bg); }
.solutions__uniqueness { background: white; }
.solutions__features-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1rem; }
.solutions__feature h4 { font-family: var(--font-display); font-size: 1rem; font-weight: 600; color: var(--color-primary); margin-bottom: 0.5rem; }
.solutions__feature p { font-size: 0.875rem; color: var(--color-text-muted); line-height: 1.6; }
.solutions__stack { background: var(--color-bg); }
.solutions__stack-grid { display: grid; grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr); gap: clamp(2rem, 5vw, 3.5rem); align-items: center; }
.solutions__stack-text { color: var(--color-text-muted); line-height: 1.75; margin: 1.25rem 0 1.75rem; }
.solutions__stack-image { width: 100%; border-radius: var(--radius-lg); background: white; border: 1px solid var(--color-border-light); box-shadow: var(--shadow-md); }
@media (max-width: 900px) {
  .solutions__stack-grid { grid-template-columns: 1fr; }
}
.solutions__technology { background: var(--color-bg); }
.solutions__tech-intro {
  max-width: 720px;
  margin-bottom: clamp(2rem, 4vw, 3rem);
}
.solutions__tech-text { color: var(--color-text-muted); line-height: 1.75; margin: 1.25rem 0 1.75rem; }
</style>
