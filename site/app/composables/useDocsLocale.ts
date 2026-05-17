import type { ContentNavigationItem } from '@nuxt/content'
import { en, zh_cn } from '@nuxt/ui/locale'

type DocsLocale = 'zh' | 'en'

type SearchSection = {
  id?: string
  path?: string
}

const messages = {
  zh: {
    copyActions: '打开复制操作菜单',
    copyMarkdownLink: '复制 Markdown 链接',
    copyPage: '复制本页',
    copiedToClipboard: '已复制到剪贴板',
    editThisPage: '编辑本页',
    openInChatGPT: '在 ChatGPT 中打开',
    openInClaude: '在 Claude 中打开',
    pageNotFoundDescription: '抱歉，找不到这个页面。',
    pageNotFoundTitle: '页面未找到',
    projectLinksTitle: '项目链接',
    readInAiPrompt: (url: string) => `请阅读 ${url}，我会基于它继续提问。`,
    searchDescription: '在当前语言文档中搜索页面、标题和正文。',
    searchPlaceholder: '搜索文档...',
    searchTitle: '搜索文档',
    tocTitle: '目录',
    viewAsMarkdown: '查看 Markdown'
  },
  en: {
    copyActions: 'Open copy actions menu',
    copyMarkdownLink: 'Copy Markdown link',
    copyPage: 'Copy page',
    copiedToClipboard: 'Copied to clipboard',
    editThisPage: 'Edit this page',
    openInChatGPT: 'Open in ChatGPT',
    openInClaude: 'Open in Claude',
    pageNotFoundDescription: 'We are sorry, but this page could not be found.',
    pageNotFoundTitle: 'Page not found',
    projectLinksTitle: 'Project links',
    readInAiPrompt: (url: string) => `Read ${url} so I can ask questions about it.`,
    searchDescription: 'Search pages, headings, and content in the current language.',
    searchPlaceholder: 'Search docs...',
    searchTitle: 'Search docs',
    tocTitle: 'On this page',
    viewAsMarkdown: 'View as Markdown'
  }
} as const

function isLocalePath(value: string | undefined, prefix: string) {
  return value === prefix || value?.startsWith(`${prefix}/`)
}

function filterNavigationByPrefix(items: ContentNavigationItem[] | undefined, prefix: string): ContentNavigationItem[] {
  const filteredItems: ContentNavigationItem[] = []

  for (const item of items || []) {
    const children = filterNavigationByPrefix(item.children, prefix)

    if (!isLocalePath(item.path, prefix) && !children.length) {
      continue
    }

    filteredItems.push({
      ...item,
      children
    })
  }

  return filteredItems
}

function filterSearchSectionsByPrefix<T extends SearchSection>(items: T[] | undefined, prefix: string): T[] {
  return (items || []).filter((item) => {
    return isLocalePath(item.path, prefix) || isLocalePath(item.id?.split('#')[0], prefix)
  })
}

export function useDocsLocale() {
  const route = useRoute()

  const locale = computed<DocsLocale>(() => route.path.startsWith('/en') ? 'en' : 'zh')
  const localePrefix = computed(() => `/${locale.value}`)
  const htmlLang = computed(() => locale.value === 'en' ? 'en' : 'zh-CN')
  const uiLocale = computed(() => locale.value === 'en' ? en : zh_cn)
  const text = computed(() => messages[locale.value])
  const oppositeLocale = computed<DocsLocale>(() => locale.value === 'en' ? 'zh' : 'en')
  const oppositeLocaleLabel = computed(() => locale.value === 'en' ? '中文' : 'English')

  const oppositeLocalePath = computed(() => {
    const currentPrefix = localePrefix.value
    const nextPrefix = `/${oppositeLocale.value}`

    if (isLocalePath(route.path, currentPrefix)) {
      return route.path.replace(currentPrefix, nextPrefix)
    }

    return nextPrefix
  })

  function filterNavigation(items: ContentNavigationItem[] | undefined) {
    return filterNavigationByPrefix(items, localePrefix.value)
  }

  function filterSearchSections<T extends SearchSection>(items: T[] | undefined) {
    return filterSearchSectionsByPrefix(items, localePrefix.value)
  }

  function isCurrentLocalePath(value: string | undefined) {
    return isLocalePath(value, localePrefix.value)
  }

  return {
    locale,
    localePrefix,
    htmlLang,
    uiLocale,
    text,
    oppositeLocale,
    oppositeLocaleLabel,
    oppositeLocalePath,
    filterNavigation,
    filterSearchSections,
    isCurrentLocalePath
  }
}
