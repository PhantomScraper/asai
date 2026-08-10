<template>
  <div class="newsletter">
    <div class="newsletter__text">
      <h3>{{ t('footer.stayUpToDate') }}</h3>
      <p>{{ t('footer.newsletterTitle') }}</p>
    </div>
    <form class="newsletter__form" @submit.prevent="handleSubscribe">
      <input v-model="email" type="email" :placeholder="t('footer.emailPlaceholder')" required aria-label="Email" />
      <button type="submit" class="newsletter__submit">{{ t('footer.signUp') }}</button>
    </form>
    <p v-if="subscribed" class="newsletter__success">{{ t('common.subscribeSuccess') }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from '@/i18n'

const { t } = useI18n()
const email = ref('')
const subscribed = ref(false)

const handleSubscribe = () => {
  subscribed.value = true
  email.value = ''
  setTimeout(() => { subscribed.value = false }, 4000)
}
</script>

<style scoped>
.newsletter {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  padding: 1.5rem 2rem;
  background: var(--color-primary);
  border-radius: var(--radius-md);
}

.newsletter__text h3 {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 600;
  color: white;
  margin-bottom: 0.25rem;
}

.newsletter__text p {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.85);
  max-width: 460px;
}

.newsletter__form {
  display: flex;
  gap: 0.75rem;
  flex: 1;
  max-width: 420px;
  min-width: 260px;
}

.newsletter__form input {
  flex: 1;
  padding: 0.625rem 1.125rem;
  border: none;
  border-radius: var(--radius-pill);
  background: white;
  color: var(--color-text);
  font-size: 0.9375rem;
}

.newsletter__submit {
  padding: 0.625rem 1.375rem;
  font-family: var(--font-display);
  font-size: 0.9375rem;
  font-weight: 500;
  color: var(--color-primary-dark);
  background: white;
  border-radius: var(--radius-pill);
  transition: background var(--transition);
  white-space: nowrap;
}

.newsletter__submit:hover {
  background: rgba(255, 255, 255, 0.88);
}

.newsletter__success {
  width: 100%;
  color: white;
  font-size: 0.875rem;
}

@media (max-width: 640px) {
  .newsletter {
    flex-direction: column;
    align-items: flex-start;
    padding: 1.5rem;
  }

  .newsletter__form {
    flex-direction: column;
    width: 100%;
    max-width: 100%;
  }
}
</style>
