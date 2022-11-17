import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: null,
    user: null,
    username: null,
    picked: [],
  },
  getters: {

  },
  mutations: {
    GET_MOVIE(state, results) {
      state.movies = results
    },
    GET_USERNAME(state, username) {
      state.username = username
    },
    GET_USER(state, results) {
      state.user = results
    },
    REMOVE_USER(state) {
      state.user = null
      state.username = null
    }
  },
  actions: {
    getMovie(context) {
      const API_URL = 'http://127.0.0.1:8000'

      axios({
        method: 'get',
        url : `${API_URL}/movies/`,
      })
      .then((response) => {
        // console.log(response.data)
        context.commit("GET_MOVIE", response.data)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    getUserName(context) {
      let username = ''
      if (localStorage.getItem('username')!==null) {
        username = localStorage.getItem('username')
      }
      context.commit("GET_USERNAME", username)
    },
    getUser(context, payload) {
      const API_URL = 'http://127.0.0.1:8000'
      // const username = context.state.username

      axios({
        method: 'get',
        url : `${API_URL}/accounts/profile/${payload.username}/`,
      })
      .then((response) => {
        // console.log(response.data)
        context.commit("GET_USER", response.data)
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  modules: {
  }
})
