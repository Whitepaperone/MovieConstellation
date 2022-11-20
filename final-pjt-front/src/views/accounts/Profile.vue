<template>
    <div>
        <h1>{{ user.username }}'s Profile</h1>
        {{this.$store.state.user.id}}
        {{user.id}}
        {{followObj}}
        <div>
        팔로잉 : {{followObj?.followings_count}}/ 팔로워 :{{followObj?.followers_count}}
      </div>
        <button id="followBtn" v-if="this.$store.state.user.id!==user.id" @click="following">follow</button>
        <p>profile.vue user = {{user}}</p>
        <div>
            <FollowersVue
                :usercomp="user"
            />
        </div>
        <div v-if="this.$store.state.user.id!==user.id">
            <Combination
            :comuser="userObj={'a':user.id,'b':this.$store.state.user.id}"/>
        </div>
        <div>

        </div>
    </div>
</template>

<script>
import FollowersVue from '@/components/profile/Followers.vue'
import Combination from '@/components/profile/Combination'

import axios from 'axios'
export default {
name: 'Profile',
components: {
    FollowersVue,
    Combination
},
data(){
    return{
        followObj: null,
        followings: null,
        followers:null,
        user:null,
    }
},
computed:{
    follow(){
        return this.followObj
    }
},
props: {
    user: Object
},
methods: {
    getUserName() {
        this.username = localStorage.getItem('username')
    },
    getProfile(){
      const username=this.$route.params.username
      console.log(username)
       axios({
          method: 'get',
          url : `http://127.0.0.1:8000/accounts/profile/${username}/`,

        })
        .then((response) => {
          console.log(response.data)
          this.user=response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    following(){
        console.log(this.user.id)
        const user_pk=this.user.id
        axios({
          method: 'post',
          url : `http://127.0.0.1:8000/accounts/${user_pk}/follow/`,
          headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }

        })
        .then((response) => {
          console.log(response.data)
          this.followObj=response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getFollow(){
        console.log(this.user.id)
        const user_pk=this.user.id
        axios({
          method: 'get',
          url : `http://127.0.0.1:8000/accounts/${user_pk}/follow/`,
          headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }

        })
        .then((response) => {
          console.log('getFollow')
          this.followObj=response.data
        })
        .catch((error) => {
          console.log(error)
        })
    }
},
created() {
    this.getUserName()
    this.getProfile()
    this.getFollow()
}
}
</script>

<style>

</style>