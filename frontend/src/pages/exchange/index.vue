<script lang="ts" setup>
import { useStore } from '../../store/web3store';
import ExchangesTable from '../../components/ExchangesTable.vue';

const store = useStore()

store.$patch({
    colors: {
        primary: '#9b39cc',
        secondary: "#77289e",
        tertiary: "#571a75"
    }
})



</script>

<template>
    <div class="p-5 px-10 pt-14">
        <h1 class="font-bold text-3xl">Exchanges</h1>

        <ExchangesTable class="mt-5" />
    </div>
</template>