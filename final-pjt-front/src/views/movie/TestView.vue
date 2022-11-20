<template>
  <div class="row row-cols-1 row-cols-md-4 g-4" style="margin-left:150px">
    {{movies.intersection}}
    <hr>
    {{movies.a_complement}}
    <hr>
    {{movies.b_complement}}
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
  data(){
    return{
      movies:[],
      number:1
    }
  },
 
  methods:{
    combinationMovie:function(event){
      const user_id=1
      const another_user_id=2
      if (another_user_id===user_id){
        another_user_id=1
      }
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