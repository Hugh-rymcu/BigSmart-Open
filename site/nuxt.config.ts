// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    '@nuxt/eslint',
    '@nuxt/image',
    '@nuxt/ui',
    '@nuxt/content',
    'nuxt-llms',
    '@nuxtjs/mcp-toolkit'
  ],

  devtools: {
    enabled: true
  },

  css: ['~/assets/css/main.css'],

  content: {
    build: {
      markdown: {
        toc: {
          searchDepth: 2
        }
      }
    },
    experimental: {
      sqliteConnector: 'native'
    }
  },

  ui: {
    fonts: false
  },

  experimental: {
    asyncContext: true
  },

  compatibilityDate: '2024-07-11',

  nitro: {
    prerender: {
      routes: [
        '/',
        '/zh',
        '/en'
      ],
      crawlLinks: true
    }
  },

  eslint: {
    config: {
      stylistic: {
        commaDangle: 'never',
        braceStyle: '1tbs'
      }
    }
  },

  icon: {
    provider: 'server',
    clientBundle: {
      scan: true,
      sizeLimitKb: 512
    },
    serverBundle: {
      collections: ['lucide', 'simple-icons']
    },
    fallbackToApi: false
  },

  image: {
    provider: 'none'
  },

  llms: {
    domain: 'https://rymcu.github.io/BigSmart-Open/',
    title: 'RYMCU BigSmart Docs',
    description: 'Documentation, hardware resources, firmware, and tools for the RYMCU BigSmart ESP32-S3 development board.',
    full: {
      title: 'RYMCU BigSmart Docs - Full Documentation',
      description: 'Complete documentation for the RYMCU BigSmart ESP32-S3 development board.'
    },
    sections: [
      {
        title: '中文文档',
        contentCollection: 'docs',
        contentFilters: [
          { field: 'path', operator: 'LIKE', value: '/zh%' }
        ]
      },
      {
        title: 'English Documentation',
        contentCollection: 'docs',
        contentFilters: [
          { field: 'path', operator: 'LIKE', value: '/en%' }
        ]
      }
    ]
  },

  mcp: {
    name: 'RYMCU BigSmart Docs'
  }
})
