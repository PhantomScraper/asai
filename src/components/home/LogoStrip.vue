<template>
  <section class="lstrip">
    <div class="container lstrip__inner">
      <RouterLink to="/our-products" class="lstrip__title">
        {{ t('home.logoStrip.title') }}
        <span aria-hidden="true">→</span>
      </RouterLink>
      <div class="lstrip__logos">
        <a
          v-for="d in distributors"
          :key="d.name"
          :href="d.url"
          target="_blank"
          rel="noopener noreferrer"
          class="lstrip__logo"
          :aria-label="d.name"
        >
          <img :src="d.logo" :alt="d.name" loading="lazy" />
        </a>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'
import { distributors } from '@/data/site'

const { t } = useI18n()
</script>

<style scoped>
.lstrip {
  background: var(--color-gray-dark);
  padding: 2rem 0;
}

.lstrip__inner {
  display: flex;
  align-items: center;
  gap: clamp(1.5rem, 4vw, 3rem);
  flex-wrap: wrap;
}

.lstrip__title {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 500;
  color: white;
  white-space: nowrap;
}

.lstrip__title:hover {
  text-decoration: underline;
}

.lstrip__logos {
  display: flex;
  align-items: center;
  gap: clamp(1.25rem, 3vw, 2.25rem);
  flex-wrap: wrap;
  flex: 1;
  justify-content: flex-end;
}

.lstrip__logo img {
  height: 26px;
  width: auto;
  filter: brightness(0) invert(1);
  opacity: 0.7;
  transition: opacity var(--transition);
}

.lstrip__logo:hover img {
  opacity: 1;
}

@media (max-width: 768px) {
  .lstrip__logos {
    justify-content: flex-start;
  }
}
</style>
