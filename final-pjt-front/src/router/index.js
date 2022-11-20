import Vue from 'vue'
import VueRouter from 'vue-router'

import MovieView from '../views/movie/MovieView.vue'
import RandomView from '../views/movie/RandomView.vue'
import WatchList from '../views/movie/WatchList.vue'
import SearchMovieView from '@/views/movie/SearchMovieView'
import MovieViewCardDetail from '@/views/movie/MovieViewCardDetail'
import TestView from '@/views/movie/TestView'

import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Logout from '@/views/accounts/Logout'
import Profile from '@/views/accounts/Profile'

import PlayListView from '@/views/community/PlayListView'
import CreatePlayListView from '@/views/community/CreatePlayListView'
import PlayListDetailView from '@/views/community/PlayListDetailView'

Vue.use(VueRouter)

const routes = [
  // MOVIE
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
  {
    path:'/search',
    name:'searchmovie',
    component : SearchMovieView
  },
  {
    path:'/:movieId/detail',
    name:'detailmovie',
    component : MovieViewCardDetail,
    props:{newsletterPopup: false}
  },
  
  {
    path:'/combination',
    name:'combinationMovie',
    component : TestView
  },
  {
    path:'/'
  },

  // ACCOUNTS
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

  // COMMUNITY
  {
    path: '/community/',
    name: 'PlayListView',
    component: PlayListView,
  },
  {
    path: '/community/create',
    name: 'CreatePlayList',
    component: CreatePlayListView,
  },
  {
    path: '/community/:id',
    name: 'PlayListDetailView',
    component: PlayListDetailView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
