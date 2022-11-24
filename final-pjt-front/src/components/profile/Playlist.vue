<template>
  <div class="back container row justify-content-center my-1 p-3" id="Playlist">
    <div class="p-0 m-0">
      <div>
        <h5 class="playlisttitle px-2 py-1" style="width:fit-content;">{{PL.title}}</h5>
      </div>
    </div>
    <div class="d-flex justify-content-start">
      <PlaylistItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
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
        // console.log(res.data.movies)
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

<style scoped>
.back {
  background-color: rgba(65, 65, 65, 0.832);
  border-radius: 10px;
}
.playlisttitle{
  background-color: rgba(92, 92, 92, 0.758);
  border-radius: 10px;
}
</style>