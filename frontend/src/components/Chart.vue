<script lang="ts" setup>
import { computed } from '@vue/reactivity';
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

const activeTimeslot = ref(0) // 0 for 7 day, 1 for 1 month, etc.
const activeData = computed(() => props.data[activeTimeslot.value])

const options: ApexOptions = reactive({
    chart: {
        type: 'line',
    },
    tooltip: {
        theme: 'dark'
    },
    series: [
        {
            name: props.title,
            data: activeData.value.y,
        }
    ],
    xaxis: {
        categories: activeData.value.x
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

watch(activeData, async (newData) => {
    chart.value = new ApexCharts(element.value, { ...options, series: [{ name: props.title, data: newData.value.y }], xaxis: { categories: newData.value.x } })
    await chart.value.render()
})

</script>

<template>
    <div class="bg-dark-900 border border-dark-300 p-5 rounded-lg">
        <h3 class="text-gray-400 text-sm font-bold">{{ label ?? title }}</h3>
        <div ref="element"></div>
        <div class="px-3 py-2 rounded-lg flex items-center space-x-2 text-xs text-right">
            <div class="tab" :style="{
                backgroundColor: activeTimeslot === 0 ? colors.primary : ''
            }" @click="activeTimeslot = 0">7 Days</div>
            <div class=" tab" :style="{
                backgroundColor: activeTimeslot === 1 ? colors.primary : ''
            }" @click="activeTimeslot = 1">1 Month</div>
        </div>
    </div>
</template>

<style scoped>
.tab {
    @apply px-2 py-1 cursor-pointer rounded-lg;
}
</style>
