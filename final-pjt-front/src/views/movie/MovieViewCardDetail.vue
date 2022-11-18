<template>
<div class="card" style="width: 20rem;">
  {{this.movie}}
      <img :src="poster_path" class="card-img-top" alt="" style="width:17rem; height:25rem; margin-left:22px;">
      <div class="card-body">
        
        <h5 class="card-title"><b>{{ title }}</b></h5>
        <p class="card-text">{{ overview }}</p>
        <router-link :to="{ name : 'detailmovie' }" :movie="movie">[Detail]</router-link>
      </div>
    </div>
</template>

<script>
export default {
name:'MovieViewCardDetail',
props:{
  movie:Object
},
data() {
    return {
      title: this.movie.title,
      overview:this.movie.overview, 
      poster_path:this.movie.poster_path  
    }
  }
}
</script>

<style>

</style>