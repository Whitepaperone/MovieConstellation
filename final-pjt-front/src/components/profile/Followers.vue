<template>
  <div>
    <!-- <p>{{user.id}}</p> -->
    <!-- <p @click="print">components followers.vue user = {{userinfo}}</p>
    <p>components followings = {{user.followings.length}}</p>
    <p>user.id = {{userinfo.id}}</p> -->
    {{usercomp}}
    

    <!-- <button @click="getFollowInfo">getfollowinfo</button> -->
    <!-- <FollowListItem
      v-for="follow in followings"
      :key="follow.username"
      :follow="follow"
    />
    <FollowListItem
      v-for="follow in followers"
      :key="follow.username"
      :follow="follow"
    /> -->
  </div>
</template>

<script>
import axios from 'axios'
import FollowListItem from '@/components/profile/FollowListItem'

export default {
  name: 'Followers',
  props: {
    usercomp: Object
  },
  components:{
    FollowListItem,
  },
  data() {
    return {
      // follow_info : null,
    }
  },
  computed: {
    // follow(){
    //   return followObj={
    //     'followings':this.followings,'followers':this.followers}
    // },
  },
  methods: {
    // print() {
    //   console.log(this.user)
    // }, 
    // getFollowInfo() {
    //   const API_URL = 'http://127.0.0.1:8000'
    //   const ID = this.usercomp?.id
    //   console.log(ID)
    //   console.log(typeof(ID))
    //   axios({
    //     method: 'get',
    //     url : `${API_URL}/accounts/${ID}/follow/`,
    //     headers: {
    //       Authorization: `Bearer ${localStorage.getItem('jwt')}`
    //     }
    //   })
    //   .then((response) => {
    //     // console.log('#########################')
    //     // console.log(response.data)
    //     this.follow_info = response.data
    //   })
    //   .catch((error) => {
    //     console.log(error.response.data)
    //   })
    // },
  },
  created() {
    // this.getFollowInfo()
  }

}
</script>

<style scoped>

</style>