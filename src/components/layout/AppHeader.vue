<template>
  <header class="header" :class="{ 'header--scrolled': isScrolled, 'header--menu-open': menuOpen }">
    <div class="container header__inner">
      <RouterLink to="/" class="header__logo" @click="closeMenu">
        <img :src="'/logo.png'" alt="LEAPS - Low Energy Accurate Positioning System" width="189" height="70" />
      </RouterLink>

      <nav v-if="!isMobile" class="header__nav header__nav--desktop">
        <RouterLink
          v-for="link in navLinks"
          :key="link.path"
          :to="link.path"
          class="header__link"
          :class="{ 'header__link--active': isActive(link.path) }"
        >
          {{ link.name }}
        </RouterLink>
      </nav>

      <div class="header__actions">
        <select
          :value="locale"
          class="header__lang header__lang--desktop"
          aria-label="Language"
          @change="onLocaleChange"
        >
          <option v-for="opt in supportedLocales" :key="opt.code" :value="opt.code">
            {{ opt.label }}
          </option>
        </select>
        <RouterLink to="/about#contact" class="btn btn-primary header__cta" @click="closeMenu">
          {{ t('nav.contactUs') }}
        </RouterLink>
        <button
          class="header__toggle"
          :aria-expanded="menuOpen"
          aria-label="Toggle menu"
          @click="menuOpen = !menuOpen"
        >
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>

    <Teleport to="body">
      <template v-if="isMobile">
        <div
          v-if="menuOpen"
          class="mobile-menu-overlay"
          aria-hidden="true"
          @click="closeMenu"
        />
        <nav
          class="mobile-menu-panel"
          :class="{ 'mobile-menu-panel--open': menuOpen }"
          :aria-hidden="!menuOpen"
          aria-label="Main navigation"
        >
          <RouterLink
            v-for="link in navLinks"
            :key="link.path"
            :to="link.path"
            class="mobile-menu-link"
            :class="{ 'mobile-menu-link--active': isActive(link.path) }"
            @click="closeMenu"
          >
            {{ link.name }}
          </RouterLink>

          <div class="mobile-menu-lang">
            <label class="mobile-menu-lang__label" for="lang-mobile">{{ langLabel }}</label>
            <select
              id="lang-mobile"
              :value="locale"
              class="mobile-menu-lang__select"
              @change="onLocaleChange"
            >
              <option v-for="opt in supportedLocales" :key="opt.code" :value="opt.code">
                {{ opt.label }}
              </option>
            </select>
          </div>

          <RouterLink to="/about#contact" class="btn btn-primary mobile-menu-cta" @click="closeMenu">
            {{ t('nav.contactUs') }}
          </RouterLink>
        </nav>
      </template>
    </Teleport>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useI18n, supportedLocales as locales } from '@/i18n'

const route = useRoute()
const { locale, setLocale, t, navLinks } = useI18n()
const supportedLocales = locales

const isScrolled = ref(false)
const menuOpen = ref(false)
const isMobile = ref(false)

const langLabel = computed(() => (locale.value === 'cs' ? 'Jazyk' : 'Language'))

const isActive = (path) => route.path === path || route.path.startsWith(path + '/')

const onLocaleChange = (e) => {
  setLocale(e.target.value)
}

const closeMenu = () => { menuOpen.value = false }
const handleScroll = () => { isScrolled.value = window.scrollY > 20 }
const checkMobile = () => {
  isMobile.value = window.innerWidth < 1024
  if (!isMobile.value) menuOpen.value = false
}

watch(menuOpen, (open) => {
  document.body.style.overflow = open && isMobile.value ? 'hidden' : ''
})

watch(isMobile, (mobile) => {
  if (!mobile) document.body.style.overflow = ''
})

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  window.addEventListener('resize', checkMobile)
  checkMobile()
  handleScroll()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', checkMobile)
  document.body.style.overflow = ''
})
</script>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  height: var(--header-height);
  transition: all var(--transition);
}

.header--scrolled {
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--color-border-light);
  box-shadow: var(--shadow-sm);
}

.header--menu-open {
  background: white;
  border-bottom: 1px solid var(--color-border-light);
  box-shadow: var(--shadow-sm);
  z-index: 1120;
}

.header__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  gap: 2rem;
}

.header__logo img {
  height: 44px;
  width: auto;
}

.header__nav {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.header__link {
  padding: 0.5rem 1rem;
  font-family: var(--font-display);
  font-size: 0.9375rem;
  font-weight: 500;
  color: var(--color-text-muted);
  border-radius: var(--radius-sm);
  transition: all var(--transition);
  position: relative;
}

.header__link:hover,
.header__link--active {
  color: var(--color-primary);
}

.header__link--active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 20px;
  height: 2px;
  background: var(--color-primary);
  border-radius: 1px;
}

.header__lang-mobile,
.header__cta-mobile {
  display: none;
}

.header__actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header__lang {
  padding: 0.375rem 0.75rem;
  font-size: 0.875rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: white;
  color: var(--color-text);
  cursor: pointer;
}

.header__lang-label {
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--color-text-muted);
  margin-bottom: 0.375rem;
  display: block;
}

.header__cta {
  padding: 0.625rem 1.25rem;
  font-size: 0.875rem;
}

.header__toggle {
  display: none;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  width: 44px;
  height: 44px;
  padding: 10px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: white;
}

.header__toggle span {
  display: block;
  height: 2px;
  background: var(--color-text);
  border-radius: 1px;
  transition: all var(--transition);
}

.header--menu-open .header__toggle span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.header--menu-open .header__toggle span:nth-child(2) {
  opacity: 0;
}

.header--menu-open .header__toggle span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

@media (max-width: 1023px) {
  .header__nav--desktop {
    display: none;
  }

  .header__toggle {
    display: flex;
  }

  .header__cta,
  .header__lang--desktop {
    display: none;
  }
}
</style>
