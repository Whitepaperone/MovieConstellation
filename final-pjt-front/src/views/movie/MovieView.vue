<template>
  <div class="row row-cols-1 row-cols-md-4 g-4" style="margin-left:150px">
    <div>
      <button v-on:click="show=!show">변경하기</button>
      <transition-group
      ref="main" class="main">
         <MovieViewCard
         ref="box"
         class="box"
            v-for="movie in movies"
            :key="movie.id"
            :movie="movie"
          />
      </transition-group>
    </div>

   
    <br><hr>
    <MovieNowPlaying/>
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

    this.$refs.box.forEach(box => {
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