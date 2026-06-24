<template>
  <figure class="showcase" :class="`showcase--${variant}`">
    <div class="showcase__frame">
      <img
        :src="primaryImage"
        :alt="primaryAlt"
        class="showcase__primary"
        loading="eager"
      />
      <img
        v-if="secondaryImage"
        :src="secondaryImage"
        :alt="secondaryAlt"
        class="showcase__secondary"
        loading="lazy"
      />
    </div>
    <figcaption v-if="caption" class="showcase__caption">{{ caption }}</figcaption>
  </figure>
</template>

<script setup>
defineProps({
  primaryImage: { type: String, required: true },
  primaryAlt: { type: String, default: '' },
  secondaryImage: { type: String, default: '' },
  secondaryAlt: { type: String, default: '' },
  caption: { type: String, default: '' },
  variant: { type: String, default: 'hero' },
})
</script>

<style scoped>
.showcase {
  margin: 0;
  width: 100%;
}

.showcase__frame {
  position: relative;
  background: white;
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border-light);
  box-shadow: 0 24px 48px rgba(15, 20, 25, 0.1);
  overflow: hidden;
  padding: clamp(0.75rem, 2vw, 1.25rem);
}

.showcase--hero .showcase__frame {
  min-height: clamp(280px, 42vw, 420px);
}

.showcase__primary {
  width: 100%;
  height: auto;
  display: block;
  object-fit: contain;
}

.showcase__secondary {
  position: absolute;
  right: clamp(0.5rem, 2vw, 1rem);
  bottom: clamp(0.5rem, 2vw, 1rem);
  width: min(38%, 180px);
  border-radius: var(--radius-md);
  border: 2px solid white;
  box-shadow: var(--shadow-md);
  background: white;
  object-fit: contain;
}

.showcase--banner .showcase__frame {
  padding: 0;
  background: var(--color-bg);
}

.showcase--banner .showcase__primary {
  width: 100%;
  max-height: none;
}

.showcase__caption {
  margin-top: 0.75rem;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  text-align: center;
}
</style>
