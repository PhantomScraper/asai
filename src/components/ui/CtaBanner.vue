<template>
  <section class="cta-banner">
    <div class="container">
      <div class="cta-banner__inner">
        <div class="cta-banner__text">
          <h2>{{ title || t('cta.title') }}</h2>
          <p>{{ description || t('cta.description') }}</p>
        </div>
        <div class="cta-banner__actions">
          <RouterLink v-if="primaryLink && !primaryExternal" :to="primaryLink" class="btn btn-primary">
            {{ primaryText || t('common.contactUs') }}
          </RouterLink>
          <a v-else-if="primaryLink && primaryExternal" :href="primaryLink" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
            {{ primaryText || t('common.contactUs') }}
          </a>
          <RouterLink v-if="secondaryLink && !secondaryExternal" :to="secondaryLink" class="btn btn-outline cta-banner__secondary">
            {{ secondaryText || t('cta.faq') }}
          </RouterLink>
          <a v-else-if="secondaryLink && secondaryExternal" :href="secondaryLink" target="_blank" rel="noopener noreferrer" class="btn btn-outline cta-banner__secondary">
            {{ secondaryText || t('cta.faq') }}
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'

defineProps({
  title: { type: String, default: '' },
  description: { type: String, default: '' },
  primaryText: { type: String, default: '' },
  primaryLink: { type: String, default: '/about#contact' },
  primaryExternal: { type: Boolean, default: false },
  secondaryText: { type: String, default: '' },
  secondaryLink: { type: String, default: '/support' },
  secondaryExternal: { type: Boolean, default: false },
})

const { t } = useI18n()
</script>

<style scoped>
.cta-banner { padding: clamp(2.5rem, 6vw, 4rem) 0; }
.cta-banner__inner { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1.5rem; padding: clamp(1.75rem, 4vw, 3rem); background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%); border-radius: var(--radius-xl); box-shadow: var(--shadow-glow); }
.cta-banner__text h2 { font-family: var(--font-display); font-size: clamp(1.375rem, 3vw, 1.75rem); font-weight: 700; color: white; margin-bottom: 0.5rem; }
.cta-banner__text p { color: rgba(255, 255, 255, 0.85); max-width: 480px; line-height: 1.6; }
.cta-banner__actions { display: flex; gap: 0.75rem; flex-wrap: wrap; }
.cta-banner__inner .btn-primary { background: white; color: var(--color-primary); box-shadow: none; }
.cta-banner__inner .btn-primary:hover { background: rgba(255, 255, 255, 0.9); }
.cta-banner__secondary { border-color: white; color: white; }
.cta-banner__secondary:hover { background: white; color: var(--color-primary); }
@media (max-width: 640px) { .cta-banner__actions { width: 100%; } .cta-banner__actions .btn { flex: 1; min-width: 140px; } }
</style>
