<script setup lang="ts">
const { oppositeLocaleLabel, oppositeLocalePath } = useDocsLocale()
</script>

<template>
  <UButton
    :to="oppositeLocalePath"
    :label="oppositeLocaleLabel"
    icon="i-lucide-languages"
    color="neutral"
    variant="ghost"
    size="sm"
    class="font-medium"
  />
</template>
