<template>
  <div>
    <div class="form-group has-search">
      <span class="fa fa-search form-control-feedback"></span>
      <input @input="searchMovie" type="text" class="form-control" placeholder="Search">
    </div>
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

<style lang="scss" scoped>
.main {
    width: 50%;
    margin: 50px auto;
}

/* Bootstrap 4 text input with search icon */

.has-search .form-control {
    padding-left: 2.375rem;
}

.has-search .form-control-feedback {
    position: absolute;
    z-index: 2;
    display: block;
    width: 2.375rem;
    height: 2.375rem;
    line-height: 2.375rem;
    text-align: center;
    pointer-events: none;
    color: #aaa;
}
</style>