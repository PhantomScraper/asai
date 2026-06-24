<template>
  <section class="hero">
    <div class="hero__bg">
      <div class="hero__mesh"></div>
      <div class="hero__orb hero__orb--1"></div>
      <div class="hero__orb hero__orb--2"></div>
    </div>

    <div class="container hero__content" :class="{ 'hero__content--centered': !showVisual }">
      <div class="hero__text fade-in">
        <h1 class="hero__title">{{ title }}</h1>
        <p v-if="subtitle" class="hero__subtitle">{{ subtitle }}</p>
        <div v-if="$slots.actions" class="hero__actions">
          <slot name="actions" />
        </div>
        <component
          v-else-if="ctaText"
          :is="ctaExternal ? 'a' : 'RouterLink'"
          v-bind="ctaExternal ? { href: ctaLink, target: '_blank', rel: 'noopener noreferrer' } : { to: ctaLink }"
          class="btn-ghost hero__cta"
        >
          <span class="play-icon">▷</span>
          {{ ctaText }}
          <span class="arrow">→</span>
        </component>
      </div>

      <div v-if="showVisual" class="hero__visual fade-in">
        <ProductShowcase
          v-if="showcasePrimary"
          :primary-image="showcasePrimary"
          :primary-alt="showcasePrimaryAlt || imageAlt"
          :secondary-image="showcaseSecondary"
          :secondary-alt="showcaseSecondaryAlt"
          variant="hero"
        />
        <div v-else-if="imageSrc" class="hero__image-wrap" :class="{ 'hero__image-wrap--framed': imageFrame }">
          <img
            :src="imageSrc"
            :alt="imageAlt"
            class="hero__image"
            loading="eager"
          />
        </div>
        <div v-else class="hero__illustration">
          <div class="hero__device hero__device--main">
            <div class="hero__device-grid"></div>
          </div>
          <div class="hero__pin">
            <svg viewBox="0 0 48 64" fill="none" aria-hidden="true">
              <path d="M24 0C10.745 0 0 10.745 0 24c0 17.25 24 40 24 40s24-22.75 24-40C48 10.745 37.255 0 24 0z" fill="var(--color-primary)"/>
              <circle cx="24" cy="24" r="10" fill="white"/>
            </svg>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import ProductShowcase from '@/components/ui/ProductShowcase.vue'

defineProps({
  title: { type: String, required: true },
  subtitle: { type: String, default: '' },
  ctaText: { type: String, default: '' },
  ctaLink: { type: String, default: '/solutions' },
  ctaExternal: { type: Boolean, default: false },
  showVisual: { type: Boolean, default: true },
  imageSrc: { type: String, default: '' },
  imageAlt: { type: String, default: '' },
  imageFrame: { type: Boolean, default: true },
  showcasePrimary: { type: String, default: '' },
  showcasePrimaryAlt: { type: String, default: '' },
  showcaseSecondary: { type: String, default: '' },
  showcaseSecondaryAlt: { type: String, default: '' },
})
</script>

<style scoped>
.hero {
  position: relative;
  min-height: clamp(520px, 85vh, 760px);
  display: flex;
  align-items: center;
  padding-top: var(--header-height);
  overflow: hidden;
}

.hero__bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #f8f9fc 0%, #eef2f8 50%, #e8edf5 100%);
}

.hero__mesh {
  position: absolute;
  right: -10%;
  top: 10%;
  width: 70%;
  height: 80%;
  background-image:
    radial-gradient(circle at 20% 50%, rgba(26, 79, 216, 0.06) 0%, transparent 50%),
    url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 50 Q25 30 50 50 T100 50' fill='none' stroke='%231a4fd8' stroke-width='0.3' opacity='0.15'/%3E%3C/svg%3E");
  background-size: 80px 80px;
  mask-image: linear-gradient(to left, black 30%, transparent 100%);
  opacity: 0.8;
}

.hero__orb {
  position: absolute;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,0.9) 0%, transparent 70%);
}

.hero__orb--1 { width: 280px; height: 280px; top: 15%; right: 20%; animation: float 8s ease-in-out infinite; }
.hero__orb--2 { width: 180px; height: 180px; bottom: 20%; right: 35%; animation: float 6s ease-in-out infinite 1s; }

.hero__content {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
  gap: clamp(2rem, 5vw, 4rem);
  align-items: center;
  padding-top: clamp(2rem, 5vw, 3rem);
  padding-bottom: clamp(2rem, 5vw, 3rem);
}

.hero__content--centered {
  grid-template-columns: 1fr;
  max-width: 820px;
}

.hero__title {
  font-family: var(--font-display);
  font-size: clamp(1.875rem, 4.5vw, 3.25rem);
  font-weight: 700;
  line-height: 1.12;
  letter-spacing: -0.03em;
  color: var(--color-text);
  margin-bottom: 1.25rem;
}

.hero__subtitle {
  font-size: clamp(1rem, 2vw, 1.125rem);
  color: var(--color-text-muted);
  line-height: 1.75;
  max-width: 560px;
  margin-bottom: 1.75rem;
}

.hero__content--centered .hero__subtitle {
  max-width: none;
}

.hero__cta {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-primary);
}

.play-icon { font-size: 0.875rem; }

.hero__visual {
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero__image-wrap {
  width: 100%;
  max-width: 520px;
}

.hero__image-wrap--framed {
  background: white;
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border-light);
  box-shadow: 0 24px 48px rgba(15, 20, 25, 0.1);
  padding: clamp(0.75rem, 2vw, 1.25rem);
}

.hero__image {
  width: 100%;
  height: auto;
  object-fit: contain;
  filter: drop-shadow(0 20px 40px rgba(15, 20, 25, 0.12));
}

.hero__image-wrap--framed .hero__image {
  filter: none;
}

.hero__illustration {
  position: relative;
  width: 100%;
  max-width: 420px;
  height: 320px;
}

.hero__device {
  position: absolute;
  border: 2px solid var(--color-border);
  border-radius: var(--radius-md);
  background: white;
  box-shadow: var(--shadow-md);
}

.hero__device--main {
  width: 180px;
  height: 120px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 1rem;
}

.hero__device-grid {
  width: 100%;
  height: 100%;
  background-image: radial-gradient(circle, var(--color-primary) 1.5px, transparent 1.5px);
  background-size: 12px 12px;
  opacity: 0.3;
  border-radius: 4px;
}

.hero__pin {
  position: absolute;
  top: 10%;
  right: 20%;
  width: 56px;
  animation: float 4s ease-in-out infinite;
}

@media (max-width: 960px) {
  .hero {
    min-height: auto;
  }

  .hero__content {
    grid-template-columns: 1fr;
    text-align: left;
  }

  .hero__visual {
    order: -1;
  }

  .hero__image-wrap {
    max-width: min(100%, 420px);
    margin: 0 auto;
  }

  .hero__image {
    max-width: 100%;
  }

  .hero__illustration {
    height: 240px;
    max-width: 320px;
    margin: 0 auto;
  }
}

@media (max-width: 480px) {
  .hero__title {
    font-size: 1.75rem;
  }

  .hero__subtitle {
    font-size: 0.975rem;
  }
}
</style>
