<template>
  <footer class="footer">
    <div class="container">
      <div class="footer__newsletter">
        <div class="footer__newsletter-text">
          <span class="section-label">{{ t('footer.newsletterLabel') }}</span>
          <h3 class="footer__newsletter-title">{{ t('footer.newsletterTitle') }}</h3>
        </div>
        <form class="footer__form" @submit.prevent="handleSubscribe">
          <input v-model="email" type="email" :placeholder="t('footer.emailPlaceholder')" required aria-label="Email" />
          <button type="submit" class="btn btn-primary">{{ t('common.subscribe') }}</button>
        </form>
        <p v-if="subscribed" class="footer__success">{{ t('common.subscribeSuccess') }}</p>
      </div>

      <div class="footer__grid">
        <div class="footer__brand">
          <img :src="'/logo.png'" alt="LEAPS" width="160" height="60" />
          <p class="footer__tagline">{{ t('footer.tagline') }}</p>
          <div class="footer__social">
            <a v-for="social in socialLinks" :key="social.name" :href="social.url" target="_blank" rel="noopener noreferrer" :aria-label="social.name" class="footer__social-link">
              <SocialIcon :name="social.icon" />
            </a>
          </div>
        </div>
        <div class="footer__links">
          <h4>{{ t('footer.navigation') }}</h4>
          <RouterLink v-for="link in navLinks" :key="link.path" :to="link.path">{{ link.name }}</RouterLink>
        </div>
        <div class="footer__links">
          <h4>{{ t('footer.resources') }}</h4>
          <NuxtLink :to="docsLink()">{{ t('footer.documentation') }}</NuxtLink>
          <NuxtLink :to="docsLink('faq')">{{ t('footer.faq') }}</NuxtLink>
          <a :href="externalLinks.forum" target="_blank" rel="noopener noreferrer">{{ t('footer.forum') }}</a>
          <a :href="externalLinks.store" target="_blank" rel="noopener noreferrer">{{ t('footer.store') }}</a>
        </div>
        <div class="footer__contact">
          <h4>{{ t('footer.contact') }}</h4>
          <p>{{ contact.company }}</p>
          <p v-for="(line, i) in contact.addressLines" :key="i">{{ line }}</p>
          <p><a :href="`tel:${contact.phone.replace(/\s/g, '')}`">{{ contact.phone }}</a></p>
          <p><a :href="`mailto:${contact.email}`">{{ contact.email }}</a></p>
        </div>
      </div>
      <div class="footer__bottom">
        <p>{{ t('footer.copyright') }}</p>
        <RouterLink to="/about">{{ navLinks.find(l => l.path === '/about')?.name }}</RouterLink>
        <a href="#">{{ t('footer.privacy') }}</a>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from '@/i18n'
import { contact, socialLinks, externalLinks } from '@/data/site'
import SocialIcon from '@/components/ui/SocialIcon.vue'

const { t, navLinks } = useI18n()
const { docsLink } = useDocs()
const email = ref('')
const subscribed = ref(false)

const handleSubscribe = () => {
  subscribed.value = true
  email.value = ''
  setTimeout(() => { subscribed.value = false }, 4000)
}
</script>

<style scoped>
.footer { background: var(--color-bg-dark); color: rgba(255, 255, 255, 0.85); padding: 4rem 0 2rem; margin-top: auto; }
.footer__newsletter { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 2rem; padding-bottom: 3rem; margin-bottom: 3rem; border-bottom: 1px solid rgba(255, 255, 255, 0.1); }
.footer__newsletter .section-label { color: var(--color-primary-light); }
.footer__newsletter .section-label::before { background: var(--color-primary-light); }
.footer__newsletter-title { font-family: var(--font-display); font-size: 1.5rem; font-weight: 600; color: white; margin-top: 0.5rem; }
.footer__form { display: flex; gap: 0.75rem; flex: 1; max-width: 480px; }
.footer__form input { flex: 1; padding: 0.875rem 1.25rem; border: 1px solid rgba(255, 255, 255, 0.15); border-radius: var(--radius-md); background: rgba(255, 255, 255, 0.05); color: white; font-size: 0.9375rem; }
.footer__form input::placeholder { color: rgba(255, 255, 255, 0.4); }
.footer__success { width: 100%; color: #6ee7a0; font-size: 0.875rem; }
.footer__grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1.5fr; gap: 3rem; margin-bottom: 3rem; }
.footer__brand img { height: 48px; width: auto; margin-bottom: 0.75rem; filter: brightness(0) invert(1); }
.footer__tagline { font-size: 0.8125rem; color: rgba(255, 255, 255, 0.5); margin-bottom: 1.25rem; }
.footer__social { display: flex; gap: 0.75rem; }
.footer__social-link { display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: var(--radius-sm); background: rgba(255, 255, 255, 0.08); color: rgba(255, 255, 255, 0.7); transition: all var(--transition); }
.footer__social-link:hover { background: var(--color-primary); color: white; }
.footer__links h4, .footer__contact h4 { font-family: var(--font-display); font-size: 0.875rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: white; margin-bottom: 1.25rem; }
.footer__links { display: flex; flex-direction: column; gap: 0.75rem; }
.footer__links a, .footer__contact a { font-size: 0.9375rem; color: rgba(255, 255, 255, 0.65); transition: color var(--transition); }
.footer__links a:hover, .footer__contact a:hover { color: white; }
.footer__contact p { font-size: 0.9375rem; color: rgba(255, 255, 255, 0.65); margin-bottom: 0.5rem; line-height: 1.5; }
.footer__bottom { display: flex; flex-wrap: wrap; align-items: center; gap: 1.5rem; padding-top: 2rem; border-top: 1px solid rgba(255, 255, 255, 0.1); font-size: 0.875rem; color: rgba(255, 255, 255, 0.45); }
.footer__bottom a { color: rgba(255, 255, 255, 0.55); }
@media (max-width: 1024px) { .footer__grid { grid-template-columns: 1fr 1fr; } }
@media (max-width: 640px) { .footer__newsletter { flex-direction: column; align-items: flex-start; } .footer__form { flex-direction: column; max-width: 100%; width: 100%; } .footer__grid { grid-template-columns: 1fr; gap: 2rem; } }
</style>
