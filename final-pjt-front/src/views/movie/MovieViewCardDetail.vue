<template>
<div>{{getDetail}}</div>
<!-- <div class="card" style="width: 20rem;">
      <img :src="poster_path" class="card-img-top" alt="" style="width:17rem; height:25rem; margin-left:22px;">
      <div class="card-body">
        <h5 class="card-title"><b>{{ title }}</b></h5>
        <p class="card-text">{{ overview }}</p>
        <router-link :to="{ name : 'detailmovie' }" :movie="movie">[Detail]</router-link>
      </div>
    </div> -->
</template>

<script>
export default {
name:'MovieViewCardDetail',
props:{
  movie:Object
},
data() {
    return {
      movie: this.$route.params,
      title: this.movie.title,
      overview:this.movie.overview, 
      poster_path:this.movie.poster_path  
    }
  },
  methods:{
    getDetail(){
      console.log(this.$route.params)
      if (this.movie){
        console.log(this.movie)
      }
      else{
        console.log(this.movie)
      }
    }
  }
}
</script>

<style>

</style>