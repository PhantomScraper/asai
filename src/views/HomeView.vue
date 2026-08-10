<template>
  <div class="home">
    <HomeHero />
    <SolutionChips />
    <ProductCallout />
    <ResourceCards />
    <DesignHubBand />
    <TechBanner />
    <SuccessStories />
    <InstitutionalBand />
    <LogoStrip />
  </div>
</template>

<script setup>
import HomeHero from '@/components/home/HomeHero.vue'
import SolutionChips from '@/components/home/SolutionChips.vue'
import ProductCallout from '@/components/home/ProductCallout.vue'
import ResourceCards from '@/components/home/ResourceCards.vue'
import DesignHubBand from '@/components/home/DesignHubBand.vue'
import TechBanner from '@/components/home/TechBanner.vue'
import SuccessStories from '@/components/home/SuccessStories.vue'
import InstitutionalBand from '@/components/home/InstitutionalBand.vue'
import LogoStrip from '@/components/home/LogoStrip.vue'
</script>

<style scoped>
/* The dark logo strip sits flush against the dark footer, Qorvo-style */
.home {
  background: white;
}
</style>
