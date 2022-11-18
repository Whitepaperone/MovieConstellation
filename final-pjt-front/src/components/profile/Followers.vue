<template>
  <div>
    <p @click="print">components followers.vue user = {{user}}</p>
    <p>components followings = {{user.followings.length}}</p>
    <p>user.id = {{this.user.id}}</p>
    <button @click="getFollowInfo">getfollowinfo</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Followers',
  // props: {
  //   user: Object
  // },
  data() {
    return {
      userinfo : this.user
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  methods: {
    print() {
      console.log(this.user)
    }, 
    // getFollowInfo() {
    //   const API_URL = 'http://127.0.0.1:8000'

    //   axios({
    //     method: 'get',
    //     url : `${API_URL}/${this.userinfo.id}/follow`,
    //   })
    //   .then((response) => {
    //     console.log(response.data)
    //   })
    //   .catch((error) => {
    //     console.log(error)
    //   })
    // },

  }

}
</script>

<style>

</style>