<template>
  <div class="mx-5">
    <div @click="selectMovie" class="card" style="width: 20rem;">
      <img :src="imgSrc" v-if="imgSrc" class="card-img-top" alt="" style="width:17rem; height:25rem; margin-left:22px;">
      <div class="card-body" :class="{'is-selectd' : this.isSelected }" >
        <h5 class="card-title"><b>{{ title }}</b></h5>
        <p class="card-text">{{ overview }}</p>
        <router-link :to="{ name : 'detailmovie', params: { movieId: movies.id} }">[Detail]</router-link>
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
      title: this.movie.title,
      overview:_.truncate(this.movie.overview,{length:50}), 
      poster_path:this.movie.poster_path,
      movies: this.movie,
      isSelected:false
    }
  },
  computed:{
    imgSrc(){
      return "https://image.tmdb.org/t/p/w500"+this.movie.poster_path
    }
  },
  methods:{
    selectMovie(){
      
      let isConsistent=this.$store.state.selected_movies.indexOf(this.movies.id)
      
      if (isConsistent>=0){
        var newMovies=this.$store.state.selected_movies.filter((movie)=>{return movie!=this.movies.id})
        this.isSelected=false}
      else{
        var newMovies=[...this.$store.state.selected_movies,this.movie.id]
        this.isSelected=true
      }
      console.log('getSelected clicked', this.isSelected)
      this.$store.dispatch('updateSeletedMovies',newMovies)
    }
  }
}
</script>

<style>
.is-selected {
    background-color: aqua;
  }
</style>