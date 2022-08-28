<script lang="ts" setup>
import DataTable from '../components/DataTable.vue';
import { useStore } from '../store/web3store';
import { Header } from '../types';
import axios from 'axios'
import { BASE_URL } from '../constants';
import { onMounted, Ref, ref } from 'vue';

const store = useStore()
store.$patch({
    colors: {
        primary: '#059669',
        secondary: '#047857',
    }
})

const totalValueIndexed = ref(0)

async function fetchData() {
    for (let i = 1; i <= 10; i++) {
        const { data, status } = await axios.get(BASE_URL + `/api/lp/?lp_id=${i}`)
        if (status === 200) {
            const metadata = {} as any
            metadata.token0 = data.token0
            metadata.token1 = data.token1
            metadata.exchange = data.exchange
            metadata.tvl = data.tvl
            metadata.chain = data.chain_id
            metadata.reserves0 = data.token_reserve0
            metadata.reserves1 = data.token_reserve1
            metadata.apy = data.apy[0].y[data.apy[0].y.length - 1]
            metadata.il = data.il[0].y[data.il[0].y.length - 1]
            items.value.push(metadata)
            totalValueIndexed.value += data.tvl
        }
    }

}

onMounted(() => fetchData())


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

const items: Ref<any[]> = ref([
    // {
    //     name: 'USDC-USDT',
    //     token0: 'USDC',
    //     token1: 'USDT',
    //     chain: 137,
    //     apy: 10,
    //     il: 0.01,
    //     tvl: 100_000,
    //     exchange: 'SushiSwap',
    // },
    // {
    //     name: 'WETH-USDC',
    //     token0: 'WETH',
    //     token1: 'USDC',
    //     chain: 137,
    //     apy: 23,
    //     il: 2,
    //     tvl: 100_120,
    //     exchange: 'SushiSwap',
    // },
    // {
    //     name: 'WETH-USDT',
    //     token0: 'WETH',
    //     token1: 'USDT',
    //     chain: 56,
    //     apy: 13,
    //     il: 2.01,
    //     tvl: 9_149,
    //     exchange: 'PancakeSwap',
    // },
])

</script>

<template>
    <div class="p-5 w-full">

        <!-- Card Collection -->
        <div class="md:(grid grid-cols-5 gap-5) mt-8 w-full">
            <div class="space-y-3 md:(col-span-2)">
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">Last Indexed At</h2>
                    <p class="mt-1 text-2xl font-bold">28th August 2022</p>
                </div>
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">Total Chains Indexed</h2>
                    <p class="mt-1 text-2xl font-bold">2</p>
                    <!-- Use chain icons here later -->
                </div>
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">Total LPs Indexed</h2>
                    <p class="mt-1 text-2xl font-bold">4</p>
                </div>
            </div>
            <div class="md:(col-span-3) info-card">
                <h2 class="uppercase text-gray-400 text-xs font-bold">Total Value Indexed (TVI)</h2>
                <p class="mt-1 text-4xl font-bold text-teal-400">${{ totalValueIndexed.toLocaleString('en-US') }}</p>
                <!-- Graph here -->
            </div>
        </div>

        <!-- Table -->
        <h1 class="mt-6 font-bold text-xl">Top Liquidity Pools / Farms</h1>
        <DataTable :items="items" :headers="headers" class="mt-3" />
    </div>
</template>

<style>
</style>
