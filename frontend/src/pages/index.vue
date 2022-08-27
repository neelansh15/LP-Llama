<script lang="ts" setup>
import { useStore } from '../store/web3store';

const { address } = useStore()
</script>

<template>
    <h1>Home</h1>
    <p>{{ address }}</p>
</template>
