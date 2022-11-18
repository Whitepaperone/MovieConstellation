<template>
  <div class="" style="margin-top:20px;">
    <button type="button" class="btn btn-success" style="margin-bottom:10px; width:32rem"  @click="randomPick()" >pick</button> <br>
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
    movies() {
      return this.$store.state.movies
    }
  },
  methods:{
    randomPick(){
      console.log('clicked pick')
      // this.number = Math.floor(Math.random() * this.movies.length);
      this.number = _.sampleSize(_.range(0,this.movies.length),1)
      this.poster = 'http://image.tmdb.org/t/p/w185' + this.movies[this.number].poster_path,
      this.title = this.movies[this.number].title
    },
  },
  watch: {
    movies : 'randomPick',
  },
  created(){
    console.log('created random')
    this.randomPick()
  }

}
</script>

<style>

</style>  