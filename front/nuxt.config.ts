// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    devtools: {enabled: true},
    routeRules: {
        '/api/**': {proxy: {to: `${process.env.BASE_URL}**`}}
    },
    runtimeConfig: {
        public: {
            baseURL: process.env.BASE_URL,
        },
    },
    build: {
        transpile: ["@vuepic/vue-datepicker"],
    },
})
