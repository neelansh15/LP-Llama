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
        <header class="flex justify-between">
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
    </div>
</template>
