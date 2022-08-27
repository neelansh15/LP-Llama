<script lang="ts" setup>
</script>

<template>
    <nav
        class="flex flex-col justify-between h-full bg-gradient-to-b from-primary-600 to-primary-700 ">
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
                <li>
                    <router-link to="/pool/1/0x3041CbD36888bECc7bbCBc0045E3B1f144466f5f">Test</router-link>
                </li>
            </ul>
        </div>
        <p class="text-xs text-gray-300 p-5">Team ZKMaxiz &sdot; Unfold Hackathon </p>
    </nav>
</template>

<style scoped>
li a {
    @apply font-semibold transition;
}

li a:hover {
    @apply text-gray-300;
}
</style>
