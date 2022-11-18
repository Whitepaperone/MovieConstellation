<template>
  <div>SearchView
    <input
          v-model="searchValue"
          type="text"
          placeholder="검색할 영화"
          @input="searchMovie" />
    <button @click="searchMovie">+</button>
    <MovieViewCard
      v-for="movie in search_movies"
      :key="movie.title"
      :movie="movie"
    />
    </div>
</template>

<script>
import axios from 'axios'
import MovieViewCard from '@/views/movie/MovieViewCard'

export default {
  name: 'SearchView',
  components: {
    MovieViewCard,
  },
  data(){
    return{
      movies:[]
    }
  },
  computed:{
    search_movies(){
      return this.movies.moviesList
    }
  },
 
  methods:{
    searchMovie(){
       axios({
          method: 'get',
          url : 'http://127.0.0.1:8000/movies/search/',
          params:{'search':this.searchValue},
        })
        .then((response) => {
          console.log(response.data)
          this.movies=response.data
          this.movies.sort
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}

</script>

<style>

</style>