<template>
  <section class="stories section">
    <div class="container">
      <div class="stories__header">
        <div>
          <span class="section-label">{{ t('home.stories.label') }}</span>
          <h2 class="section-title">{{ t('home.stories.title') }}</h2>
          <p class="stories__subtitle">{{ t('home.stories.subtitle') }}</p>
        </div>
        <RouterLink to="/projects" class="btn btn-primary stories__cta">{{ t('home.stories.cta') }}</RouterLink>
      </div>
      <div class="stories__grid">
        <RouterLink
          v-for="story in tm('projects.stories')"
          :key="story.name"
          to="/projects"
          class="stories__card"
        >
          <span class="card__label">{{ story.industry }}</span>
          <span class="stories__title-row">
            <h3>{{ story.name }}</h3>
            <span class="arrow-circle" aria-hidden="true">→</span>
          </span>
          <p>{{ story.help }}</p>
        </RouterLink>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'

const { t, tm } = useI18n()
</script>

<style scoped>
.stories {
  background: white;
}

.stories__header {
  display: flex;
  align-items: flex-end;
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

.stories__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
}

.stories__card {
  display: flex;
  flex-direction: column;
  background: white;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 1.25rem;
  transition: box-shadow var(--transition), transform var(--transition);
}

.stories__card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
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
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
