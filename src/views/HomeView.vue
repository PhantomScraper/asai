<template>
  <div class="home">
    <HeroSection
      :title="tm('home.heroTitle')"
      :subtitle="tm('home.heroSubtitle')"
      :cta-text="t('common.discoverSolutions')"
      cta-link="/solutions"
      :showcase-primary="productImages.solutionsIsometric"
      :showcase-secondary="productImages.udkBanner"
      showcase-primary-alt="LEAPS RTLS tracking across industrial facilities"
      showcase-secondary-alt="UDK Ultra-Wideband development kit"
    />

    <section class="section home__portfolio">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('home.portfolioLabel') }}</span>
          <h2 class="section-title">{{ t('home.portfolioTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('home.portfolioSubtitle') }}</p>
        </div>
        <div class="home__portfolio-grid">
          <VisualCard
            v-for="card in portfolioCards"
            :key="card.id"
            :image="card.image"
            :title="t(card.titleKey)"
            :description="t(card.textKey)"
            :link-text="t(card.ctaKey)"
            :to="card.link"
          />
        </div>
      </div>
    </section>

    <section class="section home__use-cases">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('home.useCasesLabel') }}</span>
          <h2 class="section-title">{{ t('home.useCasesTitle') }}</h2>
        </div>
        <ProductShowcase
          :primary-image="productImages.rtlsUseCases"
          primary-alt="RTLS object tracking, indoor navigation, and geofencing"
          variant="banner"
        />
      </div>
    </section>

    <section class="section home__highlights">
      <div class="container">
        <div class="home__intro">
          <span class="section-label">{{ t('home.whyLabel') }}</span>
          <h2 class="section-title">{{ t('home.whyTitle') }}</h2>
          <p class="section-subtitle">{{ t('home.whySubtitle') }}</p>
          <div class="home__intro-actions">
            <RouterLink to="/our-products" class="btn btn-primary">{{ t('common.tryLeaps') }}</RouterLink>
            <RouterLink to="/solutions" class="btn btn-outline">{{ t('common.learnMore') }}</RouterLink>
          </div>
        </div>
        <ul class="home__checklist">
          <li v-for="(item, i) in tm('home.checklist')" :key="i" class="home__check-item">
            <span class="home__check-icon" aria-hidden="true">✓</span>
            <span>{{ item }}</span>
          </li>
        </ul>
      </div>
    </section>

    <section class="section home__docs">
      <div class="container">
        <div class="home__docs-grid">
          <div class="home__docs-text">
            <span class="section-label">{{ t('home.docsLabel') }}</span>
            <h2 class="section-title">{{ t('home.docsTitle') }}</h2>
            <p class="section-subtitle">{{ t('home.docsSubtitle') }}</p>
            <NuxtLink :to="docsLink()" class="btn btn-primary">
              {{ t('home.docsButton') }}
            </NuxtLink>
          </div>
          <img :src="productImages.rtlsStack" alt="" class="home__docs-image" loading="lazy" />
        </div>
      </div>
    </section>

    <section class="section home__features">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('home.featuresLabel') }}</span>
          <h2 class="section-title">{{ t('home.featuresTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('home.featuresSubtitle') }}</p>
        </div>
        <div class="grid-3">
          <article v-for="feature in tm('home.features')" :key="feature.id" class="card home__feature-card">
            <div class="home__feature-icon">
              <FeatureIcon :name="feature.id" />
            </div>
            <h3>{{ feature.title }}</h3>
            <p>{{ feature.description }}</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section home__help">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('home.helpLabel') }}</span>
          <h2 class="section-title">{{ t('home.helpTitle') }}</h2>
        </div>
        <div class="grid-3">
          <article v-for="(card, i) in tm('home.helpCards')" :key="card.title" class="card home__help-card">
            <h3>{{ card.title }}</h3>
            <p>{{ card.description }}</p>
            <RouterLink :to="helpLinks[i]" class="btn-ghost">
              {{ card.linkText }}
              <span class="arrow">{{ t('common.arrow') }}</span>
            </RouterLink>
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
import FeatureIcon from '@/components/ui/FeatureIcon.vue'
import VisualCard from '@/components/ui/VisualCard.vue'
import ProductShowcase from '@/components/ui/ProductShowcase.vue'
import { useI18n } from '@/i18n'
import { externalLinks } from '@/data/site'
import { productImages, portfolioCards } from '@/data/images'

const { t, tm } = useI18n()
const { docsLink } = useDocs()
const helpLinks = ['/our-products', '/our-services', '/support']
</script>

<style scoped>
.home__portfolio { background: white; }
.home__portfolio-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}
.home__use-cases { background: var(--color-bg); }
.home__highlights { background: white; }
.home__intro { max-width: 720px; margin-bottom: 2.5rem; }
.home__intro-actions { display: flex; gap: 1rem; margin-top: 1.75rem; flex-wrap: wrap; }
.home__checklist { display: grid; gap: 1rem; padding: clamp(1.25rem, 3vw, 2rem); background: var(--color-bg); border-radius: var(--radius-lg); border: 1px solid var(--color-border-light); }
.home__check-item { display: flex; align-items: flex-start; gap: 1rem; font-size: 0.975rem; color: var(--color-text-muted); line-height: 1.65; }
.home__check-icon { flex-shrink: 0; display: flex; align-items: center; justify-content: center; width: 24px; height: 24px; background: var(--color-primary); color: white; border-radius: 50%; font-size: 0.75rem; font-weight: 700; margin-top: 2px; }
.home__docs { background: var(--color-bg); }
.home__docs-grid { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(2rem, 5vw, 4rem); align-items: center; }
.home__docs-image { width: 100%; border-radius: var(--radius-lg); box-shadow: var(--shadow-md); border: 1px solid var(--color-border-light); background: white; }
.home__features { background: white; }
.home__feature-card h3 { font-family: var(--font-display); font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; }
.home__feature-card p { font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.65; }
.home__feature-icon { width: 48px; height: 48px; display: flex; align-items: center; justify-content: center; background: rgba(184, 50, 50, 0.08); border-radius: var(--radius-md); color: var(--color-primary); margin-bottom: 1.25rem; }
.home__help { background: var(--color-bg); }
.home__help-card h3 { font-family: var(--font-display); font-size: 1.125rem; font-weight: 700; color: var(--color-primary); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.02em; }
.home__help-card p { font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.65; margin-bottom: 1.5rem; }
@media (max-width: 1100px) { .home__portfolio-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 900px) { .home__docs-grid { grid-template-columns: 1fr; } }
@media (max-width: 640px) { .home__portfolio-grid { grid-template-columns: 1fr; } }
</style>
