<template>
  <div class="moviecard">
    <MovieViewCard
      :movie="moviee"
    />
  </div>
</template>

<script>
import MovieViewCard from '@/views/movie/MovieViewCard.vue'

export default {
  name: 'PlayListMovie',
  components: {
    MovieViewCard,
  },
  props: {
    movie: Object,
  },
  computed: {
    moviee() {
      return this.movie
    }
  }

}
</script>

<style scoped>
.moviecard{
  margin-bottom: 20px;
  background-color: rgba(226, 226, 226, 0.377);
  border-radius: 10px;
}
</style>