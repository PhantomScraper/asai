<template>
  <div class="projects">
    <HeroSection
      :title="t('projects.heroTitle')"
      :subtitle="t('projects.heroSubtitle')"
      :cta-text="t('projects.ctaRtls')"
      :cta-link="docsLink('leaps-rtls')"
      :showcase-primary="productImages.rtlsUseCases"
      :showcase-secondary="productImages.solutionsIsometric"
      showcase-primary-alt="RTLS use cases across industries"
      showcase-secondary-alt="LEAPS RTLS tracking illustration"
    />
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('projects.appsLabel') }}</span>
          <h2 class="section-title">{{ t('projects.appsTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('projects.appsSubtitle') }}</p>
        </div>
        <div class="grid-3">
          <VisualCard
            v-for="(app, i) in tm('projects.applications')"
            :key="app.title"
            :image="applicationImages[i]"
            :title="app.title"
            :description="app.description"
            :link-text="t('common.readMore')"
            to="/solutions"
          />
        </div>
      </div>
    </section>
    <section class="section projects__architecture">
      <div class="container projects__arch-grid">
        <div>
          <span class="section-label">{{ t('projects.archLabel') }}</span>
          <h2 class="section-title">{{ t('projects.archTitle') }}</h2>
          <p class="projects__arch-text">{{ t('projects.archText') }}</p>
          <NuxtLink :to="docsLink('leaps-rtls')" class="btn btn-outline">{{ t('projects.readRtls') }}</NuxtLink>
        </div>
        <img :src="productImages.rtlsArchitecture" alt="" class="projects__arch-image" loading="lazy" />
      </div>
    </section>
    <section class="section projects__topics">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('projects.topicsLabel') }}</span>
          <h2 class="section-title">{{ t('projects.topicsTitle') }}</h2>
        </div>
        <div class="projects__topic-grid">
          <article v-for="(topic, i) in tm('projects.topics')" :key="topic.title" class="card projects__topic-card">
            <img :src="topicImages[i]" :alt="topic.title" class="projects__topic-image" loading="lazy" />
            <div class="projects__topic-body">
              <h3>{{ topic.title }}</h3>
              <p>{{ topic.description }}</p>
              <NuxtLink :to="docsLink('leaps-solutions')" class="btn-ghost">
                {{ t('common.readMore') }} <span class="arrow">{{ t('common.arrow') }}</span>
              </NuxtLink>
            </div>
          </article>
        </div>
      </div>
    </section>
    <section class="section projects__illustrations">
      <div class="container">
        <ProductShowcase
          :primary-image="productImages.solutionsIsometric"
          primary-alt="LEAPS RTLS tracking across facilities"
          variant="banner"
        />
      </div>
    </section>
    <CtaBanner :title="t('projects.ctaTitle')" :description="t('projects.ctaDesc')" :primary-text="t('common.getInTouch')" primary-link="/about#contact" />
  </div>
</template>

<script setup>
import HeroSection from '@/components/ui/HeroSection.vue'
import CtaBanner from '@/components/ui/CtaBanner.vue'
import VisualCard from '@/components/ui/VisualCard.vue'
import ProductShowcase from '@/components/ui/ProductShowcase.vue'
import { useI18n } from '@/i18n'
import { externalLinks } from '@/data/site'
import { productImages, applicationImages } from '@/data/images'

const { t, tm } = useI18n()
const { docsLink } = useDocs()
const topicImages = ['/images/docs/comparison.png', '/images/docs/safety.png', '/images/docs/compliant.png']
</script>

<style scoped>
.projects__architecture { background: var(--color-bg); }
.projects__arch-grid { display: grid; grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); gap: clamp(2rem, 5vw, 3.5rem); align-items: center; }
.projects__arch-text { color: var(--color-text-muted); line-height: 1.75; margin: 1rem 0 1.75rem; }
.projects__arch-image { width: 100%; border-radius: var(--radius-lg); border: 1px solid var(--color-border-light); box-shadow: var(--shadow-md); background: white; }
.projects__topics { background: white; }
.projects__topic-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
.projects__topic-card { padding: 0; overflow: hidden; display: flex; flex-direction: column; }
.projects__topic-image { width: 100%; height: 200px; object-fit: contain; background: var(--color-bg); padding: 1.5rem; border-bottom: 1px solid var(--color-border-light); }
.projects__topic-body { padding: 1.5rem; display: flex; flex-direction: column; flex: 1; }
.projects__topic-body h3 { font-family: var(--font-display); font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; }
.projects__topic-body p { font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.65; margin-bottom: 1rem; flex: 1; }
.projects__illustrations { background: var(--color-bg); padding-top: 2rem; padding-bottom: 2rem; }
@media (max-width: 1024px) { .projects__topic-grid { grid-template-columns: 1fr; max-width: 480px; margin: 0 auto; } }
@media (max-width: 900px) { .projects__arch-grid { grid-template-columns: 1fr; } }
</style>
