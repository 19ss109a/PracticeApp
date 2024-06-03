export default {
  head: {
    titleTemplate: '%s - murakami junya playground',
    title: 'murakami junya playground',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  css: [],

  plugins: [],

  components: true,

  buildModules: [
    '@nuxtjs/vuetify',
  ],

  modules: [],

  router: {
    extendRoutes(routes, resolve) {
      routes.push({
        name: 'page-image-recognition', // ページ名
        path: '/page-image-recognition', // URLパス
        component: resolve(__dirname, 'pages/image-recognition.vue') // ページのファイルパス
      })
    }
  },
  env: {
    fastApiEndpoint: 'http://localhost:8000/'
  },
  server: {
    port: 3000, // ポート番号を3000に設定
    host: '0.0.0.0' // ホストをすべてのインターフェースにバインド
  },
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: true,
      themes: {
        light: {
          primary: '#ff4081',
          secondary: '#ff80ab',
          accent: '#ff4081',
          error: '#ff1744',
          warning: '#ff9100',
          info: '#00e5ff',
          success: '#00e676',
        },
      },
    },
  },

  build: {},
}
