<template>
  <div class="back row justify-content-center">
    <div class="m-0 p-0">
      <div class="lititle d-flex justify-content-start mb-3">
        <span>
          <h1 class="px-2 m-2" style="padding-top:6px; padding-bottom:4px; width: fit-content;">My Playlist</h1>
        </span>
        <span class="ms-3">
          <router-link :to="{name: 'CreatePlayList'}">
            <i class="icon bi bi-pencil"></i>
          </router-link>
        </span>
      </div>
    </div>
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

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');
h1 {
  font-family: 'Black Han Sans', sans-serif;
  color: #ffeba7;
  width:auto;
  background-color: #1026708a;
  border-radius: 10px;
}
.back {
  background-color: rgba(159, 157, 157, 0.5);
  border-radius: 10px;
}
.icon {
  font-size: 32px;
  line-height: 60px;
  color: #ffeba7;
}
</style>