<script lang="ts" setup>
import type { Header, Item } from '../types'
import { getIconUrl } from '../utils';
import SafeImage from './SafeImage.vue';
import { chainTokens } from '../constants'

const props = defineProps<{
    headers: Header[],
    items: Item[]
}>()

</script>

<template>
    <table class="w-full bg-dark-700 p-5 rounded">
        <tr>
            <th v-for="header in headers" :key="header.label" class="text-gray-300 text-xs p-3 text-left">{{
                    header.label.toUpperCase()
            }}</th>
        </tr>
        <tr v-for="item in props.items" :key="item.name + item.exchange">
            <td class="flex space-x-3 items-center">
                <div class="flex -space-x-4">
                    <SafeImage :src="getIconUrl(item.token0)" class="w-7.5 h-7.5 mt-0.5" />
                    <SafeImage :src="getIconUrl(item.token1)" class="w-7.5 h-7.5 mt-0.5" />
                </div>
                <div>
                    <h1 class="text-sm">{{ item.name }}</h1>
                    <h2 class="text-xs text-primary-300">{{ item.exchange }}</h2>
                </div>
            </td>
            <td>
                <SafeImage :src="getIconUrl(chainTokens[item.chain])" />
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
