import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    // createPersustedState()
  ],
  state: {
    like_movies:null,
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
    GET_USER(state, results) {
      state.user = results
    },
    REMOVE_USER(state) {
      state.user = null
      state.username = null
    },
    GET_LIKE_MOVIE(state,results){
      state.like_movies=results
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
    getLikeMovie(context,user_id){
      const API_URL = 'http://127.0.0.1:8000'

      axios({
        method: 'get',
        url : `${API_URL}/movies/${user_id}/like/`,
      })
      .then((response) => {
        console.log(response.data)
        context.commit("GET_LIKE_MOVIE", response.data)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    getUser(context) {
      const API_URL = 'http://127.0.0.1:8000'
      
      if (localStorage.getItem('username')) {
        const username = localStorage.getItem('username')
        axios({
          method: 'get',
          url : `${API_URL}/accounts/profile/${username}/`,
        })
        .then((response) => {
          console.log(response.data)
          context.commit("GET_USER", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },
  },
  modules: {
  }
})
