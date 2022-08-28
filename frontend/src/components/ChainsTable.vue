<script lang="ts" setup>
import type { Header, Item } from '../types'
import { getIconUrl } from '../utils';
import SafeImage from './SafeImage.vue';
import { chainNames, chainTokens, exchangeLogos } from '../constants'
import { useRouter } from 'vue-router';

const headers: Header[] = [
    {
        label: 'Chain',
        key: 'chain'
    },
    {
        label: 'LP Tokens Indexed',
        key: 'lp_indexed'
    },
    {
        label: 'Total Value Indexed',
        key: 'tvi'
    },
    {
        label: 'Exchanges',
        key: 'exchanges'
    },
]

const items: any = [
    {
        chainId: 137,
        lp_indexed: 34,
        apy: 97,
        tvi: 1000,
        exchanges: ['sushiswap']
    },
    {
        chainId: 56,
        lp_indexed: 34,
        apy: 56,
        tvi: 1000,
        exchanges: ['pancakeswap', 'sushiswap']
    },
]

const router = useRouter()

</script>

<template>
    <table class="w-full bg-dark-900 p-5 rounded">
        <tr>
            <th v-for="header in headers" :key="header.label" class="text-gray-500 text-xs p-3 text-left">{{
                    header.label.toUpperCase()
            }}</th>
        </tr>
        <tr v-for="item in items" :key="item.chainId">
            <td class="flex space-x-3 items-center">
                <SafeImage :src="getIconUrl(chainTokens[item.chainId])" class="w-7 h-7 mt-0.5 rounded-full" />
                <h1 class="text-sm font-semibold">{{ chainNames[item.chainId] }}</h1>
            </td>
            <td>{{ item.lp_indexed }}</td>
            <td>${{ item.tvi.toLocaleString('en-US') }}</td>
            <td class="flex space-x-1">
                <SafeImage v-for="exchange in item.exchanges" :key="exchange" :src="exchangeLogos[exchange]"
                    class="w-8 h-8 cursor-pointer transition hover:(transform -translate-y-0.5)"
                    @click="router.push(`/${item.chainId}/${exchange}`)" />
            </td>
        </tr>
    </table>
</template>

<style scoped>
td {
    @apply p-3;
}
</style>
