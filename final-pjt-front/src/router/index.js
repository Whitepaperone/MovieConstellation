import Vue from 'vue'
import VueRouter from 'vue-router'

import MovieView from '../views/movie/MovieView.vue'
import RandomView from '../views/movie/RandomView.vue'
import WatchList from '../views/movie/WatchList.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movieview',
    component: MovieView
  },
  {
    path:'/random',
    name:'randomview',
    component : RandomView
  },
  {
    path:'/watch',
    name:'watchlist',
    component : WatchList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
