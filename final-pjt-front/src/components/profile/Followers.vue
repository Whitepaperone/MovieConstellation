<template>
  <div>
    <!-- <p>{{user.id}}</p> -->
    <!-- <p @click="print">components followers.vue user = {{userinfo}}</p>
    <p>components followings = {{user.followings.length}}</p>
    <p>user.id = {{userinfo.id}}</p> -->
    <button @click="getFollowInfo">getfollowinfo</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Followers',
  props: {
    usercomp: Object
  },
  data() {
    return {
    }
  },
  computed: {
    
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
        method: 'post',
        url : `${API_URL}/accounts/${ID}/follow/`,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
      })
      .then((response) => {
        console.log(response.data)
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