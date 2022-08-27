<script lang="ts" setup>
import { reactive, ref } from 'vue';
import { useRoute } from 'vue-router';
import { getIconUrl } from '../utils'
import { explorerUrls } from '../constants'
import SafeImage from '../components/SafeImage.vue';

const isLoading = ref(true)

const route = useRoute()
const { chainId, lpAddress } = route.params

const data = reactive({
    name: 'USDC-USDT',
    token0: 'USDC',
    token1: 'USDT',
    exchange: 'SushiSwap'
})

async function fetchData() {
    isLoading.value = true
    console.log({ chainId, lpAddress })
    isLoading.value = false
}

</script>

<template>
    <div class="p-5 mx-5 mt-8">
        <header class="flex justify-between items-center">
            <div class="flex items-center space-x-2.5">
                <div class="flex -space-x-4">
                    <SafeImage :src="getIconUrl(data.token0)" class="w-9 h-9 mt-0.5" />
                    <SafeImage :src="getIconUrl(data.token1)" class="w-9 h-9 mt-0.5" />
                </div>
                <div>
                    <h1 class="text-xl font-semibold">{{ data.name }}</h1>
                    <h2 class="text-sm text-primary-300">{{ data.exchange }}</h2>
                </div>
            </div>
            <div>
                <a :href="explorerUrls[+chainId] + '/address/' + lpAddress" target="_blank">View on explorer &nearr;</a>
            </div>
        </header>

        <article class="mt-8">
            <div class="space-y-3 md:(space-y-0 grid grid-cols-4 gap-3)">
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">Total Value Locked (TVL)</h2>
                    <p class="mt-1 text-2xl font-bold">$1.12m</p>
                </div>
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">APY</h2>
                    <p class="mt-1 text-2xl font-bold">45%</p>
                </div>
                <div class="info-card">
                    <div class="flex items-center space-x-1">
                        <SafeImage :src="getIconUrl(data.token0)" class="w-3.5 h-3.5 mt-[1px]" />
                        <h2 class="uppercase text-gray-400 text-xs font-bold">{{ data.token0 }} Reserves</h2>
                    </div>
                    <p class="mt-1 text-2xl font-bold ">531,203</p>
                </div>
                <div class="info-card">

                    <div class="flex items-center space-x-1">
                        <SafeImage :src="getIconUrl(data.token1)" class="w-3.5 h-3.5 mt-[1px]" />
                        <h2 class="uppercase text-gray-400 text-xs font-bold">{{ data.token1 }} Reserves</h2>
                    </div>

                    <p class="mt-1 text-2xl font-bold">542,984</p>
                </div>
            </div>
        </article>
    </div>
</template>
