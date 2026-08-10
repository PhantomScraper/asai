<template>
  <div class="projects">
    <HeroSection
      :title="t('projects.heroTitle')"
      :subtitle="t('projects.heroSubtitle')"
      :cta-text="t('projects.ctaRtls')"
      :cta-link="docsLink('leaps-rtls')"
      :showcase-primary="productImages.rtlsIllustrations"
      showcase-primary-alt="LEAPS RTLS tracking across industrial facilities"
    />

    <!-- Applications: Qorvo label-card row -->
    <section class="section projects__apps">
      <div class="container">
        <div class="projects__apps-header">
          <span class="section-label">{{ t('projects.appsLabel') }}</span>
          <h2 class="section-title">{{ t('projects.appsTitle') }}</h2>
          <p class="section-subtitle">{{ t('projects.appsSubtitle') }}</p>
        </div>
        <div class="grid-3">
          <RouterLink
            v-for="(app, i) in tm('projects.applications')"
            :key="app.title"
            to="/solutions"
            class="projects__app-card"
          >
            <span class="projects__app-media">
              <img :src="applicationImages[i]" alt="" class="recolor-mono-blue" loading="lazy" />
            </span>
            <span class="projects__app-body">
              <span class="card__label">{{ t('projects.appsLabel') }}</span>
              <h3>{{ app.title }}</h3>
              <p>{{ app.description }}</p>
              <span class="projects__app-cta">
                {{ t('common.readMore') }}
                <span class="arrow-circle" aria-hidden="true">→</span>
              </span>
            </span>
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- Architecture: Qorvo gray-gradient banner (kept as-is) -->
    <section class="section projects__architecture">
      <div class="container projects__arch-grid">
        <div>
          <span class="section-label">{{ t('projects.archLabel') }}</span>
          <h2 class="section-title">{{ t('projects.archTitle') }}</h2>
          <p class="projects__arch-text">{{ t('projects.archText') }}</p>
          <NuxtLink :to="docsLink('leaps-rtls')" class="btn btn-light">{{ t('projects.readRtls') }}</NuxtLink>
        </div>
        <img :src="productImages.rtlsArchitecture" alt="" class="projects__arch-image" loading="lazy" />
      </div>
    </section>

    <!-- Topics: Qorvo tinted band with asymmetric corner -->
    <section class="section projects__topics">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('projects.topicsLabel') }}</span>
          <h2 class="section-title">{{ t('projects.topicsTitle') }}</h2>
        </div>
        <div class="grid-3">
          <article v-for="(topic, i) in tm('projects.topics')" :key="topic.title" class="card projects__topic-card">
            <img :src="topicImages[i]" :alt="topic.title" class="projects__topic-image recolor-blue" loading="lazy" />
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

    <CtaBanner :title="t('projects.ctaTitle')" :description="t('projects.ctaDesc')" :primary-text="t('common.getInTouch')" primary-link="/about#contact" />
  </div>
</template>

<script setup>
import HeroSection from '@/components/ui/HeroSection.vue'
import CtaBanner from '@/components/ui/CtaBanner.vue'
import { useI18n } from '@/i18n'
import { productImages, applicationImages } from '@/data/images'

const { t, tm } = useI18n()
const { docsLink } = useDocs()
const topicImages = ['/images/docs/comparison.png', '/images/docs/safety.png', '/images/docs/compliant.png']
</script>

<style scoped>
/* Applications: white section, label cards in the ResourceCards/SuccessStories idiom */
.projects__apps {
  background: white;
}

.projects__apps-header {
  margin-bottom: clamp(2rem, 5vw, 3rem);
}

.projects__apps-header .section-subtitle {
  margin-top: 0.25rem;
}

.projects__app-card {
  display: flex;
  flex-direction: column;
  background: white;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  overflow: hidden;
  transition: box-shadow var(--transition), transform var(--transition);
}

.projects__app-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.projects__app-media {
  display: block;
  aspect-ratio: 16 / 9;
  background: var(--color-bg);
  overflow: hidden;
}

.projects__app-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  /* The crawled application images carry banner text along their top edge — keep the illustration side */
  object-position: center bottom;
}

.projects__app-body {
  display: flex;
  flex-direction: column;
  flex: 1;
  padding: 1.25rem;
}

.projects__app-card h3 {
  font-family: var(--font-display);
  font-size: 1.0625rem;
  font-weight: 500;
  line-height: 1.35;
  color: var(--color-text);
  margin-bottom: 0.5rem;
}

.projects__app-card p {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.6;
  margin-bottom: 1.25rem;
}

.projects__app-cta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  margin-top: auto;
  font-family: var(--font-display);
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--color-primary-dark);
}

/* Architecture: Qorvo signature dark gray gradient banner */
.projects__architecture {
  background: var(--gradient-gray);
  color: white;
}

.projects__architecture .section-label {
  color: var(--color-primary-light);
}

.projects__architecture .section-title {
  color: white;
}

.projects__arch-grid {
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
  gap: clamp(2rem, 5vw, 3.5rem);
  align-items: center;
}

.projects__arch-text {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.75;
  margin: 1rem 0 1.75rem;
}

.projects__arch-image {
  width: 100%;
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border-light);
  box-shadow: var(--shadow-md);
  background: white;
}

/* Topics: Qorvo signature tinted band with large asymmetric corner */
.projects__topics {
  background: var(--tint-blue);
  border-radius: 0 0 var(--radius-corner-lg) 0;
}

.projects__topic-card {
  padding: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.projects__topic-image {
  width: 100%;
  height: 180px;
  object-fit: contain;
  background: white;
  padding: 1.25rem;
  border-bottom: 1px solid var(--color-border-light);
}

.projects__topic-body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.projects__topic-body h3 {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 500;
  margin-bottom: 0.75rem;
}

.projects__topic-body p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.65;
  margin-bottom: 1rem;
  flex: 1;
}

@media (max-width: 900px) {
  .projects__arch-grid {
    grid-template-columns: 1fr;
  }
}
</style>
