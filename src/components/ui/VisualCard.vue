<template>
  <component
    :is="to ? 'RouterLink' : 'article'"
    :to="to"
    class="visual-card card"
    :class="{ 'visual-card--link': to }"
  >
    <div class="visual-card__media">
      <img :src="image" :alt="imageAlt || title" loading="lazy" />
    </div>
    <div class="visual-card__body">
      <h3 v-if="title">{{ title }}</h3>
      <p v-if="description">{{ description }}</p>
      <span v-if="linkText" class="visual-card__cta btn-ghost">
        {{ linkText }}
        <span class="arrow">→</span>
      </span>
    </div>
  </component>
</template>

<script setup>
defineProps({
  image: { type: String, required: true },
  imageAlt: { type: String, default: '' },
  title: { type: String, default: '' },
  description: { type: String, default: '' },
  linkText: { type: String, default: '' },
  to: { type: String, default: '' },
})
</script>

<style scoped>
.visual-card {
  padding: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.visual-card--link {
  text-decoration: none;
  color: inherit;
  transition: transform var(--transition), box-shadow var(--transition);
}

.visual-card--link:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.visual-card__media {
  aspect-ratio: 16 / 10;
  background: linear-gradient(180deg, #f4f6fa 0%, #eef2f8 100%);
  border-bottom: 1px solid var(--color-border-light);
  overflow: hidden;
}

.visual-card__media img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center;
  padding: 0.75rem;
}

.visual-card__body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.visual-card__body h3 {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  line-height: 1.35;
}

.visual-card__body p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.65;
  margin-bottom: 1rem;
  flex: 1;
}

.visual-card__cta {
  margin-top: auto;
  font-weight: 600;
  color: var(--color-primary);
}
</style>
