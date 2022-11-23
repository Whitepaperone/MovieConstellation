<template>
  <div >
      <transition-group ref="main"  >
    <MovieViewCard
    ref="box" class="box"
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
    
  </transition-group>
  </div>
</template>

<script>
import MovieViewCard from '@/views/movie/MovieViewCard'

import axios from 'axios'

export default {
  name: 'MoieNowPlaying',
  components: {
    MovieViewCard,
  },
  data() {
    return {
      movies: [],
    }
  },
  methods:{
    onGetVideo(){
      axios({
        method:'get',
        url: 'https://api.themoviedb.org/3/movie/now_playing?api_key=5db6b281cedd2e443755d865852e5bba',
        params:{
          api_key:process.env.VUE_APP_TMDP_API_KEY,
          language:"ko",
        }
      })
        .then((res) => {
          this.movies = res.data.results
        })
        .catch((error) => {console.log(error)})
    }
  },
  created(){
    this.onGetVideo()
  }
}
</script>


<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
/* #rl1 {
  float: right;
} */
/* nav {
  padding: 30px;
} */

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin: 20px;
}

nav a.router-link-exact-active {
  color: #42b983;
}

/* #divTag {
  float: right;
} */
nav{
  background-color: skyblue;
}
</style>
