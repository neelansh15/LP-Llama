<script lang="ts" setup>
import { onImageError } from '../utils'
</script>

<template>
    <img @error="onImageError">
</template>