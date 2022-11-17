<template>
  <div>SearchView
    <input
          v-model="searchValue"
          type="text"
          placeholder="검색할 영화"
          @input="searchMovie" />
    <button @click="searchMovie">+</button>
    <MovieViewCard
      v-for="movie in movies.moviesList"
      :key="movie.id"
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
    movies(){
      return this.movies
    }
  },
 
  methods:{
    searchMovie(){
      let selected={
        'search':'',
      }
      selected.search=this.searchValue
       axios({
          method: 'get',
          url : 'http://127.0.0.1:8000/movies/search/',
          params:{'search':this.searchValue},
        })
        .then((response) => {
          console.log(response.data)
          this.movies=response.data
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