<template>
  <div>
    <div>
      <div>
        <h1>{{context?.playlist?.title}}</h1>
        <p>{{context?.playlist?.content}}</p>
      </div>
      <div>
        <PlayListMovieVue
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>

    <button @click="deletePlaylist">[delete]</button>
    <router-link 
      :to="{
        name : 'UpdatePlayListView',
        params: {id:context?.playlist.id},
        }"
    >
      updatePlaylist
    </router-link>
  </div>
</template>

<script>
import axios from 'axios';
import PlayListMovieVue from '@/components/playlist/PlayListMovie.vue';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'PlayListDetailView',
  components: {
    PlayListMovieVue
  },
  data() {
    return {
        context: null,
        movies: null,
    }
  },
  methods: {
    getPlaylistDetail() {
        axios({
            method: 'get',
            url: `${API_URL}/community/${this.$route.params.id}/`,
            headers: {
                Authorization: `Bearer ${localStorage.getItem('jwt')}`
            }
        })
        .then((res) => {
          // console.log(res.data)
          this.context=res.data
          this.movies=res.data.movies
        })
        .catch(err => console.log(err))
    },
    deletePlaylist() {
        axios({
            method: 'DELETE',
            url: `${API_URL}/community/${this.$route.params.id}/`,
            headers: {
                Authorization: `Bearer ${localStorage.getItem('jwt')}`
            }
        })
        .then(() => {
            this.$router.push({name: 'PlayListView'})
        })
        .catch(err => console.log(err))
    }
  },
  created() {
    this.getPlaylistDetail()
  }
}
</script>

<style scoped>
div {
border:#c54b30 solid 1px;
}
span {
border:#f6ff00 solid 1px;
}
</style>