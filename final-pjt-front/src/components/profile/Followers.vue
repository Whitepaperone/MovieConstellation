<template>
  <div>
    <!-- <p>{{user.id}}</p> -->
    <!-- <p @click="print">components followers.vue user = {{userinfo}}</p>
    <p>components followings = {{user.followings.length}}</p>
    <p>user.id = {{userinfo.id}}</p> -->
    <button @click="getFollowInfo">getfollowinfo</button>
    <FollowList
      v-for="follow in followings"
      :key="follow.username"
      :follow="follow"
    />
    <FollowList
      v-for="follow in followers"
      :key="follow.username"
      :follow="follow"
    />
  </div>
</template>

<script>
import axios from 'axios'
import FollowList from '@/components/profile/FollowList'

export default {
  name: 'Followers',
  props: {
    usercomp: Object
  },
  components:{
    FollowList,
  },
  data() {
    return {
      followings:null,
      followers:null
    }
  },
  computed: {
    follow(){
      return followObj={
        'followings':this.followings,'followers':this.followers}
    },
  },
  methods: {
    print() {
      console.log(this.user)
    }, 
    getFollowInfo() {
      const API_URL = 'http://127.0.0.1:8000'
      const ID = this.usercomp?.id
      console.log(ID)
      console.log(typeof(ID))
      axios({
        method: 'get',
        url : `${API_URL}/accounts/${ID}/follow/`,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
      .then((response) => {
        console.log(response.data)
        this.followings=response.data.followings
        this.followers=response.data.followers
      })
      .catch((error) => {
        console.log(error.response.data)
      })
    },

  }

}
</script>

<style>

</style>