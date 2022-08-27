<script lang="ts" setup>
import { useRoute } from 'vue-router';

const route = useRoute()
const { chainId, lpAddress } = route.params

async function fetchData() {
    console.log({ chainId, lpAddress })
}

</script>

<template>
    <h1> {{ chainId }} {{ lpAddress }}</h1>
</template>
