<script lang="ts" setup>
import ApexCharts from 'apexcharts'
import { onMounted, ref } from 'vue';

const props = defineProps<{
    title: string
    data: any
}>()

const element = ref(null)

const options = {
    chart: {
        type: 'line'
    },
    series: [{
        name: 'sales',
        data: [30, 40, 35, 50, 49, 60, 70, 91, 125]
    }],
    xaxis: {
        categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
    }
}

onMounted(() => {
    const chart = new ApexCharts(element.value, options)
    chart.render()
})

</script>

<template>
    <div class="bg-dark-900 border border-dark-300 p-5 rounded-md">
        <h3 class="text-gray-400 text-sm font-bold">{{ title }}</h3>
        <div ref="element"></div>
    </div>
</template>
