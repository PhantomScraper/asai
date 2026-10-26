<template>
  <div class="support">
    <HeroSection
      :title="t('support.heroTitle')"
      :subtitle="t('support.heroSubtitle')"
      :cta-text="t('support.ctaDocs')"
      :cta-link="externalLinks.docs"
      :cta-external="true"
      :show-visual="false"
    />
    <section class="section support__resources">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">{{ t('support.docsSectionsTitle') }}</h2>
        </div>
        <div class="grid-3">
          <article v-for="(resource, i) in tm('support.resources')" :key="resource.title" class="card support__card">
            <span class="support__icon" aria-hidden="true">
              <!-- Documentation: open book -->
              <svg v-if="i === 0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
              </svg>
              <!-- Quick Start: rocket -->
              <svg v-else-if="i === 1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z" />
                <path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z" />
                <path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0" />
                <path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5" />
              </svg>
              <!-- Community Forum: two chat bubbles -->
              <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 9a2 2 0 0 1-2 2H6l-4 4V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2z" />
                <path d="M18 9h2a2 2 0 0 1 2 2v11l-4-4h-8a2 2 0 0 1-2-2v-1" />
              </svg>
            </span>
            <h3>{{ resource.title }}</h3>
            <p>{{ resource.description }}</p>
            <a :href="resourceLinks[i]" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">{{ resource.linkText }}</a>
          </article>
        </div>
        <div class="support__ask">
          <button type="button" class="btn btn-primary support__ask-btn" @click="openChat">
            <span aria-hidden="true">✦</span>
            {{ t('support.askDocs') }}
          </button>
          <p class="support__ask-hint">{{ t('support.askDocsHint') }}</p>
        </div>
      </div>
    </section>
    <CtaBanner />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import HeroSection from '@/components/ui/HeroSection.vue'
import CtaBanner from '@/components/ui/CtaBanner.vue'
import { useI18n } from '@/i18n'
import { externalLinks } from '@/data/site'

const { t, tm } = useI18n()
// Documentation lives at docs.leapslabs.com — link out rather than to the local mirror.
const resourceLinks = computed(() => [externalLinks.docs, externalLinks.udkStart, externalLinks.forum])

const chatOpen = useState('leaps-chat-open', () => false)
const openChat = () => { chatOpen.value = true }
</script>

<style scoped>
.support__resources {
  background: white;
}

.support__card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.support__icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: var(--tint-brand-soft);
  color: var(--color-primary-dark);
  margin-bottom: 1rem;
}

.support__icon svg {
  width: 32px;
  height: 32px;
}

.support__card h3 {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.support__card p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.65;
  margin-bottom: 1.5rem;
  flex: 1;
}

/* Ask-the-Docs entry right below the resource cards */
.support__ask {
  margin-top: 2.5rem;
  text-align: center;
}

.support__ask-btn span {
  font-size: 0.8125rem;
}

.support__ask-hint {
  margin-top: 0.625rem;
  font-size: 0.875rem;
  color: var(--color-text-muted);
}
</style>
