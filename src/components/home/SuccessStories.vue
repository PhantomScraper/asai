<template>
  <section class="stories section">
    <div class="container">
      <div class="stories__header">
        <div>
          <h2 class="section-title">{{ t('home.stories.title') }}</h2>
          <p class="stories__subtitle">{{ t('home.stories.subtitle') }}</p>
        </div>
        <RouterLink to="/our-projects" class="btn btn-primary stories__cta">{{ t('home.stories.cta') }}</RouterLink>
      </div>
      <div class="grid-3">
        <RouterLink
          v-for="(app, i) in tm('projects.applications')"
          :key="app.title"
          to="/our-projects"
          class="stories__card"
        >
          <span class="stories__media">
            <img :src="applicationImages[i]" :class="{ 'recolor-mono-blue': !isPhoto(applicationImages[i]) }" alt="" loading="lazy" />
          </span>
          <span class="stories__body">
            <span class="stories__title-row">
              <h3>{{ app.title }}</h3>
              <span class="arrow-circle" aria-hidden="true">→</span>
            </span>
            <p>{{ app.description }}</p>
          </span>
        </RouterLink>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'
import { applicationImages, isPhoto } from '@/data/images'

const { t, tm } = useI18n()
</script>

<style scoped>
.stories {
  background: white;
}

.stories__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1.5rem;
  flex-wrap: wrap;
  margin-bottom: 2rem;
}

.stories__subtitle {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.7;
  max-width: 560px;
}

.stories__cta {
  flex-shrink: 0;
}

.stories__card {
  display: flex;
  flex-direction: column;
  background: white;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  overflow: hidden;
  transition: box-shadow var(--transition), transform var(--transition);
}

.stories__card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.stories__media {
  display: block;
  aspect-ratio: 16 / 9;
  background: var(--color-bg);
  overflow: hidden;
}

.stories__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  /* The crawled application images carry banner text along their top edge — keep the illustration side */
  object-position: center bottom;
}

.stories__body {
  display: flex;
  flex-direction: column;
  padding: 1.25rem;
}

.stories__title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
}

.stories__card h3 {
  font-family: var(--font-display);
  font-size: 1.0625rem;
  font-weight: 500;
  color: var(--color-text);
}

.stories__card p {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.6;
}
</style>
