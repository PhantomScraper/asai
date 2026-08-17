<template>
  <div class="projects">
    <HeroSection
      :title="t('projects.heroTitle')"
      :subtitle="t('projects.heroSubtitle')"
      :cta-text="t('common.discoverSolutions')"
      cta-link="/solutions"
      :showcase-primary="productImages.rtlsUseCases"
      showcase-primary-alt="LEAPS RTLS use cases"
    />

    <section class="section projects__intro">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('projects.introLabel') }}</span>
          <h2 class="section-title section-title--lg">{{ t('projects.introTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('projects.introText') }}</p>
        </div>
      </div>
    </section>

    <section class="section projects__stories">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('projects.storiesLabel') }}</span>
          <h2 class="section-title">{{ t('projects.storiesTitle') }}</h2>
        </div>
        <div class="projects__stories-grid">
          <article v-for="(story, i) in tm('projects.stories')" :key="story.name" class="card projects__story">
            <span class="card__label">{{ story.industry }}</span>
            <h3>{{ story.name }}</h3>
            <dl>
              <dt>{{ t('projects.helpLabel') }}</dt>
              <dd>{{ story.help }}</dd>
              <dt>{{ t('projects.sinceLabel') }}</dt>
              <dd>{{ story.since }}</dd>
              <dt>{{ t('projects.scaleLabel') }}</dt>
              <dd>{{ story.scale }}</dd>
            </dl>
            <a
              v-if="successStoryMeta[i]?.link"
              :href="successStoryMeta[i].link"
              target="_blank"
              rel="noopener noreferrer"
              class="btn-ghost projects__story-link"
            >
              {{ t('common.readMore') }}
              <span class="arrow" aria-hidden="true">→</span>
            </a>
          </article>
        </div>
      </div>
    </section>

    <!-- Typical UWB RTLS use cases — detail blocks the Solutions page links into -->
    <section class="section projects__usecases">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('solutions.appsLabel') }}</span>
          <h2 class="section-title">{{ t('solutions.appsTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('solutions.appsSubtitle') }}</p>
        </div>
        <div class="projects__usecase-list">
          <article
            v-for="(example, i) in tm('solutions.appExamples')"
            :key="example.title"
            :id="`uc-${appExampleSlugs[i]}`"
            class="projects__usecase"
            :class="{ 'projects__usecase--flip': i % 2 === 1 }"
          >
            <figure class="projects__usecase-media">
              <img :src="appExampleImages[i]" :alt="example.title" loading="lazy" />
            </figure>
            <div class="projects__usecase-body">
              <h3>{{ example.title }}</h3>
              <ul class="projects__usecase-highlights">
                <li v-for="(hl, j) in example.highlights" :key="j">{{ hl }}</li>
              </ul>
              <h4>{{ example.similarTitle }}</h4>
              <ul class="projects__usecase-similar">
                <li v-for="(sim, j) in example.similar" :key="j">{{ sim }}</li>
              </ul>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="section projects__partners">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('projects.partnersLabel') }}</span>
          <h2 class="section-title">{{ t('projects.partnersTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('projects.partnersText') }}</p>
        </div>
        <div class="grid-3">
          <article v-for="partner in tm('projects.partners')" :key="partner.name" class="card projects__partner">
            <h3>{{ partner.name }}</h3>
            <p>{{ partner.text }}</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section projects__values">
      <div class="container projects__values-grid">
        <div>
          <h2 class="section-title">{{ t('projects.valuesTitle') }}</h2>
          <ul class="projects__values-list">
            <li v-for="(item, i) in tm('home.values.items')" :key="i">
              <span class="projects__check" aria-hidden="true">✓</span>
              <span>{{ item }}</span>
            </li>
          </ul>
        </div>
        <img :src="productImages.solutionsIsometric" alt="" loading="lazy" />
      </div>
    </section>

    <CtaBanner :title="t('projects.ctaTitle')" :description="t('projects.ctaDesc')" />
  </div>
</template>

<script setup>
import HeroSection from '@/components/ui/HeroSection.vue'
import CtaBanner from '@/components/ui/CtaBanner.vue'
import { useI18n } from '@/i18n'
import { successStoryMeta } from '@/data/site'
import { productImages, appExampleImages, appExampleSlugs } from '@/data/images'

const { t, tm } = useI18n()
</script>

<style scoped>
.projects__intro {
  background: white;
  padding-bottom: 0;
}

.projects__intro .section-subtitle {
  max-width: 820px;
}

.projects__stories {
  background: white;
}

.projects__stories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.projects__story {
  display: flex;
  flex-direction: column;
}

.projects__story h3 {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--color-primary-dark);
  margin-bottom: 1rem;
}

.projects__story dl {
  flex: 1;
}

.projects__story dt {
  font-family: var(--font-display);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-text-light);
  margin-bottom: 0.25rem;
}

.projects__story dd {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.65;
  margin-bottom: 0.875rem;
}

.projects__story-link {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  margin-top: 0.5rem;
  font-family: var(--font-display);
  font-size: 0.875rem;
  font-weight: 600;
}

/* Typical use cases — alternating image/text detail rows */
.projects__usecases {
  background: var(--color-bg);
}

.projects__usecase-list {
  display: grid;
  gap: clamp(2.5rem, 5vw, 4rem);
}

.projects__usecase {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
  align-items: center;
  gap: clamp(1.5rem, 4vw, 3rem);
}

.projects__usecase--flip .projects__usecase-media {
  order: 1;
}

.projects__usecase-media {
  margin: 0;
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid var(--color-border-light);
  box-shadow: var(--shadow-md);
  background: white;
}

.projects__usecase-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.projects__usecase-body h3 {
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 2.5vw, 1.5rem);
  font-weight: 600;
  color: var(--color-primary-dark);
  margin-bottom: 1rem;
}

.projects__usecase-body h4 {
  font-family: var(--font-display);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-text-light);
  margin: 1.25rem 0 0.625rem;
}

