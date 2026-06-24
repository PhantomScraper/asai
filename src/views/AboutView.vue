<template>
  <div class="about">
    <HeroSection
      :title="t('about.heroTitle')"
      :subtitle="t('about.intro')"
      :image-src="productImages.aboutMark"
      image-alt="LEAPS"
      :image-frame="true"
      :show-visual="true"
    />

    <section class="section about__company">
      <div class="container about__company-inner">
        <img :src="productImages.aboutMark" alt="LEAPS" class="about__mark" loading="lazy" />
        <h2 class="about__company-name">{{ t('about.companyName') }}</h2>
        <p class="about__company-text">{{ t('about.intro') }}</p>
      </div>
    </section>

    <section class="section about__values">
      <div class="container">
        <div class="about__values-grid">
          <article v-for="value in tm('about.values')" :key="value.title" class="card about__value-card">
            <img :src="value.icon" :alt="value.title" class="about__value-icon" loading="lazy" />
            <h3>{{ value.title }}</h3>
            <p>{{ value.description }}</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section about__team">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('about.teamLabel') }}</span>
          <h2 class="section-title">{{ t('about.teamTitle') }}</h2>
        </div>
        <div class="about__team-grid">
          <article v-for="member in team" :key="member.name" class="card about__member">
            <img :src="member.photo" :alt="member.name" class="about__member-photo" loading="lazy" />
            <h3>{{ member.displayName || member.name }}</h3>
            <p class="about__member-role">{{ member.role }}</p>
            <a
              v-if="member.linkedin"
              :href="member.linkedin"
              target="_blank"
              rel="noopener noreferrer"
              class="about__member-link"
              :aria-label="`${t('about.linkedinLabel')} — ${member.name}`"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 114.127 0 2.063 2.063 0 01-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" />
              </svg>
              LinkedIn
            </a>
          </article>
        </div>
      </div>
    </section>

    <section class="section about__milestones">
      <div class="container">
        <div class="section-header">
          <span class="section-label">{{ t('about.milestonesLabel') }}</span>
          <h2 class="section-title">{{ t('about.milestonesTitle') }}</h2>
        </div>
        <ol class="about__timeline">
          <li v-for="item in tm('about.milestones')" :key="item.year" class="about__timeline-item">
            <span class="about__timeline-year">{{ item.year }}</span>
            <p>{{ item.text }}</p>
          </li>
        </ol>
      </div>
    </section>

    <section id="contact" class="section about__contact">
      <div class="container about__contact-grid">
        <form class="about__form card" @submit.prevent="handleSubmit">
          <span class="section-label">{{ t('about.contactLabel') }}</span>
          <h2 class="about__form-title">{{ t('about.formTitle') }}</h2>
          <p class="about__form-desc">{{ t('about.formDesc') }}</p>
          <div class="about__form-row">
            <input v-model="form.name" type="text" :placeholder="t('about.formName')" required autocomplete="name" />
            <input v-model="form.company" type="text" :placeholder="t('about.formCompany')" autocomplete="organization" />
          </div>
          <input v-model="form.email" type="email" :placeholder="t('about.formEmail')" required autocomplete="email" />
          <textarea v-model="form.message" :placeholder="t('about.formMessage')" rows="5" required></textarea>
          <button type="submit" class="btn btn-primary">{{ t('common.submit') }}</button>
          <p v-if="submitted" class="about__success">{{ t('common.contactSuccess') }}</p>
        </form>

        <div class="about__contact-info card">
          <h2 class="about__contact-title">{{ t('about.contactTitle') }}</h2>
          <address class="about__contact-details">
            <p><strong>{{ contact.company }}</strong></p>
            <p v-for="(line, i) in contact.addressLines" :key="i">{{ line }}</p>
            <p>{{ t('about.phoneLabel') }}: <a :href="`tel:${contact.phone.replace(/\s/g, '')}`">{{ contact.phone }}</a></p>
            <p>{{ t('about.emailLabel') }}: <a :href="`mailto:${contact.email}`">{{ contact.email }}</a></p>
            <p>{{ t('about.vat') }}: {{ contact.vat }}</p>
          </address>
        </div>
      </div>
    </section>

    <CtaBanner primary-link="/about#contact" />
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import HeroSection from '@/components/ui/HeroSection.vue'
import CtaBanner from '@/components/ui/CtaBanner.vue'
import { useI18n } from '@/i18n'
import { team, contact } from '@/data/site'
import { productImages } from '@/data/images'

