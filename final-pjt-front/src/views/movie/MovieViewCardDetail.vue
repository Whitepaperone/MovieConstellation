<template>
<div>{{getMovieDetail}}
  <button @click="likeMovie">+</button>
</div>
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
import axios from 'axios'
export default {
name:'MovieViewCardDetail',
data(){
  return{
    movie:null,
  }
},
computed:{
  getMovieDetail(){
    return this.movie
  }
},
  methods:{
    getMovie(){
      this.movie=this.$route.params.movieId
      console.log(this.movie)
       axios({
          method: 'get',
          url : `http://127.0.0.1:8000/movies/${this.movie}/`,
        })
        .then((response) => {
          console.log(response.data)
          this.movie=response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    likeMovie(){
      const isConsistent=this.movie.like_users.some((user)=>{return user===this.$store.state.user.id})
      if (isConsistent){
        const newUsers=this.movie.like_users.filter((user)=>{return user!==this.$store.state.user.id})
        axios({
                method: 'put',
                url: `http://127.0.0.1:8000/movies/${this.movie.id}/update/`,
                data:{
                  id:this.movie.id,
                  title:this.movie.title,
                  release_date:this.movie.release_date,
                  popularity:this.movie.popularity,
                  vote_count:this.movie.vote_count,
                  vote_average:this.movie.vote_average,
                  overview:this.movie.overview,
                  poster_path:this.movie.poster_path,
                  genres:this.movie.genres,
                  like_users: newUsers
                  }
              })
              .then((res)=>{
                console.log(res)
              })
              .catch((err)=>console.log(err))
      }
      else{
        this.movie.like_users.push(this.$store.state.user.id)
        axios({
                method: 'put',
                url: `http://127.0.0.1:8000/movies/${this.movie.id}/update/`,
                data:{
                  id:this.movie.id,
                  title:this.movie.title,
                  release_date:this.movie.release_date,
                  popularity:this.movie.popularity,
                  vote_count:this.movie.vote_count,
                  vote_average:this.movie.vote_average,
                  overview:this.movie.overview,
                  poster_path:this.movie.poster_path,
                  genres:this.movie.genres,

                  like_users: this.movie.like_users
                  }
              })
              .then((res)=>{
                console.log(res)
              })
              .catch((err)=>console.log(err))
      }
     
    },
    },
  created(){
    this.getMovie()
  },
}
</script>

<style>

</style>