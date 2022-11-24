<template>
  <div>
    <div class="back mx-5">
      <div class="mx-5 pt-3">
        <div class="title mb-3">
          <h1>{{context?.playlist?.title}}</h1>
          <p class="mb-0">{{context?.playlist?.content}}</p>
        </div>
        <div>
          <PlayListMovieVue
            v-for="movie in movies"
            :key="movie.id"
            :movie="movie"
          />
        </div>
      </div>
      
      <div class="d-flex justify-content-center align-items-center">
        <a @click="deletePlaylist" class="btn mt-4 me-5">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16">
            <path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5ZM11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H2.506a.58.58 0 0 0-.01 0H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1h-.995a.59.59 0 0 0-.01 0H11Zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5h9.916Zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47ZM8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5Z"/>
          </svg>
        </a>
        <router-link 
          :to="{
            name : 'UpdatePlayListView',
            params: {id:context?.playlist?.id},
            }"
          class="btn mt-4"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
            <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
            <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
          </svg>
        </router-link>
      </div>
    </div>
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

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');

h1{
  font-family: 'Black Han Sans', sans-serif;
  color: #ffeba7;
  width:auto;
  background-color: #1026708a;
  border-radius: 10px;
  width:fit-content;
  padding-left: 30px;
  padding-right: 30px;
}
p {
  text-align:left;
  padding-left: 20px;
  margin-top: 20px;
  font-size: 24px;
  color:#102670
}
.back {
  background-color: rgba(159, 157, 157, 0.5);
  border-radius: 10px;
}

.title {
  background-color: rgba(226, 226, 226, 0.377);
  border-radius: 10px;
  padding: 20px;
}
.btn {
  border-radius: 4px;
  height: 44px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  padding: 0 30px;
  letter-spacing: 1px;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-align-items: center;
  -moz-align-items: center;
  -ms-align-items: center;
  align-items: center;
  -webkit-justify-content: center;
  -moz-justify-content: center;
  -ms-justify-content: center;
  justify-content: center;
  -ms-flex-pack: center;
  text-align: center;
  border: none;
  background-color: #ffeba7;
  color: #102770;
  box-shadow: 0 8px 24px 0 rgba(255, 235, 167, 0.2);
}
.btn:active,
.btn:focus {
  background-color: #102770;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16, 39, 112, 0.2);
}
.btn:hover {
  background-color: #102770;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16, 39, 112, 0.2);
}
.icon {
  font-size: 32px;
  line-height: 60px;
  color: #102770;
}
</style>