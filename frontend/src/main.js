import Vue from 'vue'
import App from "./App.vue"
import { createApp } from "vue"
import { h } from 'vue'
import {router} from "@/router/router";


// Vue.config.productionTip = false

const app = createApp({
    router,
    render: h => h(App)
})

app.mount('#app')

export default {
  render() {
    return h('div')
  }
}
