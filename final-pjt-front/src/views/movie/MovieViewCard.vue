<template>
  <div class="mx-5">
    <div class="card" style="width: 20rem;">
      <img :src="poster_path" class="card-img-top" alt="" style="width:17rem; height:25rem; margin-left:22px;">
      <div class="card-body">
        <h5 class="card-title"><b>{{ title }}</b></h5>
        <p class="card-text">{{ overview }}</p>
        <router-link :to="{ name : 'detailmovie', params: {movie: movie} }" :movie="movie">[Detail]</router-link>
      </div>
    </div>
  </div>
</template>

<script>

import _ from 'lodash'
export default {
  name: 'MovieViewCard',
  props: {
    movie: Object
  },
  data() {
    return {
      poster: 'http://image.tmdb.org/t/p/w185' + this.movie.poster_path,
      title: this.movie.title,
      overview:_.truncate(this.movie.overview,{length:50}), 
      poster_path:this.movie.poster_path  
    }
  }
}
</script>

<style>

</style>