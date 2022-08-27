<script lang="ts" setup>
import type { Header, Item } from '../types'
import { getIconUrl } from '../utils';
import SafeImage from './SafeImage.vue';
import { chainTokens } from '../constants'
import { useRouter } from 'vue-router';

defineProps<{
    headers: Header[],
    items: Item[]
}>()

const router = useRouter()

</script>

<template>
    <table class="w-full bg-dark-900 p-5 rounded">
        <tr>
            <th v-for="header in headers" :key="header.label" class="text-gray-500 text-xs p-3 text-left">{{
                    header.label.toUpperCase()
            }}</th>
        </tr>
        <tr v-for="item in items" :key="item.name + item.exchange"
            @click="router.push(`/${item.chain}/pool/0x3041CbD36888bECc7bbCBc0045E3B1f144466f5f`)">
            <td class="flex space-x-3 items-center">
                <div class="flex -space-x-4">
                    <SafeImage :src="getIconUrl(item.token0)" class="w-7.5 h-7.5 mt-0.5" />
                    <SafeImage :src="getIconUrl(item.token1)" class="w-7.5 h-7.5 mt-0.5" />
                </div>
                <div>
                    <h1 class="text-sm font-semibold">{{ item.name }}</h1>
                    <h2 class="text-xs text-primary-300">{{ item.exchange }}</h2>
                </div>
            </td>
            <td>
                <SafeImage :src="getIconUrl(chainTokens[item.chain])" class="w-8 h-8" />
            </td>
            <td>{{ item.apy }}%</td>
            <td>{{ item.il }}%</td>
        </tr>
    </table>
</template>

<style scoped>
td {
    @apply p-3;
}
</style>
