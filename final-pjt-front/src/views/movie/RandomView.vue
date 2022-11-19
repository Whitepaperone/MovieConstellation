<template>
  <div class="" style="margin-top:20px;">
    <button type="button" class="btn btn-success" style="margin-bottom:10px; width:32rem"  @click="randomPick()" >next</button> <br>
    <div class="card mx-auto" style="width: 32rem;">
      <img :src="poster" alt="" style="width:31rem; margin: 7px">
      <div class="card-body">
        <h5 class="card-title"> <b>{{ title }}</b></h5>
      </div>
    </div>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.11/lodash.min.js"></script>
<script>
import _ from 'lodash'
  
export default {
  name:'RandomView',
  data(){
    return {
      poster: '',
      title: '',
      number: 0,
    }
  },
  computed: {
    // movies() {
    //   return this.$store.state.movies
    // }
    movies(){
      return this.$store.state.recommend_movies_genre
    }
  },
  methods:{
    randomPick(){
      // console.log(this.movies.length)
      // this.number = Math.floor(Math.random() * this.movies.length);
      this.poster = 'http://image.tmdb.org/t/p/w185' + this.movies[this.number].poster_path,
      this.title = this.movies[this.number].title
      this.number = this.number+1
    },
    
  },
  // watch: {
  //   movies : 'randomPick',
  // },
  created(){
    console.log('created random')
    this.$store.dispatch('recommendWithGenre',this.$store.state.user.id)
    this.randomPick()
  }

}
</script>

<style>

</style>  