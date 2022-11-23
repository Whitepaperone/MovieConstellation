<template>
  <div class="container row" id="Playlist">
    <h5>{{PL.title}}</h5>
    <p>{{PL.content}}</p>
    <div class="d-flex justify-content-start">
      <p>영화목록 : </p>
      <PlaylistItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        class="col"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import PlaylistItem from '@/components/profile/PlaylistItem.vue'

export default {
  name: 'ProfilePlaylist',
  components: {
    PlaylistItem,
  },
  props: {
    PL : Object
  },
  data() {
    return {
      movies : [],
    }
  },
  methods: {
    getMovies() {
      const PL_id = this.PL.id
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/community/${PL_id}/`
      })
      .then((res) => {
        console.log(res.data.movies)
        this.movies = res.data.movies
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created() {
    this.getMovies()
  }
}
</script>

<style>

</style>