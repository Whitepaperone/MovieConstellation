<template>
  <div class="container row mx-auto">
    최신영화
    <div class="col">
        <MovieNowPlaying  />
    </div>
    랭킹영화
    <transition-group 
      ref="main" class="main col">
      
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

<style>
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