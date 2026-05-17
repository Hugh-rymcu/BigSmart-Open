<script setup lang="ts">
const { seo } = useAppConfig()
const { htmlLang, uiLocale, text, filterNavigation, filterSearchSections } = useDocsLocale()

const { data: navigation } = await useAsyncData('navigation', () => queryCollectionNavigation('docs'))
const { data: files } = useLazyAsyncData('search', () => queryCollectionSearchSections('docs'), {
  server: false
})
const filteredNavigation = computed(() => filterNavigation(navigation.value))
const filteredFiles = computed(() => filterSearchSections(files.value))

useHead({
  meta: [
    { name: 'viewport', content: 'width=device-width, initial-scale=1' }
  ],
  link: [
    { rel: 'icon', href: './favicon.ico' }
  ],
  htmlAttrs: {
    lang: htmlLang
  }
})

useSeoMeta({
  titleTemplate: `%s - ${seo?.siteName}`,
  ogSiteName: seo?.siteName,
  twitterCard: 'summary_large_image'
})

provide('navigation', filteredNavigation)
</script>

<template>
  <UApp :locale="uiLocale">
    <NuxtLoadingIndicator />

    <AppHeader />

    <UMain>
      <NuxtLayout>
        <NuxtPage />
      </NuxtLayout>
    </UMain>

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
