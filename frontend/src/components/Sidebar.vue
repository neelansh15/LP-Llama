<script lang="ts" setup>
import { useRouter } from 'vue-router';
import { useStore } from '../store/web3store';

const { colors } = useStore()
const router = useRouter()

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
                <h1 class="text-xl font-bold cursor-pointer" @click="router.push('/')">
                    LP Llama
                </h1>
            </div>

            <ul class="space-y-4 px-5 pb-5">
                <li>
                    <router-link to="/" class="flex items-center space-x-1.5">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                        </svg>

                        <span>Dashboard</span>
                    </router-link>
                </li>
                <li>
                    <router-link to="/exchanges" class="flex items-center space-x-1.5">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M16.5 8.25V6a2.25 2.25 0 00-2.25-2.25H6A2.25 2.25 0 003.75 6v8.25A2.25 2.25 0 006 16.5h2.25m8.25-8.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-7.5A2.25 2.25 0 018.25 18v-1.5m8.25-8.25h-6a2.25 2.25 0 00-2.25 2.25v6" />
                        </svg>

                        <span>Exchanges</span>

                    </router-link>
                </li>
                <li>
                    <router-link to="/chains" class="flex items-center space-x-1.5">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M13.19 8.688a4.5 4.5 0 011.242 7.244l-4.5 4.5a4.5 4.5 0 01-6.364-6.364l1.757-1.757m13.35-.622l1.757-1.757a4.5 4.5 0 00-6.364-6.364l-4.5 4.5a4.5 4.5 0 001.242 7.244" />
                        </svg>

                        <span>Chains</span>

                    </router-link>
                </li>
                <li>
                    <router-link to="/1/sushiswap/0x3041CbD36888bECc7bbCBc0045E3B1f144466f5f">Test</router-link>
                </li>
            </ul>
        </div>
        <div class="mt-auto">
            <ul class="space-y-4 px-5 pb-5">
                <li>
                    <a href="https://github.com/neelansh15/LP-Llama" target="_blank"
                        class="flex items-center space-x-1.5">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" :style="{
                            fill: 'white'
                        }">
                            <path
                                d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                        </svg>
                        <span>Github</span>
                    </a>
                </li>
                <li>
                    <a href="https://devfolio.co/projects/lp-llama-5eac" target="_blank"
                        class="flex items-center space-x-1.5">
                        <img src="https://github.com/devfolioco/brand-assets/raw/main/Logo/Logo.svg" alt="Devfolio Logo" class="w-5 h-5" style="filter: brightness(10);">
                        <span>Devfolio</span>
                    </a>
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
