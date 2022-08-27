<script lang="ts" setup>

</script>

<template>
    <div class="p-5 w-full">

        <!-- Card Collection -->
        <div class="md:(grid grid-cols-5 gap-5) mt-10 w-full">
            <div class="space-y-3 md:(col-span-2)">
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">Last Indexed At</h2>
                    <p class="mt-1 text-2xl font-bold text-cyan-400">27th August 2022</p>
                </div>
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">Total Chains Indexed</h2>
                    <p class="mt-1 text-2xl font-bold text-pink-400">5</p>
                    <!-- Use chain icons here later -->
                </div>
                <div class="info-card">
                    <h2 class="uppercase text-gray-400 text-xs font-bold">Total LPs Indexed</h2>
                    <p class="mt-1 text-2xl font-bold text-yellow-400">430</p>
                </div>
            </div>
            <div class="md:(col-span-3) info-card">
                <h2 class="uppercase text-gray-400 text-xs font-bold">Total Indexed Value (TIL)</h2>
                <p class="mt-1 text-3xl font-bold text-teal-400">$80.92B</p>
                <!-- Graph here -->
            </div>
        </div>
    </div>
</template>

<style scoped>
.info-card {
    @apply p-5 border border-dark-300 bg-dark-800 rounded;
}
</style>
