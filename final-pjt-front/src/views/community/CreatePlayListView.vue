<template>
  <div>
    <h1>CREATE</h1>
    <form @submit.prevent="createPlaylist">
        <label for="title">제목 : </label>
        <input
            type="text"
            id="title"
            v-model.trim="title"
        ><br>
        <label for="movie_title">영화 제목: </label>
        <input
            type="text"
            id="movie_title"
            v-model.trim="movie_title"
        ><br>
        <label for="rank">평점 : </label>
        <input
            type="number"
            id="rank"
            v-model.trim="rank"
        ><br>
        <label for="content">내용 :</label>
        <textarea
            id="content"
            cols="30" rows="10"
            v-model="content"
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
    name: "CreatePlayListView",
    data() {
        return {
            title: null,
            movie_title: null,
            rank: null,
            content: null,
        }
    },
    methods: {
        createPlaylist() {
            const title = this.title
            const movie_title = this.movie_title
            const rank = this.rank
            const content = this.content

            if (title && movie_title && rank && content) {
                axios({
                    method: 'post',
                    url:`${API_URL}/community/`,
                    data: {title, movie_title, rank, content},
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('jwt')}`
                    }
                })
                .then((res) => {
                    console.log(res)
                })
                .catch((err) => {
                    console.log(err)
                })
            } else{
                alert('입력을 확인하세요.')
            }
        }
    }
}
</script>

<style>

</style>