.projects__usecase-highlights {
  display: grid;
  gap: 0.625rem;
}

.projects__usecase-highlights li {
  position: relative;
  padding-left: 1.375rem;
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.65;
}

.projects__usecase-highlights li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: var(--color-primary);
  font-weight: 700;
}

.projects__usecase-similar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.375rem;
}

.projects__usecase-similar li {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  background: white;
  border: 1px solid var(--color-border-light);
  border-radius: var(--radius-pill);
  padding: 0.25rem 0.75rem;
}

.projects__partners {
  background: white;
}

.projects__partner h3 {
  font-family: var(--font-display);
  font-size: 1.0625rem;
  font-weight: 600;
  margin-bottom: 0.625rem;
}

.projects__partner p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.65;
}

.projects__values {
  background: white;
}

.projects__values-grid {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  align-items: center;
  gap: clamp(2rem, 5vw, 4rem);
}

.projects__values-list {
  display: grid;
  gap: 0.875rem;
  margin-top: 1.25rem;
}

.projects__values-list li {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.65;
}

.projects__check {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  background: var(--color-primary);
  color: white;
  border-radius: 50%;
  font-size: 0.6875rem;
  font-weight: 700;
  margin-top: 2px;
}

.projects__values-grid img {
  width: 100%;
  -webkit-mask-image: linear-gradient(270deg, black 65%, transparent 100%);
  mask-image: linear-gradient(270deg, black 65%, transparent 100%);
}

@media (max-width: 900px) {
  .projects__values-grid {
    grid-template-columns: 1fr;
  }

  .projects__usecase {
    grid-template-columns: 1fr;
  }

  .projects__usecase--flip .projects__usecase-media {
    order: -1;
  }

  .projects__values-grid img {
    -webkit-mask-image: none;
    mask-image: none;
    max-height: 280px;
    object-fit: contain;
  }
}
</style>
