import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Companies from './views/Companies'
import Reserve from './views/Reserve'
import DoReserve from './views/DoReserve'
import Login from './views/Login'
import Register from './views/Register'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { path: '/', name: 'login', component: Login },
    { path: '/home', name: 'home', component: Home },
    { path: '/companies', name: 'companies', component: Companies },
    { path: '/reserve', name: 'reserve', component: Reserve },
    { path: '/do_reserve', name: 'do_reserve', component: DoReserve },
    { path: '/register', name:'register', component: Register},
  ]
})
