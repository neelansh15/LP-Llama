<script lang="ts" setup>
import { useRoute } from 'vue-router';
import SafeImage from '../../components/SafeImage.vue';
import { startCase } from 'lodash'
import { useStore } from '../../store/web3store';
import { getIconUrl, rgbToHex } from '../../utils';
import { chainTokens, chainNames } from '../../constants';

// @ts-ignore
import ColorThief from 'colorthief'
import { ref } from 'vue';
import DataTable from '../../components/DataTable.vue';
import { Header } from '../../types';

const data = {
    name: 'PancakeSwap',
    imageUrl: 'https://pancakeswap.finance/images/tokens/0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82.png',
    lp_indexed: 34,
    tvi: 1000,
    chains: [56]
}

const headers: Header[] = [
    {
        label: 'LP Token Pair',
        key: 'name'
    },
    {
        label: 'Chain',
        key: 'chain'
    },
    {
        label: 'Total Value Locked',
        key: 'tvl'
    },
    {
        label: 'APY',
        key: 'apy'
    },
    {
        label: 'IL',
        key: 'il'
    },
]

const items = [
    {
        name: 'USDC-USDT',
        token0: 'USDC',
        token1: 'USDT',
        chain: 137,
        apy: 10,
        il: 10,
        tvl: 100_000,
        exchange: 'SushiSwap',
    },
    {
        name: 'WETH-USDC',
        token0: 'WETH',
        token1: 'USDC',
        chain: 137,
        apy: 23,
        il: 8,
        tvl: 100_120,
        exchange: 'SushiSwap',
    },
    {
        name: 'WETH-USDT',
        token0: 'WETH',
        token1: 'USDT',
        chain: 56,
        apy: 333,
        il: 2,
        tvl: 9_149,
        exchange: 'PancakeSwap',
    },
]


const image = ref(null)

const { params } = useRoute()
const { chainId, exchange } = params

const store = useStore()

function getDominantColor() {
    // Analyze dominant color
    const colorthief = new ColorThief()
    const color: [number, number, number][] = colorthief.getPalette(image.value, 5)
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
    <div class="p-5 px-10 pt-14">
        <header class="flex items-center space-x-2">
            <img :src="data.imageUrl" @load="getDominantColor" class="hidden w-1 h-1" ref="image"
                crossorigin="anonymous" />
            <SafeImage :src="data.imageUrl" class="w-12 h-12 rounded-full" />
            <div class="space-y-0.5">
                <h1 class="font-bold text-lg">{{ startCase(exchange.toString()).replace(" ", "") }}</h1>
                <div class="text-sm text-gray-300 flex space-x-1">
                    <SafeImage :src="getIconUrl(chainTokens[+chainId])" class="w-5 h-5 mt-[1px] rounded-full" />
                    <p>{{ chainNames[+chainId] }}</p>
                </div>
            </div>
        </header>

        <DataTable :items="items" :headers="headers" class="mt-10" />
    </div>
</template>