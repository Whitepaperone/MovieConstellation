import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: null,
    picked: [],
  },
  getters: {

  },
  mutations: {
    GET_MOVIE(state, results) {
        state.movies = results
    }
  },
  actions: {
    getMovie(context) {
        axios({
          method: 'get',
          url : 'http://127.0.0.1:8000/movies/',
         
        })
        .then((response) => {
          console.log(response.data)
          context.commit("GET_MOVIE", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
      },
  },
  modules: {
  }
})
