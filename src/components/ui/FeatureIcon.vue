<template>
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
    <template v-if="name === 'modular'">
      <rect x="3" y="3" width="7" height="7" rx="1"/>
      <rect x="14" y="3" width="7" height="7" rx="1"/>
      <rect x="3" y="14" width="7" height="7" rx="1"/>
      <rect x="14" y="14" width="7" height="7" rx="1"/>
    </template>
    <template v-else-if="name === 'secure'">
      <path d="M12 2L4 6v6c0 5.5 3.8 10.7 8 12 4.2-1.3 8-6.5 8-12V6l-8-4z"/>
      <path d="M9 12l2 2 4-4"/>
    </template>
    <template v-else-if="name === 'versatile'">
      <circle cx="12" cy="12" r="3"/>
      <path d="M12 2v4M12 18v4M2 12h4M18 12h4"/>
    </template>
    <template v-else-if="name === 'simple'">
      <path d="M4 6h16M4 12h10M4 18h14"/>
    </template>
    <template v-else-if="name === 'unique'">
      <path d="M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z"/>
    </template>
    <template v-else>
      <path d="M9 12l2 2 4-4"/>
      <circle cx="12" cy="12" r="10"/>
    </template>
  </svg>
</template>

<script setup>
defineProps({
  name: { type: String, required: true },
})
</script>
