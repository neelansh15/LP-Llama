<script lang="ts" setup>
</script>

<template>
    <nav class="flex flex-col justify-between bg-primary-600 h-full">
        <div class="space-y-8">
            <div class="border-b border-b-primary-500 p-5">
                <h1 class="text-xl font-bold">
                    LP Llama
                </h1>
            </div>

            <ul class="space-y-2 px-5 pb-5">
                <li>
                    <router-link to="/">Dashboard</router-link>
                </li>
                <li>
                    <router-link to="/">Exchange</router-link>
                </li>
            </ul>
        </div>
        <p class="text-xs text-gray-300 p-5">Team ZKMaxiz</p>
    </nav>
</template>

<style scoped>
li a {
    @apply font-semibold transition;
}

li a:hover {
    @apply text-primary-500;
}
</style>
