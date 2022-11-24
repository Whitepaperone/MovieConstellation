<template>
<div>
  <div class="moviecard">
    
  <div class="movie-poster play-trailer" @click="likeMovie" :style="{'background-image': 'url('+this.movie.movie?.poster_path+')'}"></div>
  <div id="movie-content">
    <div class="movie-title">{{movie.movie?.title}}<span class="movie-year">{{movie.movie?.release_date}}</span></div>
    <div class="movie-details"><span class="movie-genre"  v-for="genre in movie.genre" :key="genre.id">{{genre}}</span></div>
    <div class="movie-castcrew"><span class="star">★</span><span class="score">{{movie.movie?.vote_average}}</span><span class="score-out-of">/ 10 (TMDB)</span></div></div>
    <div class="movie-castcrew"><span class="title">Like</span><span class="name text-animation" v-for="user in movie?.like_user" :key="user.id"> <router-link class="router-link" :to="{ name : 'Profile', params: { username: user} }">| {{user}} |</router-link> </span></div>
    <div class="movie-synopsis">{{movie.movie?.overview}}</div>
    
    <button class="movie-trailer-btn play-trailer" @click="likeMovie" type="button">Like it</button>
  </div>
  <div class="decode-text">
  	<div class="text-animation" v-for="user in movie?.like_user" :key="user.id">{{user}}
    <div class="space"></div></div>
  </div>
<!-- 
<a id="refresh" onclick="decodeText();">
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M17.65 6.35C16.2 4.9 14.21 4 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
</a> -->

