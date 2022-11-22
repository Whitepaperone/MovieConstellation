<template>
    <div>
      <h1>CREATE</h1>
      <form @submit.prevent="createPlaylist">
          <label for="title">제목 : </label>
          <input
              type="text"
              id="title"
              v-model.trim="title"
          ><br>
          <SearchMovieView/>
          <label for="content">내용 :</label>
          <textarea
              id="content"
              cols="30" rows="10"
              v-model="content"
          >
          </textarea><br>
          <input type="submit" id="submit">
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import SearchMovieView from '../movie/SearchMovieView.vue';
  const API_URL = 'http://127.0.0.1:8000'
  
  export default {
      name: "CreatePlayListView",
      data() {
          return {
              title: null,
              content: null,
              movies: [],
          }
      },
      components:{
        SearchMovieView
      },
      methods: {
          createPlaylist() {
              const title = this.title
              const content = this.content
              const movies = this.$store.state.selected_movies
                console.log(movies)
              if (title && content) {
                  axios({
                      method: 'post',
                      url:`${API_URL}/community/`,
                      data: {title, content, movies},
                      headers: {
                          Authorization: `Bearer ${localStorage.getItem('jwt')}`
                      }
                  })
                  .then((res) => {
                      console.log(res)
                      this.$store.dispatch('updateSeletedMovies',[])
                      console.log(this.$store.state.selected_movies)
                      this.$router.push({name: 'PlayListView'})
                  })
                  .catch((err) => {
                      console.log(err)
                  })
              } else{
                  alert('입력을 확인하세요.')
              }
          }
      }
  }
  </script>
  
  <style>
  
  </style>