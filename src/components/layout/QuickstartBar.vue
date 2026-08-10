<template>
  <div v-if="!isDocs" class="qbar" role="navigation" aria-label="Quick links">
    <a :href="externalLinks.udkStart" target="_blank" rel="noopener noreferrer" class="qbar__lead">
      <span class="qbar__lead-title">{{ t('quickstart.quickstart') }}</span>
      <span class="qbar__lead-sub">{{ t('quickstart.quickstartSub') }}</span>
    </a>
    <span class="qbar__sep" aria-hidden="true"></span>
    <NuxtLink :to="docsLink()" class="qbar__item">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V4H6.5A2.5 2.5 0 0 0 4 6.5v13z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></svg>
      {{ t('quickstart.docs') }}
    </NuxtLink>
    <a :href="externalLinks.store" target="_blank" rel="noopener noreferrer" class="qbar__item">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="9" cy="21" r="1.5"/><circle cx="19" cy="21" r="1.5"/><path d="M2 3h3l2.6 12.5a1 1 0 0 0 1 .8h9.7a1 1 0 0 0 1-.8L21 7H6"/></svg>
      {{ t('quickstart.store') }}
    </a>
    <a :href="externalLinks.forum" target="_blank" rel="noopener noreferrer" class="qbar__item">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
      {{ t('quickstart.forum') }}
    </a>
    <RouterLink to="/support" class="qbar__item">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="M4.9 4.9l4.2 4.2M14.9 14.9l4.2 4.2M14.9 9.1l4.2-4.2M4.9 19.1l4.2-4.2"/></svg>
      {{ t('quickstart.support') }}
    </RouterLink>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from '@/i18n'
import { externalLinks } from '@/data/site'

const route = useRoute()
const { t } = useI18n()
const { docsLink } = useDocs()

const isDocs = computed(() => route.path.startsWith('/docs'))
</script>

<style scoped>
.qbar {
  position: fixed;
  bottom: 1rem;
  left: 50%;
  transform: translateX(-50%);
  z-index: 900;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: 0.625rem 1.5rem;
  background: white;
  border: 1px solid var(--color-border-light);
  border-radius: var(--radius-pill);
  box-shadow: var(--shadow-lg);
  white-space: nowrap;
}

.qbar__lead {
  display: flex;
  flex-direction: column;
}

.qbar__lead-title {
  font-family: var(--font-display);
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--color-text);
}

.qbar__lead-sub {
  font-size: 0.6875rem;
  color: var(--color-text-muted);
}

.qbar__sep {
  width: 1px;
  height: 28px;
  background: var(--color-border);
}

.qbar__item {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-display);
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--color-text);
  transition: color var(--transition);
}

.qbar__item:hover {
  color: var(--color-primary-dark);
}

.qbar__item svg {
  width: 18px;
  height: 18px;
  color: var(--color-primary-dark);
}

@media (max-width: 767px) {
  .qbar {
    display: none;
  }
}
</style>
