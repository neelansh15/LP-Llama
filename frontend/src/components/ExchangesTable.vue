<script lang="ts" setup>
import type { Header, Item } from '../types'
import { getIconUrl } from '../utils';
import SafeImage from './SafeImage.vue';
import { chainTokens } from '../constants'
import { useRouter } from 'vue-router';

const headers: Header[] = [
    {
        label: 'Exchange Name',
        key: 'name'
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
        label: 'Chains',
        key: 'chains'
    },
]

const items: any = [
    {
        name: 'SushiSwap',
        imageUrl: 'https://sushi.com/_next/static/media/logo.d019d88b.png',
        lp_indexed: 34,
        tvi: 1000,
        chains: [137, 1, 56]
    },
    {
        name: 'PancakeSwap',
        imageUrl: 'https://www.gitbook.com/cdn-cgi/image/width=40,height=40,fit=contain,dpr=2,format=auto/https%3A%2F%2F1397868517-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-MHREX7DHcljbY5IkjgJ%252Favatar-1602750187173.png%3Fgeneration%3D1602750187468978%26alt%3Dmedia',
        lp_indexed: 34,
        tvi: 1000,
        chains: [56]
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
        <tr v-for="item in items" :key="item.name + item.exchange">
            <td class="flex space-x-3 items-center">
                <SafeImage :src="item.imageUrl" class="w-7 h-7 mt-0.5 rounded-full" />
                <h1 class="text-sm font-semibold">{{ item.name }}</h1>
            </td>
            <td>{{ item.lp_indexed }}</td>
            <td>${{ item.tvi }}</td>
            <td class="flex space-x-1">
                <SafeImage v-for="chainId in item.chains" :key="chainId" :src="getIconUrl(chainTokens[chainId])"
                    class="w-8 h-8 cursor-pointer"
                    @click="router.push(`/${chainId}/sushiswap`)" />
            </td>
        </tr>
    </table>
</template>

<style scoped>
td {
    @apply p-3;
}
</style>
