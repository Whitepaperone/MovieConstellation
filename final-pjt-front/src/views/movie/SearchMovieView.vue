<template>
  <div>SearchView
    <input
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
      return this.movies.movies
    }
  },
 
  methods:{
    searchMovie:function(event){
       axios({
          method: 'get',
          url : 'http://127.0.0.1:8000/movies/search/',
          params:{'search':event.target.value},
        })
        .then((response) => {
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