<script lang="ts" setup>
import DataTable from '../components/DataTable.vue';
import { Header } from '../types';

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
        exchange: 'SushiSwap',
    },
    {
        name: 'WETH-USDC',
        token0: 'WETH',
        token1: 'USDC',
        chain: 137,
        apy: 23,
        il: 8,
        exchange: 'SushiSwap',
    },
    {
        name: 'WETH-USDT',
        token0: 'WETH',
        token1: 'USDT',
        chain: 56,
        apy: 333,
        il: 2,
        exchange: 'PancakeSwap',
    },
]

</script>

<template>
    <div class="p-5 w-full">

        <!-- Card Collection -->
        <div class="md:(grid grid-cols-5 gap-5) mt-8 w-full">
            <div class="space-y-3 md:(col-span-2)">
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">Last Indexed At</h2>
                    <p class="mt-1 text-2xl font-bold text-cyan-400">27th August 2022</p>
                </div>
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">Total Chains Indexed</h2>
                    <p class="mt-1 text-2xl font-bold text-pink-400">5</p>
                    <!-- Use chain icons here later -->
                </div>
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">Total LPs Indexed</h2>
                    <p class="mt-1 text-2xl font-bold text-yellow-400">430</p>
                </div>
            </div>
            <div class="md:(col-span-3) info-card">
                <h2 class="uppercase text-gray-400 text-xs font-bold">Total Value Value (TVI)</h2>
                <p class="mt-1 text-3xl font-bold text-teal-400">$80.92B</p>
                <!-- Graph here -->
            </div>
        </div>

        <!-- Table -->
        <h1 class="mt-6 font-bold text-xl">Top Liquidity Pools / Farms</h1>
        <DataTable :items="items" :headers="headers" class="mt-3" />
    </div>
</template>

<style scoped>
.info-card {
    @apply p-5 border border-dark-300 bg-dark-800 rounded;
}
</style>
