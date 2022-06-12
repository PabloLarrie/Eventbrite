import Vue from "vue";
import VueRouter from "vue-router"
import HelloWorld from "@/components/HelloWorld";

const Home = { template: '<div>Home</div>' }

const routes = [
  { path: '/', component: HelloWorld },
]

const router = VueRouter.createRouter({
  history: VueRouter.createWebHashHistory(),
  routes,
})

const app = Vue.createApp({})

app.use(router)

app.mount('#app')

