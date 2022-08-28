<script lang="ts" setup>
import { useStore } from '../../store/web3store';
import ChainsTable from '../../components/ChainsTable.vue';

const store = useStore()

store.$patch({
    colors: {
        primary: '#cfae38',
        secondary: "#b39427",
        tertiary: "#876e14"
    }
})



</script>

<template>
    <div class="p-5 px-10 pt-14">
        <h1 class="font-bold text-3xl">Chains</h1>

        <ChainsTable class="mt-5" />
    </div>
</template>