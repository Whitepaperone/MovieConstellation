<template>
  <div>
    {{playlist}}
    <h3>{{playlist?.title}}</h3>
    <p>{{playlist?.content}}</p>
    <button @click="deletePlaylist">[delete]</button>
    <router-link 
      :to="{
        name : 'UpdatePlayListView',
        params: {id:playlist.id},
        }"
    >
      updatePlaylist
    </router-link>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'PlayListDetailView',
  data() {
    return {
        playlist: null,
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
            this.playlist=res.data
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

<style>

</style>