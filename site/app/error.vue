<script setup lang="ts">
import type { NuxtError } from '#app'

const props = defineProps<{
  error: NuxtError
}>()

const { htmlLang, uiLocale, localePrefix, text, filterNavigation, filterSearchSections } = useDocsLocale()
const localizedError = computed(() => ({
  ...props.error,
  message: text.value.pageNotFoundDescription,
  statusMessage: props.error.statusCode === 404 ? text.value.pageNotFoundTitle : props.error.statusMessage
}))

useHead({
  htmlAttrs: {
    lang: htmlLang
  }
})

useSeoMeta({
  title: text.value.pageNotFoundTitle,
  description: text.value.pageNotFoundDescription
})

const { data: navigation } = await useAsyncData('navigation', () => queryCollectionNavigation('docs'))
const { data: files } = useLazyAsyncData('search', () => queryCollectionSearchSections('docs'), {
  server: false
})
const filteredNavigation = computed(() => filterNavigation(navigation.value))
const filteredFiles = computed(() => filterSearchSections(files.value))

provide('navigation', filteredNavigation)
</script>

<template>
  <UApp :locale="uiLocale">
    <AppHeader />

    <UError
      :error="localizedError"
      :redirect="localePrefix"
    />

    <AppFooter />

    <ClientOnly>
      <LazyUContentSearch
        :files="filteredFiles"
        :navigation="filteredNavigation"
        :title="text.searchTitle"
        :description="text.searchDescription"
        :placeholder="text.searchPlaceholder"
      />
    </ClientOnly>
  </UApp>
</template>
