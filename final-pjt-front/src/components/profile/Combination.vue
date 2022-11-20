<template>
  <div class="row row-cols-1 row-cols-md-4 g-4" style="margin-left:150px">
    <MovieViewCard
      v-for="movie in movies.intersection"
      :key="movie.id"
      :movie="movie"
    />
    <hr><hr><hr><br>
    <MovieViewCard
      v-for="movie in movies.a_complement"
      :key="movie.id"
      :movie="movie"
    />
    
    <hr><hr><hr><br>
    <MovieViewCard
      v-for="movie in movies.b_complement"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieViewCard from '@/views/movie/MovieViewCard'
import axios from 'axios'
export default {
  name: 'TestView',
  components: {
    MovieViewCard,
  },
  props:{
    comuser:Object
  },
  data(){
    return{
      movies:[],
      number:1
    }
  },
 
  methods:{
    combinationMovie(){
      const user_id=this.comuser.a
      const another_user_id=this.comuser.b

      console.log(another_user_id,user_id)
       axios({
          method: 'get',
          url : `http://127.0.0.1:8000/movies/${user_id}/combination/${another_user_id}`,

        })
        .then((response) => {
          console.log(response.data)
          this.movies=response.data
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created(){
    this.combinationMovie()
  }
}
</script>

<style>

</style>