</div>


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
  },
},
  methods:{
    getMovie(){
      this.movie=this.$route.params.movieId
      console.log('getMovie',this.movie)
       axios({
          method: 'get',
          url : `http://127.0.0.1:8000/movies/${this.movie}/`,
        })
        .then((response) => {
          this.movie=response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    likeMovie(){
      console.log('likeMovie',this.movie)
      const isConsistent=this.movie.movie.like_users?.some((user)=>{return user===this.$store.state.user.id})
      if (isConsistent){
        const newUsers=this.movie.movie.like_users.filter((user)=>{return user!==this.$store.state.user.id})

        axios({
                method: 'put',
                url: `http://127.0.0.1:8000/movies/${this.movie.movie.id}/update/`,
                data:{
                  id:this.movie.movie.id,
                  title:this.movie.movie.title,
                  release_date:this.movie.movie.release_date,
                  popularity:this.movie.movie.popularity,
                  vote_count:this.movie.movie.vote_count,
                  vote_average:this.movie.movie.vote_average,
                  poster_path:this.movie.movie.poster_path,
                  genres:this.movie.movie.genres,
                  like_users: newUsers
                  }
              })
              .then((res)=>{
                this.getMovie()
                console.log('unlike',newUsers)
              })
              .catch((err)=>console.log(err))
      }
      else{
        this.movie.movie.like_users?.push(this.$store.state.user.id)
        axios({
                method: 'put',
                url: `http://127.0.0.1:8000/movies/${this.movie.movie.id}/update/`,
                data:{
                  id:this.movie.movie.id,
                  title:this.movie.movie.title,
                  release_date:this.movie.movie.release_date,
                  popularity:this.movie.movie.popularity,
                  vote_count:this.movie.movie.vote_count,
                  vote_average:this.movie.movie.vote_average,
                  poster_path:this.movie.movie.poster_path,
                  genres:this.movie.movie.genres,
                  like_users: this.movie.movie.like_users
                  }
              })
              .then((res)=>{
                console.log('like==========',this.movie.like_users)
                this.getMovie()
              })
              .catch((err)=>console.log(err))
        }
      },
  
    },
  created(){
    this.getMovie()
  },
  mounted(){;
  }
}

/* ------------------------------------------------------------------------ *  
4 states per letter: Transparent | Line | Block | Visible.
These states are shuffled for a unique "decode" effect each time.
* ------------------------------------------------------------------------ */



// send the node for later .state changes



// Demo only stuff


// beware: refresh button can overlap this timer and cause state mixups




</script>

<style scoped>
@charset "UTF-8";
* {
  box-sizing: border-box;
}
.router-link{
    color:#333333;
    text-decoration:none;
  }

.moviecard {
  font-family: "Helvetica", sans-serif, "Ariel";
  position: relative;
  background: #ffffff;
  color: #555555;
  margin: 50px auto;
  width: 850px;
  max-width: 900px;
  min-height: 300px;
  padding: 30px 290px 30px 30px;
  -moz-box-shadow: -5px 5px 15px;
  -webkit-box-shadow: -5px 5px 15px;
  box-shadow: -5px 5px 15px;
  border-radius: 5px;
}
.moviecard #movie-content {
  opacity: 1;
  width: 100%;
  display: table;
  transition: all 500ms ease-out;
  position: relative;
}
.moviecard .movie-title {
  font-size: 36px;
  padding-bottom: 6px;
  color: #333333;
}
.moviecard .movie-title .movie-year {
  margin-left: 12px;
  font-size: 16px;
}
.moviecard .movie-title a {
  color: #333333;
  text-decoration: none;
}
.moviecard .movie-title a:hover {
  color: #858585;
}
.moviecard .movie-details {
  font-size: 12px;
  padding-bottom: 24px;
  margin-bottom: 12px;
  border-bottom: 1px solid #dbdbdb;
}
.moviecard .movie-details span {
  padding: 0px 6px;
  border-right: 1px solid #dbdbdb;
}
.moviecard .movie-details span:last-child {
  border: none;
}
.moviecard .movie-castcrew {
  padding-top: 12px;
  width: 100%;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.moviecard .movie-castcrew span.title {
  color: #333333;
  display: inline-block;
  width: 80px;
  font-weight: 600;
}
.moviecard .movie-synopsis {
  display: inline-block;
  height: auto;
  margin: 24px 0px;
  padding-top: 24px;
  border-top: 1px solid #dbdbdb;
  overflow-y: hidden;
  width: 100%;
}
.moviecard .movie-ratings {
  position: absolute;
  right: 0px;
}
.moviecard .movie-ratings span.star {
  display: inline-block;
  margin-right: 12px;
  color: #F0DE00;
  font-size: 36px;
}
.moviecard .movie-ratings span.score {
  font-size: 30px;
  color: #333333;
}
.moviecard .movie-trailer-btn {
  text-transform: uppercase;
  outline: none;
  padding: 15px 50px;
  position: relative;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
}
.moviecard .movie-trailer-btn:hover {
  text-decoration: underline;
}
.moviecard .movie-trailer-btn:hover:before {
  color: #333333;
}
.moviecard .movie-trailer-btn:hover:after {
  border-color: #333333;
}
.moviecard .movie-trailer-btn:before {
  content: "♥";
  font-size: 30px;
  color: #333333;
  position: absolute;
  top: 2px;
  left: 18px;
  width: 22px;
}
.moviecard .movie-trailer-btn:after {
  content: "";
  width: 20px;
  height: 20px;
  border: 1px solid #333333;
  border-radius: 50%;
  position: absolute;
  left: 18px;
  top: 12px;
}
.moviecard .movie-trailer {
  width: 0px;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  right: 0px;
  height: 100%;
  transition: all 500ms;
  top: 0px;
  background: #ffffff;
  z-index: 1;
  padding: 60px 40px 60px 60px;
  border-radius: 5px;
}
.moviecard .movie-trailer a.back-btn {
  color: #333333;
  text-decoration: none;
  font-weight: 600;
  padding: 6px 12px 6px 18px;
  position: absolute;
  top: 12px;
  left: 300px;
  text-transform: uppercase;
  font-size: 12px;
  cursor: pointer;
}
.moviecard .movie-trailer a.back-btn:before {
  content: "⌜";
  position: absolute;
  left: 5px;
  top: -2px;
  transform: rotate(-45deg);
  font-size: 20px;
  width: 26px;
  height: 26px;
}
.moviecard .movie-trailer a.back-btn:hover {
  color: #333;
}
.moviecard .movie-trailer img {
  width: 100%;
  height: 100%;
}
.moviecard .movie-poster {
  position: absolute;
  background-color: #dbdbdb;
  background-size: 360px 540px;
  background-repeat: no-repeat;
  height: 0;
  width: 360px;
  height: 540px;
  right: -100px;
  top: -20px;
  -moz-box-shadow: -2px 2px 7px rgba(0, 0, 0, 0.6);
  -webkit-box-shadow: -2px 2px 7px rgba(0, 0, 0, 0.6);
  box-shadow: -2px 2px 7px rgba(0, 0, 0, 0.6);
  cursor: pointer;
  transition: all 500ms ease-out;
  z-index: 10;
}
.moviecard .movie-poster:before {
  content: "♥";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 200px;
  color: rgba(255, 255, 255, 0.4);
}
.moviecard .movie-poster:hover:before {
  color: rgba(255, 255, 255, 0.8);
}
.moviecard.movie-view-trailer .movie-poster {
  right: 600px;
}
.moviecard.movie-view-trailer #movie-content {
  opacity: 0;
  width: 0px;
}
.moviecard.movie-view-trailer .movie-trailer {
  width: 100%;
  opacity: 1;
  padding-left: 300px;
}
.moviecard.movie-view-trailer .movie-trailer #youvideo {
  height: 100%;
}





@import url(https://fonts.googleapis.com/css?family=Share+Tech+Mono);
.decode-text {
  width: 100%;
  font-size: 30px;
  text-align: center;
}

.space {
  display: inline-block;
  width: 10px;
}

.text-animation {
  display: inline-block;
  position: relative;
  color: transparent;
  text-transform: uppercase;
}
.text-animation:before {
  content: "";
  color: black;
  position: absolute;
  top: 50%;
  left: 50%;
  background: #0e182d;
  width: 0;
  height: 1.2em;
  -webkit-transform: translate(-50%, -55%);
  -ms-transform: translate(-50%, -55%);
  transform: translate(-50%, -55%);
}
.text-animation.state-1:before {
  width: 1px;
}
.text-animation.state-2:before {
  width: 0.9em;
}
.text-animation.state-3 {
  color: black;
}
.text-animation.state-3:before {
  width: 0;
}

#refresh {
  position: absolute;
  top: 20px;
  left: 20px;
  cursor: pointer;
}

div {
  font-family: "Share Tech Mono", monospace;
}

body {
  height: 100vh;
  align-items: center;
  display: flex;
}
</style>
