<template>
  <div>
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

<style>

</style>