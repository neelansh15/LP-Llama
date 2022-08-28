<script lang="ts" setup>
import ApexCharts, { ApexOptions } from 'apexcharts'
import { onMounted, reactive, ref, watch } from 'vue';
import { useStore } from '../store/web3store';

const props = defineProps<{
    title: string
    label?: string
    data: any
}>()

const { colors } = useStore()

const element = ref(null)
const chart = ref(null as ApexCharts | null)

const options: ApexOptions = reactive({
    chart: {
        type: 'line',
    },
    tooltip: {
        theme: 'dark'
    },
    series: [{
        name: props.title,
        data: [30, 40, 35, 50, 49, 60, 70, 91, 125],
    }],
    xaxis: {
        categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
    },
    grid: {
        borderColor: '#222',
    },
    colors: [colors.primary, colors.secondary, colors.tertiary]
})

onMounted(() => {
    if (element.value)
        chart.value = new ApexCharts(element.value, options)
})

watch(colors, async (newColors) => {
    if (!chart.value)
        return
    chart.value = new ApexCharts(element.value, { ...options, colors: [newColors.primary, newColors.secondary, newColors.tertiary] })
    await chart.value.render()
})

</script>

<template>
    <div class="bg-dark-900 border border-dark-300 p-5 rounded-lg">
        <h3 class="text-gray-400 text-sm font-bold">{{ label ?? title }}</h3>
        <div ref="element"></div>
    </div>
</template>
