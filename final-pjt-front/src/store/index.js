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
          url : 'https://api.themoviedb.org/3/movie/top_rated',
          params: {
            api_key: process.env.VUE_APP_API,
            language: 'ko-KR',
            page: 1,
          }
        })
        .then((response) => {
          context.commit("GET_MOVIE", response.data.results)
        })
        .catch((error) => {
          console.log(error)
        })
      },
  },
  modules: {
  }
})
