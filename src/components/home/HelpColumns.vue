<template>
  <section class="hcol section">
    <div class="container">
      <div class="section-header">
        <span class="section-label">{{ t('home.help.label') }}</span>
        <h2 class="section-title">{{ t('home.help.title') }}</h2>
      </div>
      <div class="grid-3">
        <article v-for="col in tm('home.help.columns')" :key="col.title" class="card hcol__card">
          <h3>{{ col.title }}</h3>
          <h4>{{ col.forWhomLabel }}</h4>
          <ul>
            <li v-for="(item, i) in col.forWhom" :key="i">{{ item }}</li>
          </ul>
          <h4>{{ col.howLabel }}</h4>
          <p>{{ col.how }}</p>
          <RouterLink :to="col.link" class="btn btn-outline btn-sm hcol__cta">
            {{ col.cta }}
            <span aria-hidden="true">→</span>
          </RouterLink>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from '@/i18n'

const { t, tm } = useI18n()
</script>

<style scoped>
.hcol {
  background: white;
}

.hcol__card {
  display: flex;
  flex-direction: column;
}

.hcol__card h3 {
  font-family: var(--font-display);
  font-size: 1.1875rem;
  font-weight: 600;
  color: var(--color-primary-dark);
  margin-bottom: 1rem;
}

.hcol__card h4 {
  font-family: var(--font-display);
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-text-light);
  margin-bottom: 0.5rem;
}

.hcol__card ul {
  display: grid;
  gap: 0.5rem;
  margin-bottom: 1.25rem;
}

.hcol__card li {
  position: relative;
  padding-left: 1.125rem;
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.6;
}

.hcol__card li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.55em;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-primary);
}

.hcol__card p {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  line-height: 1.6;
  margin-bottom: 1.5rem;
  flex: 1;
}

.hcol__cta {
  align-self: flex-start;
}
</style>
