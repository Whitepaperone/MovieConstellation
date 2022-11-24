<template>
  <div class="container">
    <div class="movie_div mb-5 row justify-content-center mx-2 p-4">
      <div class="d-flex justify-content-start align-items-center ps-0 mb-3">
        <h1 class="text-center px-2" style="padding-top:6px">최신 영화</h1>
      </div>
      <div class="moviecardzone" style="overflow:scroll; width:900px; height: 480px;">
        <MovieNowPlaying/>
      </div>
    </div>
    <div class="movie_div row justify-content-center mx-2 p-4">
      <div class="d-flex justify-content-start align-items-center ps-0 mb-3">
        <h1 class="text-center px-2" style="padding-top:6px">인기 영화</h1>
      </div>
      <div class="moviecardzone col" style="overflow:scroll; width:900px; height: 480px;">
        <transition-group 
          ref="main" class="main col" >
          
            <MovieViewCard
            ref="box" class="box" 
              v-for="movie in movies"
              :key="movie.id"
              :movie="movie"
            />
          </transition-group>
      </div>
    </div>
  </div>

</template>

<script>
import MovieViewCard from '@/views/movie/MovieViewCard'
import MovieNowPlaying from '@/views/movie/MovieNowPlaying'



export default {
  name: 'MovieView',
  components: {
    MovieViewCard,
    MovieNowPlaying,
  },
  data(){
    return{
      show: true
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
  async mounted() {
    // wait for $refs to be available
    await this.$nextTick()

    this.$refs.box?.forEach(box => {
      box.style.left = Math.random() * (this.$refs.main.clientWidth - box.clientWidth) + 'px'
      box.style.top = Math.random() * (this.$refs.main.clientHeight - box.clientHeight) + 'px'
    })
  },
   methods: {
    randomPos(){}
  }
}
</script>

<style lnag="ssas" scoped>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');
.scrollbar{
  overflow-x:hidden;
}
::-webkit-scrollbar{
  display: none;
}
.movie_div{
  background-color: rgba(159, 157, 157, 0.5);
  border-radius: 10px;
}
.moviecardzone {
  background-color: rgba(226, 226, 226, 0.095);
  border-radius: 10px;
}
h1 {
  font-family: 'Black Han Sans', sans-serif;
  color: rgb(35, 35, 35);
  width:auto;
  background-color: rgba(226, 226, 226, 0.095);
  border-radius: 10px;
}
.v-enter-active, .v-leave-active, .v-move {
  transition: opacity 1s, transform 1s;
}
.v-leave-active {
  position: absolute;
}
.v-enter {
  opacity: 0;
  transform: translateY(-20px);
}
.v-leave-to {
  opacity: 0;
  transform: translateY(20px);
}
</style>