const { t, tm } = useI18n()
const form = reactive({ name: '', company: '', email: '', message: '' })
const submitted = ref(false)

const handleSubmit = () => {
  submitted.value = true
  Object.assign(form, { name: '', company: '', email: '', message: '' })
  setTimeout(() => { submitted.value = false }, 4000)
}
</script>

<style scoped>
.about__company {
  background: white;
  padding-top: 2rem;
}

.about__company-inner {
  max-width: 760px;
  margin: 0 auto;
  text-align: center;
}

.about__mark {
  width: 120px;
  height: 120px;
  margin: 0 auto 1.25rem;
  object-fit: contain;
}

.about__company-name {
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 4vw, 2.25rem);
  font-weight: 700;
  letter-spacing: 0.04em;
  margin-bottom: 1.25rem;
}

.about__company-text {
  color: var(--color-text-muted);
  line-height: 1.8;
  font-size: 1.0625rem;
}

.about__values {
  background: var(--color-bg);
}

.about__values-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: clamp(1.25rem, 3vw, 2rem);
}

.about__value-card {
  text-align: center;
  padding: clamp(1.75rem, 4vw, 2.5rem);
}

.about__value-icon {
  width: 96px;
  height: 96px;
  margin: 0 auto 1.25rem;
  object-fit: contain;
}

.about__value-card h3 {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--color-text);
  margin-bottom: 1rem;
}

.about__value-card p {
  font-size: 0.9375rem;
  color: var(--color-text-muted);
  line-height: 1.7;
}

.about__team {
  background: white;
}

.about__team-grid {
  display: flex;
  justify-content: center;
  gap: clamp(1.5rem, 4vw, 2.5rem);
  flex-wrap: wrap;
}

.about__member {
  text-align: center;
  width: min(100%, 280px);
  padding: 1.75rem;
}

.about__member-photo {
  width: 168px;
  height: 168px;
  object-fit: cover;
  border-radius: 50%;
  margin: 0 auto 1.25rem;
  border: 3px solid var(--color-border-light);
}

.about__member h3 {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  margin-bottom: 0.25rem;
}

.about__member-role {
  color: var(--color-text-muted);
  font-size: 0.875rem;
  margin-bottom: 1rem;
}

.about__member-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--color-primary);
}

.about__member-link:hover {
  text-decoration: underline;
}

.about__milestones {
  background: var(--color-bg);
}

.about__timeline {
  max-width: 720px;
  margin: 0 auto;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.about__timeline-item {
  display: grid;
  grid-template-columns: 5.5rem 1fr;
  gap: 1.25rem;
  padding: 1.25rem 0;
  border-bottom: 1px solid var(--color-border-light);
}

.about__timeline-item:last-child {
  border-bottom: 0;
}

.about__timeline-year {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 700;
  color: var(--color-primary);
}

.about__timeline-item p {
  color: var(--color-text-muted);
  line-height: 1.7;
  font-size: 0.9375rem;
}

.about__contact {
  background: white;
}

.about__contact-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr);
  gap: clamp(1.5rem, 4vw, 2.5rem);
  align-items: start;
}

.about__form-title,
.about__contact-title {
  font-family: var(--font-display);
  font-size: clamp(1.375rem, 3vw, 1.75rem);
  font-weight: 700;
  margin: 0.5rem 0 0.75rem;
}

.about__form-desc {
  color: var(--color-text-muted);
  line-height: 1.65;
  margin-bottom: 1.25rem;
}

.about__form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: clamp(1.5rem, 3vw, 2rem);
}

.about__contact-info {
  padding: clamp(1.5rem, 3vw, 2rem);
}

.about__form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.about__form input,
.about__form textarea {
  width: 100%;
  padding: 0.875rem 1rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-family: inherit;
  font-size: 0.9375rem;
}

.about__contact-details {
  font-style: normal;
}

.about__contact-details p {
  margin-bottom: 0.5rem;
  color: var(--color-text-muted);
  line-height: 1.6;
}

.about__contact-details a {
  color: var(--color-primary);
}

.about__success {
  color: #059669;
  font-size: 0.875rem;
}

@media (max-width: 900px) {
  .about__values-grid,
  .about__contact-grid {
    grid-template-columns: 1fr;
  }

  .about__form-row {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 560px) {
  .about__timeline-item {
    grid-template-columns: 1fr;
    gap: 0.375rem;
  }
}
</style>
