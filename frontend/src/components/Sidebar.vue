<script lang="ts" setup>
import { useStore } from '../store/web3store';

const { colors } = useStore()

</script>

<template>
    <!-- bg-gradient-to-b from-primary-600 to-primary-700 -->
    <nav class="flex flex-col justify-between h-full rounded-lg" :style="{
        background: `linear-gradient(to bottom, ${colors.primary}, ${colors.secondary}), #000`,
    }">
        <div class="space-y-8">
            <div class="border-b p-5" :style="{
                borderColor: colors.secondary + '49',
            }">
                <h1 class="text-xl font-bold">
                    LP Llama
                </h1>
            </div>

            <ul class="space-y-2 px-5 pb-5">
                <li>
                    <router-link to="/">Dashboard</router-link>
                </li>
                <li>
                    <router-link to="/">Exchange</router-link>
                </li>
                <li>
                    <router-link to="/pool/1/0x3041CbD36888bECc7bbCBc0045E3B1f144466f5f">Test</router-link>
                </li>
            </ul>
        </div>
        <div class="h-50 mt-auto" :style="{
            backgroundImage: 'url(\'/llama.png\')',
            backgroundSize: '200px',
            backgroundRepeat: 'no-repeat',
            backgroundPosition: '260% 100%'
        }">
        </div>
        <p class="text-xs text-gray-300 p-5">Team ZKMaxiz &sdot; Unfold Hackathon </p>
    </nav>
</template>

<style scoped>
li a {
    @apply font-semibold transition;
}

li a:hover {
    @apply text-gray-300;
}
</style>
