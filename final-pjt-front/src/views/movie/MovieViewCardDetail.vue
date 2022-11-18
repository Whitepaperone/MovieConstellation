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
      title: this.movie.title,
    }
  },
  methods:{
    getMovie(){
      console.log(this.movie)
      this.movie
    },
  },
  created(){
    this.getMovie()
  },
}
</script>

<style>

</style>