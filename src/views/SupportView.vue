<template>
  <div class="support">
    <HeroSection
      :title="t('support.heroTitle')"
      :subtitle="t('support.heroSubtitle')"
      :cta-text="t('support.ctaDocs')"
      :cta-link="docsLink()"
      :show-visual="false"
    />
    <section class="section">
      <div class="container">
        <div class="grid-3">
          <article v-for="(resource, i) in tm('support.resources')" :key="resource.title" class="card support__card">
            <h3>{{ resource.title }}</h3>
            <p>{{ resource.description }}</p>
            <a :href="resourceLinks[i]" target="_blank" rel="noopener noreferrer" class="btn btn-outline">{{ resource.linkText }}</a>
          </article>
        </div>
      </div>
    </section>
    <section class="section support__docs-visual">
      <div class="container">
        <img :src="productImages.supportResources" alt="" class="support__resources-image" loading="lazy" />
      </div>
    </section>
    <section class="section support__docs">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('support.docsSectionsLabel') }}</span>
          <h2 class="section-title">{{ t('support.docsSectionsTitle') }}</h2>
          <p class="section-subtitle section-header__subtitle">{{ t('support.docsSectionsSubtitle') }}</p>
        </div>
        <div class="support__docs-grid">
          <a v-for="(section, i) in tm('support.docSections')" :key="section" :href="docSectionLinks[i]" target="_blank" rel="noopener noreferrer" class="support__docs-link card">
            <span>{{ section }}</span>
            <span class="arrow">{{ t('common.arrow') }}</span>
          </a>
        </div>
      </div>
    </section>
    <section class="section support__mailing">
      <div class="container support__mailing-inner card">
        <div>
          <h2>{{ t('support.mailingTitle') }}</h2>
          <p>{{ t('support.mailingText') }}</p>
        </div>
        <button class="btn btn-primary" @click="showSubscribe = true">{{ t('support.mailingButton') }}</button>
      </div>
    </section>
    <div v-if="showSubscribe" class="support__modal" role="dialog" aria-modal="true">
      <div class="support__modal-content card">
        <button class="support__modal-close" @click="showSubscribe = false" aria-label="Close">×</button>
        <h3>{{ t('support.modalTitle') }}</h3>
        <p>{{ t('support.modalText') }}</p>
        <form @submit.prevent="handleSubscribe">
          <input v-model="email" type="email" :placeholder="t('support.emailPlaceholder')" required />
          <button type="submit" class="btn btn-primary">{{ t('common.subscribe') }}</button>
        </form>
        <p v-if="subscribed" class="support__success">{{ t('common.subscribeSuccess') }}</p>
      </div>
    </div>
    <CtaBanner :secondary-text="t('cta.faqDocs')" secondary-link="https://docs.leapslabs.com/faq/" secondary-external />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import HeroSection from '@/components/ui/HeroSection.vue'
import CtaBanner from '@/components/ui/CtaBanner.vue'
import { useI18n } from '@/i18n'
import { externalLinks } from '@/data/site'
import { productImages } from '@/data/images'

const { t, tm } = useI18n()
const { docsLink } = useDocs()
const resourceLinks = computed(() => [docsLink(), docsLink('udk-start'), externalLinks.forum])
const docSectionLinks = computed(() =>
  ['leaps-solutions', 'udk', 'leaps-rtls', 'pans-pro-rtls', 'hardware', 'faq', 'support'].map((s) =>
    docsLink(s)
  )
)

const showSubscribe = ref(false)
const email = ref('')
const subscribed = ref(false)

const handleSubscribe = () => {
  subscribed.value = true
  email.value = ''
  setTimeout(() => { showSubscribe.value = false; subscribed.value = false }, 2500)
}
</script>

<style scoped>
.support__card { display: flex; flex-direction: column; }
.support__card h3 { font-family: var(--font-display); font-size: 1.25rem; font-weight: 600; margin-bottom: 0.75rem; }
.support__card p { font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.65; margin-bottom: 1.5rem; flex: 1; }
.support__docs-visual { background: white; padding-top: 0; }
.support__resources-image { width: 100%; border-radius: var(--radius-lg); border: 1px solid var(--color-border-light); box-shadow: var(--shadow-sm); }
.support__docs { background: var(--color-bg); }
.support__docs-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem; }
.support__docs-link { display: flex; align-items: center; justify-content: space-between; padding: 1.125rem 1.25rem; font-family: var(--font-display); font-weight: 600; font-size: 0.9375rem; }
.support__mailing { background: white; }
.support__mailing-inner { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1.5rem; padding: clamp(1.5rem, 3vw, 2rem); }
.support__mailing-inner h2 { font-family: var(--font-display); font-size: 1.25rem; margin-bottom: 0.5rem; }
.support__mailing-inner p { color: var(--color-text-muted); max-width: 520px; line-height: 1.6; }
.support__modal { position: fixed; inset: 0; background: rgba(15, 20, 25, 0.5); display: flex; align-items: center; justify-content: center; z-index: 2000; padding: 1rem; }
.support__modal-content { position: relative; max-width: 440px; width: 100%; padding: 2rem; }
.support__modal-close { position: absolute; top: 1rem; right: 1rem; font-size: 1.5rem; color: var(--color-text-muted); }
.support__modal-content form { display: flex; flex-direction: column; gap: 0.75rem; }
.support__modal-content input { padding: 0.875rem 1rem; border: 1px solid var(--color-border); border-radius: var(--radius-md); font-size: 0.9375rem; }
.support__success { color: #059669; margin-top: 1rem; font-size: 0.875rem; }
@media (max-width: 640px) { .support__mailing-inner { flex-direction: column; align-items: flex-start; } }
</style>
