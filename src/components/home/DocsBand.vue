<template>
  <section class="dband section">
    <div class="container">
      <div class="section-header">
        <span class="section-label">{{ t('home.docs.label') }}</span>
        <h2 class="section-title">{{ t('home.docs.title') }}</h2>
        <p class="section-subtitle section-header__subtitle">{{ t('home.docs.subtitle') }}</p>
      </div>
      <div class="dband__actions">
        <a :href="externalLinks.docs" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
          {{ t('home.docs.button') }}
        </a>
        <button type="button" class="btn btn-outline dband__ask" @click="openChat">
          <span aria-hidden="true">✦</span>
          {{ t('home.docs.askDocs') }}
        </button>
      </div>
      <p class="dband__hint">{{ t('home.docs.askDocsHint') }}</p>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'
import { externalLinks } from '@/data/site'

const { t } = useI18n()
const chatOpen = useState('leaps-chat-open', () => false)
const openChat = () => { chatOpen.value = true }
</script>

<style scoped>
.dband {
  background: var(--tint-brand-faint);
}

.dband__actions {
  display: flex;
  justify-content: center;
  gap: 0.875rem;
  flex-wrap: wrap;
}

.dband__ask span {
  color: var(--color-primary);
  font-size: 0.8125rem;
}

.dband__hint {
  margin-top: 1rem;
  text-align: center;
  font-size: 0.875rem;
  color: var(--color-text-muted);
}
</style>
