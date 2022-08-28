<script lang="ts" setup>
import { onMounted, reactive, ref } from 'vue';
import { useRoute } from 'vue-router';
import { getIconUrl, rgbToHex } from '../utils'
import { BASE_URL, explorerUrls } from '../constants'
import SafeImage from '../components/SafeImage.vue';
import Chart from '../components/Chart.vue';
import { useStore } from '../store/web3store';
import axios from 'axios'

// @ts-ignore
import ColorThief from 'colorthief'
import { storeToRefs } from 'pinia';
import Loader from '../components/Loader.vue';

const store = useStore()
const { colors } = storeToRefs(store)

const token0Image = ref(null)

const isLoading = ref(true)

const apyData = ref([])
const ilData = ref([])

const route = useRoute()
const { chainId, lpAddress } = route.params

const metadata = reactive({
    token0: 'USDC',
    token1: 'USDT',
    exchange: 'SushiSwap',
    tvl: 0,
    reserves0: 0,
    reserves1: 0,
    apy: 0
})

async function fetchData() {
    isLoading.value = true
    // await new Promise((res, rej) => setTimeout(res, 2000))

    const { data, status } = await axios.get(BASE_URL + '/api/lp/?lp_id=3')
    console.log({ data })
    if (status === 200) {
        metadata.token0 = data.token0
        metadata.token1 = data.token1
        metadata.exchange = data.exchange
        metadata.tvl = data.tvl
        metadata.reserves0 = data.token_reserve0
        metadata.reserves1 = data.token_reserve1
        metadata.apy = data.apy[0].y[data.apy[0].y.length - 1]

        apyData.value = data.apy
        ilData.value = data.il
    }

    isLoading.value = false
}

onMounted(() => fetchData())

function getDominantColor() {
    // Analyze dominant color
    const colorthief = new ColorThief()
    const color: [number, number, number][] = colorthief.getPalette(token0Image.value, 5)
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
    <Loader v-if="isLoading" />
    <div v-else class="p-5 px-10 pt-14">
        <header class="flex justify-between items-center pl-4">
            <div class="flex items-center space-x-2.5">
                <div class="flex -space-x-4">
                    <img :src="getIconUrl(metadata.token0)" @load="getDominantColor" class="hidden w-1 h-1"
                        ref="token0Image" crossorigin="anonymous" />
                    <SafeImage :src="getIconUrl(metadata.token0)" class="w-9 h-9 mt-0.5" />
                    <SafeImage :src="getIconUrl(metadata.token1)" class="w-9 h-9 mt-0.5" />
                </div>
                <div>
                    <h1 class="text-xl font-semibold">{{ metadata.token0 }}-{{ metadata.token1 }}</h1>
                    <h2 class="text-sm" :style="{
                        color: colors.tertiary,
                        opacity: 100
                    }">{{ metadata.exchange }}</h2>
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
                    <p class="mt-1 text-2xl font-bold">${{ Intl.NumberFormat('en-US', {
                            compactDisplay: 'short',
                            currency: 'USD'
                        }).format(metadata.tvl)
                    }}</p>
                </div>
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">APR</h2>
                    <p class="mt-1 text-2xl font-bold">{{ metadata.apy.toLocaleString('en-US') }}%</p>
                </div>
                <div class="info-card">
                    <div class="flex items-center space-x-1">
                        <SafeImage :src="getIconUrl(metadata.token0)" class="w-3.5 h-3.5 mt-[1px]" />
                        <h2 class="uppercase text-gray-400 text-xs font-bold">{{ metadata.token0 }} Reserves</h2>
                    </div>
                    <p class="mt-1 text-2xl font-bold ">{{ metadata.reserves0.toLocaleString('en-US') }}</p>
                </div>
                <div class="info-card">

                    <div class="flex items-center space-x-1">
                        <SafeImage :src="getIconUrl(metadata.token1)" class="w-3.5 h-3.5 mt-[1px]" />
                        <h2 class="uppercase text-gray-400 text-xs font-bold">{{ metadata.token1 }} Reserves</h2>
                    </div>

                    <p class="mt-1 text-2xl font-bold">{{ metadata.reserves1.toLocaleString('en-US') }}</p>
                </div>
            </div>

            <!-- Charts -->
            <div class="mt-8">
                <div class="md:(grid grid-cols-2) gap-4">
                    <Chart title="APY" :data="apyData" />
                    <Chart title="IL" label="Impermanant Loss" :data="ilData" />
                </div>
            </div>
        </article>
    </div>
</template>
