<template>
  <section class="rcards section">
    <div class="container">
      <div class="rcards__header">
        <h2 class="section-title">{{ t('home.resources.title') }}</h2>
        <div class="rcards__nav">
          <button type="button" class="rcards__nav-btn" aria-label="Previous" @click="scrollByCard(-1)">←</button>
          <button type="button" class="rcards__nav-btn" aria-label="Next" @click="scrollByCard(1)">→</button>
        </div>
      </div>

      <div ref="track" class="rcards__track">
        <NuxtLink :to="docsLink()" class="rcard rcard--gradient">
          <span class="rcard__label rcard__label--light">{{ t('home.resources.docsCard.label') }}</span>
          <h3>{{ t('home.resources.docsCard.title') }}</h3>
          <p>{{ t('home.docsSubtitle') }}</p>
          <span class="rcard__cta">
            {{ t('home.resources.docsCard.cta') }}
            <span class="arrow-circle rcard__arrow--light" aria-hidden="true">→</span>
          </span>
        </NuxtLink>

        <RouterLink
          v-for="(card, i) in portfolioCards"
          :key="card.id"
          :to="card.link"
          class="rcard"
        >
          <span class="rcard__media">
            <img :src="card.image" :class="{ 'recolor-blue': needsRecolor(card.image) }" alt="" loading="lazy" />
          </span>
          <span class="card__label">{{ tm('home.resources.labels')[i] }}</span>
          <h3>{{ t(card.titleKey) }}</h3>
          <p>{{ t(card.textKey) }}</p>
          <span class="rcard__cta">
            {{ t(card.ctaKey) }}
            <span class="arrow-circle" aria-hidden="true">→</span>
          </span>
        </RouterLink>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from '@/i18n'
import { portfolioCards, needsRecolor } from '@/data/images'

const { t, tm } = useI18n()
const { docsLink } = useDocs()

const track = ref(null)

const scrollByCard = (dir) => {
  if (!track.value) return
  const card = track.value.querySelector('.rcard')
  const step = card ? card.getBoundingClientRect().width + 20 : 300
  track.value.scrollBy({ left: dir * step, behavior: 'smooth' })
}
</script>

<style scoped>
.rcards {
  background: white;
}

.rcards__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 2rem;
}

.rcards__nav {
  display: flex;
  gap: 0.5rem;
}

.rcards__nav-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border: 1px solid var(--color-border);
  border-radius: 50%;
  color: var(--color-primary-dark);
  font-size: 1rem;
  transition: all var(--transition);
  background: white;
}

.rcards__nav-btn:hover {
  border-color: var(--color-primary);
  background: var(--tint-blue-faint);
}

.rcards__track {
  display: flex;
  gap: 1.25rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: none;
  padding-bottom: 0.5rem;
}

.rcards__track::-webkit-scrollbar {
  display: none;
}

.rcard {
  flex: 0 0 clamp(260px, 23.5%, 290px);
  scroll-snap-align: start;
  display: flex;
  flex-direction: column;
  background: white;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 1.25rem;
  transition: box-shadow var(--transition), transform var(--transition);
}

.rcard:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.rcard__media {
  display: block;
  aspect-ratio: 16 / 10;
  margin: -1.25rem -1.25rem 1rem;
  border-radius: var(--radius-sm) var(--radius-sm) 0 0;
  overflow: hidden;
  background: var(--color-bg);
}

.rcard__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.rcard h3 {
  font-family: var(--font-display);
  font-size: 1.0625rem;
  font-weight: 500;
  line-height: 1.35;
  color: var(--color-text);
  margin-bottom: 0.5rem;
}

.rcard p {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.6;
  margin-bottom: 1.25rem;
}

.rcard__cta {
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

/* First card: Qorvo's blue-gradient highlight card */
.rcard--gradient {
  background: var(--gradient-blue);
  border: none;
  color: white;
  justify-content: flex-end;
  min-height: 320px;
}

.rcard--gradient h3 {
  color: white;
  font-size: 1.25rem;
}

.rcard--gradient p {
  color: rgba(255, 255, 255, 0.85);
}

.rcard--gradient .rcard__cta {
  color: white;
}

.rcard__label--light {
  display: block;
  font-family: var(--font-display);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.75);
  margin-bottom: 0.5rem;
}

.rcard__arrow--light {
  background: white;
  color: var(--color-primary-dark);
}

@media (max-width: 768px) {
  .rcards__nav {
    display: none;
  }

  .rcard {
    flex-basis: 82%;
  }
}
</style>
