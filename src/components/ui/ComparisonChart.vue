<template>
  <figure class="comparison-chart" :class="{ 'comparison-chart--bleed': bleed }">
    <p v-if="title" class="comparison-chart__title">{{ title }}</p>
    <div class="comparison-chart__scroll-wrap">
      <div
        ref="scrollEl"
        class="comparison-chart__scroll"
        :class="{ 'comparison-chart__scroll--start': atStart, 'comparison-chart__scroll--end': atEnd }"
        role="region"
        :aria-label="title || alt"
        tabindex="0"
        @scroll="updateScrollState"
      >
        <button
          type="button"
          class="comparison-chart__zoom"
          :aria-label="enlargeLabel"
          @click="openLightbox"
        >
          <img
            :src="src"
            :alt="alt"
            class="comparison-chart__image"
            loading="lazy"
            @load="updateScrollState"
          />
          <span class="comparison-chart__zoom-badge" aria-hidden="true">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="7" />
              <path d="M21 21l-4.35-4.35M11 8v6M8 11h6" />
            </svg>
            {{ enlargeLabel }}
          </span>
        </button>
      </div>
      <span
        class="comparison-chart__fade comparison-chart__fade--left"
        :class="{ 'comparison-chart__fade--hidden': atStart }"
        aria-hidden="true"
      />
      <span
        class="comparison-chart__fade comparison-chart__fade--right"
        :class="{ 'comparison-chart__fade--hidden': atEnd }"
        aria-hidden="true"
      />
    </div>
    <figcaption class="comparison-chart__hint">{{ hint }}</figcaption>

    <Teleport to="body">
      <div
        v-if="lightboxOpen"
        class="comparison-lightbox"
        role="dialog"
        aria-modal="true"
        :aria-label="title || alt"
        @click.self="closeLightbox"
      >
        <button type="button" class="comparison-lightbox__close" @click="closeLightbox" aria-label="Close">
          ×
        </button>
        <div class="comparison-lightbox__content">
          <img :src="src" :alt="alt" class="comparison-lightbox__image" />
        </div>
      </div>
    </Teleport>
  </figure>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'

defineProps({
  src: { type: String, required: true },
  alt: { type: String, default: 'Technology comparison chart' },
  title: { type: String, default: '' },
  hint: { type: String, default: '' },
  enlargeLabel: { type: String, default: 'View full size' },
  bleed: { type: Boolean, default: true },
})

const lightboxOpen = ref(false)
const scrollEl = ref(null)
const atStart = ref(true)
const atEnd = ref(false)

const openLightbox = () => { lightboxOpen.value = true }
const closeLightbox = () => { lightboxOpen.value = false }

const updateScrollState = () => {
  const el = scrollEl.value
  if (!el) return
  const maxScroll = el.scrollWidth - el.clientWidth
  atStart.value = el.scrollLeft <= 4
  atEnd.value = maxScroll <= 4 || el.scrollLeft >= maxScroll - 4
}

const onKeydown = (e) => {
  if (e.key === 'Escape') closeLightbox()
}

const onResize = () => updateScrollState()

watch(lightboxOpen, (open) => {
  document.body.style.overflow = open ? 'hidden' : ''
})

onMounted(() => {
  window.addEventListener('keydown', onKeydown)
  window.addEventListener('resize', onResize)
  updateScrollState()
})

onUnmounted(() => {
  window.removeEventListener('keydown', onKeydown)
  window.removeEventListener('resize', onResize)
  document.body.style.overflow = ''
})
</script>

<style scoped>
.comparison-chart {
  margin: 0;
  width: 100%;
}

.comparison-chart--bleed {
  width: 100vw;
  max-width: 100vw;
  margin-left: calc(50% - 50vw);
  padding-inline: clamp(1rem, 4vw, 2rem);
}

.comparison-chart__title {
  max-width: var(--container-max);
  margin: 0 auto 1rem;
  padding-inline: clamp(1rem, 4vw, 0);
  font-family: var(--font-display);
  font-size: clamp(1rem, 2vw, 1.125rem);
  font-weight: 600;
  color: var(--color-text);
  text-align: center;
}

.comparison-chart__scroll-wrap {
  position: relative;
}

.comparison-chart__scroll {
  overflow-x: auto;
  overflow-y: hidden;
  -webkit-overflow-scrolling: touch;
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border-light);
  background: white;
  box-shadow: var(--shadow-md);
  scrollbar-width: thin;
}

.comparison-chart__fade {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 2.5rem;
  pointer-events: none;
  z-index: 2;
  transition: opacity var(--transition);
}

.comparison-chart__fade--left {
  left: 0;
  border-radius: var(--radius-lg) 0 0 var(--radius-lg);
  background: linear-gradient(90deg, rgba(255, 255, 255, 0.95) 0%, transparent 100%);
}

.comparison-chart__fade--right {
  right: 0;
  border-radius: 0 var(--radius-lg) var(--radius-lg) 0;
  background: linear-gradient(270deg, rgba(255, 255, 255, 0.95) 0%, transparent 100%);
}

.comparison-chart__fade--hidden {
  opacity: 0;
}

.comparison-chart__scroll:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.comparison-chart__zoom {
  display: block;
  width: 100%;
  min-width: 1040px;
  padding: clamp(0.75rem, 2vw, 1.25rem);
  border: 0;
  background: transparent;
  cursor: zoom-in;
  position: relative;
}

.comparison-chart__image {
  width: 100%;
  min-width: 1000px;
  height: auto;
  display: block;
  border-radius: calc(var(--radius-lg) - 4px);
}

.comparison-chart__zoom-badge {
  position: absolute;
  right: clamp(1rem, 2.5vw, 1.5rem);
  bottom: clamp(1rem, 2.5vw, 1.5rem);
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.875rem;
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--color-text);
  background: rgba(255, 255, 255, 0.95);
  border: 1px solid var(--color-border);
  border-radius: 999px;
  box-shadow: var(--shadow-sm);
  pointer-events: none;
}

.comparison-chart__hint {
  max-width: var(--container-max);
  margin: 0.875rem auto 0;
  padding-inline: clamp(1rem, 4vw, 0);
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  text-align: center;
}

@media (min-width: 1040px) {
  .comparison-chart__zoom,
  .comparison-chart__image {
    min-width: 0;
  }

  .comparison-chart__fade {
    display: none;
  }
}
</style>
