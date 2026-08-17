<template>
  <footer class="footer">
    <div class="container">
      <div class="footer__banner">
        <NewsletterBanner />
      </div>

      <div class="footer__grid">
        <div class="footer__brand">
          <img :src="'/logo.png'" alt="LEAPS" width="160" height="60" />
          <p class="footer__tagline">{{ t('footer.tagline') }}</p>
          <p class="footer__description">{{ t('footer.description') }}</p>
          <h4 class="footer__connect">{{ t('footer.stayConnected') }}</h4>
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
          <a :href="externalLinks.docs" target="_blank" rel="noopener noreferrer">{{ t('footer.documentation') }}</a>
          <a :href="`${externalLinks.docs}faq/`" target="_blank" rel="noopener noreferrer">{{ t('footer.faq') }}</a>
          <a :href="externalLinks.forum" target="_blank" rel="noopener noreferrer">{{ t('footer.forum') }}</a>
          <a :href="externalLinks.store" target="_blank" rel="noopener noreferrer">{{ t('footer.store') }}</a>
        </div>
        <div class="footer__links footer__contact">
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
        <a class="footer__phone" :href="`tel:${contact.phone.replace(/\s/g, '')}`">{{ contact.phone }}</a>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { useI18n } from '@/i18n'
import { contact, socialLinks, externalLinks } from '@/data/site'
import SocialIcon from '@/components/ui/SocialIcon.vue'
import NewsletterBanner from '@/components/ui/NewsletterBanner.vue'

const { t, navLinks } = useI18n()
</script>

<style scoped>
.footer { background: var(--color-bg-dark); color: rgba(255, 255, 255, 0.85); padding: 3rem 0 2rem; margin-top: auto; }
.footer__banner { margin-bottom: 3rem; }
.footer__grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1.5fr; gap: 3rem; margin-bottom: 3rem; }
.footer__brand img { height: 48px; width: auto; margin-bottom: 0.75rem; filter: brightness(0) invert(1); }
.footer__tagline { font-size: 0.8125rem; color: rgba(255, 255, 255, 0.5); margin-bottom: 1rem; }
.footer__description { font-size: 0.875rem; color: rgba(255, 255, 255, 0.65); line-height: 1.6; margin-bottom: 1.5rem; max-width: 320px; }
.footer__connect { font-family: var(--font-display); font-size: 0.875rem; font-weight: 600; color: white; margin-bottom: 0.75rem; }
.footer__social { display: flex; gap: 0.75rem; }
.footer__social-link { display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; background: rgba(255, 255, 255, 0.08); color: rgba(255, 255, 255, 0.7); transition: all var(--transition); }
.footer__social-link:hover { background: var(--color-primary); color: white; }
.footer__links h4 { font-family: var(--font-display); font-size: 0.875rem; font-weight: 600; letter-spacing: 0.02em; color: white; padding-top: 0.75rem; border-top: 2px solid rgba(255, 255, 255, 0.25); margin-bottom: 1.25rem; }
.footer__links { display: flex; flex-direction: column; gap: 0.75rem; }
.footer__links a { font-size: 0.9375rem; color: rgba(255, 255, 255, 0.65); transition: color var(--transition); }
.footer__links a:hover { color: white; }
.footer__contact p { font-size: 0.9375rem; color: rgba(255, 255, 255, 0.65); margin-bottom: 0; line-height: 1.5; }
.footer__bottom { display: flex; flex-wrap: wrap; align-items: center; gap: 1.5rem; padding-top: 2rem; border-top: 1px solid rgba(255, 255, 255, 0.1); font-size: 0.875rem; color: rgba(255, 255, 255, 0.45); }
.footer__bottom a { color: rgba(255, 255, 255, 0.55); }
.footer__phone { margin-left: auto; }
@media (max-width: 1024px) { .footer__grid { grid-template-columns: 1fr 1fr; } }
@media (max-width: 640px) { .footer__grid { grid-template-columns: 1fr; gap: 2rem; } .footer__phone { margin-left: 0; } }
</style>
