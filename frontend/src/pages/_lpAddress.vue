<script lang="ts" setup>
import { onMounted, reactive, ref } from 'vue';
import { useRoute } from 'vue-router';
import { getIconUrl, rgbToHex } from '../utils'
import { explorerUrls } from '../constants'
import SafeImage from '../components/SafeImage.vue';
import Chart from '../components/Chart.vue';
import { useStore } from '../store/web3store';

// @ts-ignore
import ColorThief from 'colorthief'
import { storeToRefs } from 'pinia';

const store = useStore()
const { colors } = storeToRefs(store)

const token0Image = ref(null)

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
    // isLoading.value = true
    await new Promise((res, rej) => setTimeout(res, 2000))
    // isLoading.value = false
}

onMounted(() => fetchData())

function getDominantColor() {
    // Analyze dominant color
    const colorthief = new ColorThief()
    const color: [number, number, number][] = colorthief.getPalette(token0Image.value, 5)
    console.log({ color })
    store.$patch({
        colors: {
            primary: rgbToHex(color[0][0], color[0][1], color[0][2]),
            secondary: rgbToHex(color[4][0], color[4][1], color[4][2]),
            tertiary: rgbToHex(color[3][0], color[3][1], color[3][2]),
        }
    })
}

</script>

<template>
    <div v-if="isLoading" class="mx-auto my-auto">

        <div class="bg-black flex  rounded-lg">
            <div>
                <img src="https://c.tenor.com/meaVSqgv9hoAAAAM/llama-hair.gif" alt="Llama running in slow motion"
                    class="rounded-l-lg" />
            </div>
            <div class="p-4">
                <h1>Loading...</h1>
            </div>
        </div>
    </div>
    <div v-else class="p-5 px-10 pt-14">
        <header class="flex justify-between items-center pl-4">
            <div class="flex items-center space-x-2.5">
                <div class="flex -space-x-4">
                    <img :src="getIconUrl(data.token0)" @load="getDominantColor" class="hidden w-1 h-1"
                        ref="token0Image" crossorigin="anonymous" />
                    <SafeImage :src="getIconUrl(data.token0)" class="w-9 h-9 mt-0.5" />
                    <SafeImage :src="getIconUrl(data.token1)" class="w-9 h-9 mt-0.5" />
                </div>
                <div>
                    <h1 class="text-xl font-semibold">{{ data.name }}</h1>
                    <h2 class="text-sm" :style="{
                        color: colors.tertiary,
                        opacity: 100
                    }">{{ data.exchange }}</h2>
                </div>
            </div>
            <div>
                <a :href="explorerUrls[+chainId] + '/address/' + lpAddress" target="_blank">View on explorer &nearr;</a>
            </div>
        </header>

        <article class="mt-8">
            <!-- Cards -->
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

            <!-- Charts -->
            <div class="mt-8">
                <div class="md:(grid grid-cols-2) gap-4">
                    <Chart title="APY" data="" />
                    <Chart title="IL" label="Impermanant Loss" data="" />
                </div>
            </div>
        </article>
    </div>
</template>
