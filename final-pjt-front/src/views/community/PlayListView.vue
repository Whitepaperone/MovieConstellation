<template>
  <div>
    
    <h1>My Playlist</h1>
    <router-link :to="{name: 'CreatePlayList'}">
      플레이 리스트 만들기
    </router-link>
    <hr>
    <PlayListListVue/>
  </div>
</template>

<script>
import PlayListListVue from '@/components/playlist/PlayListList.vue'

export default {
name: 'PlayListView',
components: {
  PlayListListVue,
}, 
methods: {
  getPlayListList() {
    if (localStorage.getItem('jwt')) {
      this.$store.dispatch('getPlayList')
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