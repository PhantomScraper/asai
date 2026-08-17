<template>
  <div class="home">
    <HomeHero />
    <HighlightsBand />
    <ValueBullets />
    <InstitutionalBand />
    <HelpColumns />
    <UdkCallout />
    <SuccessStories />
    <DocsBand />
    <LogoStrip />
  </div>
</template>

<script setup>
import HomeHero from '@/components/home/HomeHero.vue'
import HighlightsBand from '@/components/home/HighlightsBand.vue'
import ValueBullets from '@/components/home/ValueBullets.vue'
import InstitutionalBand from '@/components/home/InstitutionalBand.vue'
import HelpColumns from '@/components/home/HelpColumns.vue'
import UdkCallout from '@/components/home/UdkCallout.vue'
import SuccessStories from '@/components/home/SuccessStories.vue'
import DocsBand from '@/components/home/DocsBand.vue'
import LogoStrip from '@/components/home/LogoStrip.vue'
</script>

<style scoped>
/* The dark logo strip sits flush against the dark footer, Qorvo-style */
.home {
  background: white;
}
</style>
