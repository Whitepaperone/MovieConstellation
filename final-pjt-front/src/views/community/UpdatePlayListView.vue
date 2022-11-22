<template>
  <div>
    {{context.playlist}}
    <form @submit.prevent="updatePlaylist">
          <label for="title">제목 : </label>
          <input
              type="text"
              id="title"
              v-model="context.playlist.title"
          ><br>
          <SearchMovieView/>
          <label for="content">내용 :</label>
          <textarea
              id="content"
              cols="30" rows="10"
              v-model="context.playlist.content"
          >
          </textarea><br>
          <input type="submit" id="submit">
      </form>
  </div>
</template>

<script>
import axios from 'axios';
import SearchMovieView from '../movie/SearchMovieView.vue';
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'UpdatePlayListView',
    data() {
        return {
            context: null,
        }
    },
    components:{
        SearchMovieView
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
                console.log(res.data)
                this.context=res.data
            })
            .catch(err => console.log(err.data))
        },
        updatePlaylist() {
            const title = this.context.playlist.title
            const content = this.context.playlist.content
            const movies = this.$store.state.selected_movies
            if (title && content) {
                axios({
                    method: 'put',
                    url: `${API_URL}/community/${this.$route.params.id}/`,
                    data: {title, content, movies},
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('jwt')}`
                    }
                })
                .then((res) => {
                    console.log(res)
                    this.$router.push({name: 'PlayListDetailView', id: this.context.playlist.id})
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