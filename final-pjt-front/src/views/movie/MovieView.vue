<template>
  <div class="row row-cols-1 row-cols-md-4 g-4" style="margin-left:150px">
    <MovieViewCard
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieViewCard from '@/views/movie/MovieViewCard'

export default {
  name: 'MovieView',
  components: {
    MovieViewCard,
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
  }
}
</script>

<style>
</style>