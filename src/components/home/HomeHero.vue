<template>
  <section class="hhero">
    <div class="hhero__bg" aria-hidden="true">
      <svg class="hhero__rings" viewBox="0 0 600 600" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="300" cy="300" r="120" stroke="rgba(217,71,90,0.4)" stroke-width="1.5" />
        <circle cx="300" cy="300" r="200" stroke="rgba(217,71,90,0.25)" stroke-width="1.5" />
        <circle cx="300" cy="300" r="280" stroke="rgba(217,71,90,0.14)" stroke-width="1.5" />
      </svg>
    </div>

    <transition name="hhero-fade" mode="out-in">
      <div :key="active" class="container hhero__inner">
        <div class="hhero__content">
          <span class="hhero__kicker">{{ slides[active].kicker }}</span>
          <h1 class="hhero__title">{{ slides[active].title }}</h1>
          <p class="hhero__subtitle">{{ slides[active].subtitle }}</p>
          <div class="hhero__actions">
            <RouterLink :to="slides[active].link" class="btn btn-primary">{{ slides[active].cta }}</RouterLink>
            <RouterLink
              v-if="slides[active].secondaryCta"
              :to="slides[active].secondaryLink"
              class="btn btn-light"
            >
              {{ slides[active].secondaryCta }}
            </RouterLink>
          </div>
        </div>
        <div class="hhero__visual">
          <img :src="slideImages[active]" alt="" loading="eager" />
        </div>
      </div>
    </transition>

    <div class="container hhero__tabs" role="tablist" aria-label="Hero slides">
      <button
        v-for="(slide, i) in slides"
        :key="i"
        type="button"
        role="tab"
        class="hhero__tab"
        :class="{ 'hhero__tab--active': i === active }"
        :aria-selected="i === active"
        @click="select(i)"
      >
        {{ slide.kicker }}
        <span class="hhero__tab-track">
          <span v-if="i === active" :key="`bar-${active}-${cycle}`" class="hhero__tab-bar"></span>
        </span>
      </button>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useI18n } from '@/i18n'
import { productImages, hardwareImages } from '@/data/images'

const { tm } = useI18n()

const slides = computed(() => tm('home.hero.slides') || [])
const slideImages = [
  productImages.solutionsIsometric,
  productImages.udkKit,
  hardwareImages.lt3,
]

const INTERVAL = 8000
const active = ref(0)
const cycle = ref(0)
let timer = null

const startTimer = () => {
  if (timer) clearInterval(timer)
  timer = setInterval(() => {
    active.value = (active.value + 1) % slides.value.length
    cycle.value++
  }, INTERVAL)
}

const select = (i) => {
  active.value = i
  cycle.value++
  startTimer()
}

onMounted(startTimer)
onUnmounted(() => { if (timer) clearInterval(timer) })
</script>

<style scoped>
.hhero {
  position: relative;
  background: #000;
  color: white;
  padding-top: var(--header-height);
  overflow: hidden;
}

.hhero__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.hhero__rings {
  position: absolute;
  top: 50%;
  right: -5%;
  width: min(48vw, 640px);
  height: min(48vw, 640px);
  transform: translateY(-50%);
}

.hhero__inner {
  position: relative;
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  align-items: center;
  gap: clamp(2rem, 5vw, 4rem);
  min-height: clamp(400px, 52vh, 520px);
  padding-top: 2.5rem;
  padding-bottom: 2rem;
}

.hhero__kicker {
  display: block;
  font-family: var(--font-display);
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.75);
  margin-bottom: 1rem;
}

.hhero__title {
  font-family: var(--font-display);
  font-size: clamp(1.875rem, 4vw, 2.5rem);
  font-weight: 400;
  line-height: 1.25;
  margin-bottom: 1rem;
}

.hhero__subtitle {
  font-size: 0.9375rem;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.75);
  max-width: 480px;
  margin-bottom: 1.75rem;
}

.hhero__actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.hhero__visual img {
  width: 100%;
  max-height: 360px;
  object-fit: contain;
  border-radius: var(--radius-md);
}

/* Qorvo-style left-to-right dark overlay keeps the text side readable */
.hhero__inner::before {
  content: '';
  position: absolute;
  inset: 0;
  left: -10vw;
  background: var(--gradient-hero);
  pointer-events: none;
}

.hhero__content,
.hhero__visual {
  position: relative;
}

.hhero__tabs {
  position: relative;
  display: flex;
  gap: clamp(1.5rem, 4vw, 3rem);
  padding-bottom: 1.5rem;
}

.hhero__tab {
  flex: 1;
  max-width: 220px;
  text-align: left;
  font-family: var(--font-display);
  font-size: 0.8125rem;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.6);
  padding: 0.5rem 0 0;
  transition: color var(--transition);
}

.hhero__tab--active,
.hhero__tab:hover {
  color: white;
}

.hhero__tab-track {
  display: block;
  height: 2px;
  margin-top: 0.5rem;
  background: rgba(255, 255, 255, 0.25);
  border-radius: 1px;
  overflow: hidden;
}

.hhero__tab-bar {
  display: block;
  height: 100%;
  background: var(--color-primary);
  animation: hhero-progress 8s linear forwards;
}

@keyframes hhero-progress {
  from { width: 0; }
  to { width: 100%; }
}

.hhero-fade-enter-active,
.hhero-fade-leave-active {
  transition: opacity 0.35s ease;
}

.hhero-fade-enter-from,
.hhero-fade-leave-to {
  opacity: 0;
}

@media (max-width: 900px) {
  .hhero__inner {
    grid-template-columns: 1fr;
    min-height: 0;
  }

  .hhero__visual img {
    max-height: 240px;
  }

  .hhero__tab {
    font-size: 0.75rem;
  }
}
</style>
