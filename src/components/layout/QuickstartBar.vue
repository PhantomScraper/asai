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
/* Dark tab docked to the bottom edge — deliberately unlike the floating white pill on qorvo.com. */
.qbar {
  position: fixed;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  z-index: 900;
  display: flex;
  align-items: center;
  gap: 1.75rem;
  padding: 0.5rem 1.75rem 0.5rem 0.5rem;
  background: var(--color-ink);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-bottom: 0;
  border-radius: var(--radius-md) var(--radius-md) 0 0;
  box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.3);
  white-space: nowrap;
}

.qbar__lead {
  display: flex;
  flex-direction: column;
  padding: 0.4rem 0.9rem;
  border-radius: var(--radius-sm);
  background: var(--gradient-brand);
  transition: filter var(--transition);
}

.qbar__lead:hover {
  filter: brightness(1.12);
}

.qbar__lead-title {
  font-family: var(--font-display);
  font-size: 0.875rem;
  font-weight: 700;
  color: white;
}

.qbar__lead-sub {
  font-size: 0.6875rem;
  color: rgba(255, 255, 255, 0.8);
}

.qbar__sep {
  width: 1px;
  height: 28px;
  background: rgba(255, 255, 255, 0.12);
}

.qbar__item {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-display);
  font-size: 0.8125rem;
  font-weight: 600;
  color: rgba(226, 232, 240, 0.85);
  transition: color var(--transition);
}

.qbar__item:hover {
  color: white;
}

.qbar__item svg {
  width: 18px;
  height: 18px;
  color: var(--color-primary-light);
}

@media (max-width: 767px) {
  .qbar {
    display: none;
  }
}
</style>
