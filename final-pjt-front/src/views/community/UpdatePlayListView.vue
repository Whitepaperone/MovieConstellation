<template>
  <div>
    {{playlist}}
    <form @submit.prevent="updatePlaylist">
          <label for="title">제목 : </label>
          <input
              type="text"
              id="title"
              v-model="playlist.title"
          ><br>
          <label for="content">내용 :</label>
          <textarea
              id="content"
              cols="30" rows="10"
              v-model="playlist.content"
          >
          </textarea><br>
          <input type="submit" id="submit">
      </form>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'UpdatePlayListView',
    data() {
        return {
            playlist: null,
        }
    },
    methods: {
        getPlaylistInfo() {
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
            .catch(err => console.log(err.data))
        },
        updatePlaylist() {
            const title = this.playlist.title
            const content = this.playlist.content
  
            if (title && content) {
                axios({
                    method: 'put',
                    url: `${API_URL}/community/${this.$route.params.id}/`,
                    data: {title, content},
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('jwt')}`
                    }
                })
                .then((res) => {
                    console.log(res)
                    this.$router.push({name: 'PlayListDetailView', id: this.playlist.id})
                })
                .catch((err) => {
                    console.log(err)
                })
            } else{
                alert('입력을 확인하세요.')
            }
        }
        
    },
    created() {
        this.getPlaylistInfo()
    }
   
}
</script>

<style>

</style>