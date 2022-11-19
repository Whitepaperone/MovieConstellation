<template>
  <div>
    <h1>Movie Select</h1>
    <router-link :to="{name: 'CreatePlayList'}">
      [CREATE]
    </router-link>
    <hr>
    
  </div>
</template>

<script>
import PlayListList from '@/components/playlist/PlayListList.vue'
import axios from 'axios';

export default {
name: 'PlayListView',
components: {
  PlayListList,
}, 
methods: {
  getPlayListList() {
    const API_URL = 'http://127.0.0.1:8000'
    if (localStorage.getItem('jwt')) {
      axios({
        method: 'get',
        url: `${API_URL}/community/`,
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
    } else {
      alert('로그인이 필요합니다.')
      this.$router.push({name: 'Login'})
    } 
  },
},
created() {
  this.getPlayListList()
}
}
</script>

<style>

</style>