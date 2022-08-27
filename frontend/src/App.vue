<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import Sidebar from './components/Sidebar.vue';
import { useStore } from './store/web3store';

const { colors } = useStore()
</script>

<template>
  <!-- bg-gradient-to-b from-primary-700/30 via-transparent to-transparent -->
  <div class="grid grid-cols-10 min-h-screen pb-10 w-full text-white bg-dark-700 transition" :style="{
    background: `linear-gradient(to bottom, ${colors.primary}80, transparent, transparent), #000`,
    transition: 'background-image 4s linear',
  }">
    <Sidebar class="col-span-2 m-5" />
    <router-view class="col-span-8" />
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
