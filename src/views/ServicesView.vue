<template>
  <div class="services">
    <HeroSection
      :title="t('services.heroTitle')"
      :subtitle="t('services.heroSubtitle')"
      :cta-text="t('common.contactUs')"
      cta-link="/about#contact"
      :image-src="productImages.rtlsArchitecture"
      image-alt="LEAPS RTLS system architecture"
    />

    <!-- How we help: numbered process cards -->
    <section class="section svc-steps">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('services.introLabel') }}</span>
          <h2 class="section-title">{{ t('services.introTitle') }}</h2>
        </div>
        <div class="grid-3">
          <RouterLink
            v-for="(cat, i) in tm('services.categories')"
            :key="cat.title"
            to="/about#contact"
            class="card svc-step"
          >
            <span class="svc-step__num" aria-hidden="true">{{ String(i + 1).padStart(2, '0') }}</span>
            <h3>{{ cat.title }}</h3>
            <p>{{ cat.description }}</p>
            <span class="svc-step__cta">
              {{ t('common.contactUs') }}
              <span class="arrow-circle" aria-hidden="true">→</span>
            </span>
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- Customization: blue gradient band -->
    <section class="svc-custom">
      <div class="container">
        <div class="svc-custom__header">
          <span class="svc-custom__kicker">{{ t('services.customLabel') }}</span>
          <h2>{{ t('services.customTitle') }}</h2>
          <p>{{ t('services.customSubtitle') }}</p>
        </div>
        <div class="grid-3 svc-custom__grid">
          <div v-for="(service, i) in tm('services.customizations')" :key="service.title" class="svc-custom__item">
            <span class="svc-custom__icon" aria-hidden="true">
              <!-- Software: code brackets -->
              <svg v-if="i === 0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg">
                <path d="M8 6l-6 6 6 6" />
                <path d="M16 6l6 6-6 6" />
                <path d="M13.5 4l-3 16" />
              </svg>
              <!-- Hardware: chip -->
              <svg v-else-if="i === 1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg">
                <rect x="5" y="5" width="14" height="14" rx="2" />
                <rect x="9.5" y="9.5" width="5" height="5" />
                <path d="M9 1.5v3.5M15 1.5v3.5M9 19v3.5M15 19v3.5M19 9h3.5M19 15h3.5M1.5 9H5M1.5 15H5" />
              </svg>
              <!-- Certification: shield with check -->
              <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                <path d="M8.5 12l2.5 2.5 4.5-4.5" />
              </svg>
            </span>
            <h3>{{ service.title }}</h3>
            <p>{{ service.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Gray gradient banner -->
    <section class="svc-banner">
      <div class="svc-banner__bg" aria-hidden="true">
        <svg class="svc-banner__rings" viewBox="0 0 600 600" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="300" cy="300" r="140" stroke="rgba(0,160,223,0.35)" stroke-width="1.5" />
          <circle cx="300" cy="300" r="220" stroke="rgba(0,160,223,0.2)" stroke-width="1.5" />
          <circle cx="300" cy="300" r="295" stroke="rgba(0,160,223,0.1)" stroke-width="1.5" />
        </svg>
      </div>
      <div class="container svc-banner__inner">
        <div class="svc-banner__text">
          <h2>{{ t('services.introTitle') }}</h2>
          <p>{{ t('services.heroSubtitle') }}</p>
          <RouterLink to="/about#contact" class="btn btn-light">{{ t('common.getInTouch') }}</RouterLink>
        </div>
      </div>
    </section>

    <CtaBanner />
  </div>
</template>

<script setup>
import HeroSection from '@/components/ui/HeroSection.vue'
import CtaBanner from '@/components/ui/CtaBanner.vue'
import { useI18n } from '@/i18n'
import { productImages } from '@/data/images'

const { t, tm } = useI18n()
</script>

<style scoped>
/* ---- Numbered process cards ---- */
.svc-steps {
  background: white;
}

.svc-step {
  display: flex;
  flex-direction: column;
  color: var(--color-text);
  transition: box-shadow var(--transition), transform var(--transition);
}

.svc-step:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.svc-step__num {
  display: block;
  font-family: var(--font-display);
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 1;
  color: rgba(0, 160, 223, 0.35);
  margin-bottom: 1rem;
}

.svc-step h3 {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 500;
  color: var(--color-text);
  margin-bottom: 0.75rem;
}

.svc-step p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.65;
  margin-bottom: 1.5rem;
  flex: 1;
}

.svc-step__cta {
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

/* ---- Blue gradient customization band ---- */
.svc-custom {
  background: var(--gradient-blue);
  border-radius: var(--radius-corner-lg) 0 0 0;
  padding: clamp(2.5rem, 5vw, 4rem) 0;
  color: white;
}

.svc-custom__header {
  margin-bottom: 2.5rem;
}

.svc-custom__kicker {
  display: block;
  font-family: var(--font-display);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.75);
  margin-bottom: 0.75rem;
}

.svc-custom__header h2 {
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 2.8vw, 1.875rem);
  font-weight: 400;
  margin-bottom: 0.75rem;
}

.svc-custom__header p {
  font-size: 0.9375rem;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.85);
  max-width: 560px;
}

.svc-custom__icon {
  display: inline-flex;
  color: white;
  margin-bottom: 1rem;
}

.svc-custom__icon svg {
  width: 28px;
  height: 28px;
}

.svc-custom__item h3 {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.svc-custom__item p {
  font-size: 0.875rem;
  line-height: 1.65;
  color: rgba(255, 255, 255, 0.85);
}

/* ---- Gray gradient banner with concentric rings ---- */
.svc-banner {
  position: relative;
  background: var(--gradient-gray);
  color: white;
  overflow: hidden;
}

.svc-banner__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.svc-banner__rings {
  position: absolute;
  top: 50%;
  right: -8%;
  width: min(40vw, 520px);
  height: min(40vw, 520px);
  transform: translateY(-50%);
}

.svc-banner__inner {
  position: relative;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  align-items: center;
  gap: clamp(2rem, 5vw, 4rem);
  padding-top: clamp(2.5rem, 5vw, 3.5rem);
  padding-bottom: clamp(2.5rem, 5vw, 3.5rem);
}

.svc-banner__text h2 {
  font-family: var(--font-display);
  font-size: clamp(1.375rem, 2.5vw, 1.625rem);
  font-weight: 400;
  margin-bottom: 0.75rem;
}

.svc-banner__text p {
  font-size: 0.9375rem;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.8);
  max-width: 460px;
  margin-bottom: 1.5rem;
}

@media (max-width: 900px) {
  .svc-banner__inner {
    grid-template-columns: 1fr;
  }

  .svc-banner__rings {
    right: -30%;
    opacity: 0.5;
  }
}
</style>
