<template>
 
  <!-- <div class="card" style="margin:20px; width: 22rem"  >
    <div @click="selectMovie" class="row mx-auto justify-content-center" :class="{'is-selectd' : this.isSelected }" style="width: 20rem; ">
      <img :src="imgSrc" v-if="imgSrc" class="card-img-top" alt="" style="width:17rem; height:25rem; margin-top:1rem ;">
      <div class="card-body row"  >
        <h5 class="card-title"><b>{{ title }}</b></h5><br>
        <p class="card-text">{{ overview }}</p>
        <router-link :to="{ name : 'detailmovie', params: { movieId: movies.id} }">[Detail]</router-link>
      </div>
    </div> -->
    <div>
      <div id="movie-card-list">
        <div class="movie-card" :style="{'background-image': 'url('+this.poster_path+')'}">
          <div class="movie-card__overlay"></div>
          <div class="movie-card__share"></div>
          <div class="movie-card__content">
            <div class="movie-card__header mx-auto">
              <h1 class="movie-card__title">{{title}}</h1>
              <h4 class="movie-card__info">{{this.movie.vote_average}}</h4>
              </div>
              <p class="movie-card__desc">{{overview}}</p>
              <button v-if="!(this.movie.backdrop_path)" class="btn btn-outline movie-card__button" type="button"><router-link class="router-link" :to="{ name : 'detailmovie', params: { movieId: movies.id} }">Detail</router-link></button>
          </div>
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
      genre: null,
      overview:_.truncate(this.movie.overview,{length:50}), 
      poster_path:this.movie.poster_path,
      movies: this.movie,
      isSelected:false
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
    },
    imgSrc(){
      if (this.movie.backdrop_path){
        console.log(this.movie.backdrop_path)
        this.poster_path="https://image.tmdb.org/t/p/w500"+this.movie.backdrop_path
      }
      else{
        console.log(this.movie.poster_path)
        this.poster_path="https://image.tmdb.org/t/p/w500"+this.movie.poster_path
      }
    },
  },
    created(){
      this.imgSrc()
    }
}
</script>

<style>
  .router-link{
    color:white;
    text-decoration:none;
  }
  .card{
    opacity: 80%;
  }
  .is-selected {
    background-color: rgb(168, 184, 153) !important;
  }
rotuer-link{
  color:#ffffff !important;
}

@import url("https://fonts.googleapis.com/css?family=Montserrat:300,400,700,800");
html {
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: inherit;
}

html,
body {
  width: 100%;
  height: 100%;
}

body {
  background-color: #dce1e5;
  font-family: "Montserrat", helvetica, arial, sans-serif;
  font-size: 14px;
  color: #cfd6e1;
  line-height: 1.5;
  font-weight: 400;
  overflow-x: hidden;
}

* {
  transition: 0.4s;
}

a {
  text-decoration: none;
}

button {
  font-family: inherit;
  border: 0;
  cursor: pointer;
}
button:focus {
  outline: 0;
}
.movie-card-list{
  height:auto;
}
.movie-card {
  background-size: contain;
  background-repeat: no-repeat;
  width: 100%;
  max-width: 800px;
  height: auto;
  min-height: 300px;
  display: inline-block;
  margin: 8vh auto;
  border-radius: 8px;
  box-shadow: 0px 8px 12px 0px rgba(0, 0, 0, 0.25);
  position: relative;
}
@media screen and (max-width: 800px) {
  .movie-card {
    width: 95%;
    max-width: 95%;
  }
}
@media screen and (max-width: 600px) {
  .movie-card {
    background-position: 50% 0%;
    background-size: cover;
    height: auto;
  }
}
.movie-card[data-movie="Blade Runner"] {
  background-image: url(http://digitalspyuk.cdnds.net/15/47/1600x800/landscape-1447754794-harrison-ford-blade-runner.jpg);
}
.movie-card[data-movie="Back to the Future"] {
  background-image: url("http://www.blastr.com/sites/blastr/files/back-to-the-future-part-ii-original.jpg");
}
.movie-card[data-movie=Akira] {
  background-image: url("https://static1.squarespace.com/static/51b3dc8ee4b051b96ceb10de/t/58d86b3db3db2b57ce8f2986/1490578241899/?format=2500w");
}
.movie-card__overlay {
  width: 100%;
  height: auto;
  border-radius: 8px;
  background: linear-gradient(to right, rgba(42, 159, 255, 0.2) 0%, #212120 60%, #212120 100%);
  background-blend-mode: multiply;
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
}
@media screen and (max-width: 600px) {
  .movie-card__overlay {
    background: linear-gradient(to bottom, rgba(42, 159, 255, 0.2) 0%, #212120 60%, #212120 100%);
  }
}
.movie-card__share {
  padding: 1em;
  display: inline-block;
  width: 100%;
  max-width: 130px;
}
@media screen and (max-width: 600px) {
  .movie-card__share {
    display: block;
    width: 100%;
  }
}
.movie-card__icon {
  color: #ffffff !important;
  mix-blend-mode: lighten;
  opacity: 0.4;
  background: none;
  padding: 0;
}
.movie-card__icon:hover {
  opacity: 1;
  mix-blend-mode: lighten;
}
.movie-card__icon:not(:first-of-type) {
  margin-left: 5px;
}
.movie-card__icon i {
  font-size: 1.2em;
}
.movie-card__content {
  width: 100%;
  max-width: 370px;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  position: relative;
  float: right;
  padding-right: 1.2em;
  padding-bottom: 1em;
}
@media screen and (max-width: 1000px) {
  .movie-card__content {
    width: 50%;
  }
}
@media screen and (max-width: 600px) {
  .movie-card__content {
    margin-top: 4.2em;
    width: 100%;
    float: inherit;
    max-width: 100%;
    padding: 0 1em 1em;
    
  }
}
.movie-card__header {
  margin-bottom: 2em;
}
.movie-card__title {
  color: #ffffff ;
  margin-top: 20px;
  margin-bottom: 0.25em;
  opacity: 0.75;
}
.movie-card__info {
  text-transform: uppercase;
  letter-spacing: 2px;
  font-size: 0.8em;
  color: #2a9fff;
  line-height: 1;
  margin: 0;
  font-weight: 700;
  opacity: 0.5;
}
.movie-card__desc {
  color: #cfd6e1;
  font-weight: 300;
  opacity: 0.84;
  margin-bottom: 2em;
}

h1,
h2,
h3 {
  font-family: "Montserrat", helvetica, arial, sans-serif;
  text-transform: uppercase;
  letter-spacing: 2px;
  line-height: 1;
  font-weight: 400;
}

.btn {
  padding: 0.5rem 2rem;
  background-color: rgba(255, 255, 255, 0.4);
  color: white !important;
}

.btn-outline {
  background-color: transparent;
  border: 3px solid #ffffff !important;
}

.btn::before {
  content: "◈";
  vertical-align: middle;
  font-size: 1.5em;
  padding-right: 0.5em;
}

.btn-outline:hover {
  border-color: #2a9fff;
  color: #2a9fff;
  box-shadow: 0px 1px 8px 0px rgba(245, 199, 0, 0.2);
}
</style>