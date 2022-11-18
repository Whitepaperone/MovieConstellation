import Vue from 'vue'
import VueRouter from 'vue-router'

import MovieView from '../views/movie/MovieView.vue'
import RandomView from '../views/movie/RandomView.vue'
import WatchList from '../views/movie/WatchList.vue'
import SearchMovieView from '@/views/movie/SearchMovieView'
import MovieViewCardDetail from '@/views/movie/MovieViewCardDetail'

import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Logout from '@/views/accounts/Logout'
import Profile from '@/views/accounts/Profile'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movieview',
    component: MovieView
  },
  {
    path:'/black-hole',
    name:'randomview',
    component : RandomView
  },
  {
    path:'/watch',
    name:'watchlist',
    component : WatchList
  },
  {
    path:'/search',
    name:'searchmovie',
    component : SearchMovieView
  },
  {
    path:'/detail',
    name:'detailmovie',
    component : MovieViewCardDetail
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/logout',
    name: 'Logout',
    component: Logout,
  },
  {
    path: '/accounts/profile/:username',
    name: 'Profile',
    component: Profile,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
