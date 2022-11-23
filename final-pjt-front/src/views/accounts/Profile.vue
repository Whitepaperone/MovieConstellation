<template>
    <div>
      <div class="row">
        <!-- 유저 프로필 -->
        <div class="col-4">
          <section class="profile">
            <div class="profile-header"><img src="../../assets/space_bg.jpg" alt="BGIMG"/></div>
            <div class="profile-content"><img src="../../assets/Astronaut_helmet1.jpg" alt="PFIMG"/>
              <h1>{{followObj?.username}}</h1>
              <button v-if="this.$store.state.user?.id!==user?.id && !followObj?.is_followed" @click="following" type="button">Follow</button>
              <button v-if="this.$store.state.user?.id!==user?.id && followObj?.is_followed" @click="following" type="button">Unfollow</button>
            </div>
            <ul aria-label="Statistics">
              <li >{{followObj?.followers_count}}<span>followers</span></li>
              <li>{{followObj?.followings_count}}<span>following</span></li>
            </ul>
          </section>
        </div>
        <!-- list들 -->
        <div class="col-8">
          <!-- 플레이리스트 -->
          <div>
            <Playlist
              v-for="PL in userPL"
              :key="PL?.id"
              :PL="PL"
            />
            <button @click="getUserPlaylist">플레이리스트 보기</button>
          </div>
          <!-- 좋아요리스트 -->
          <div>
            
            좋아요 리스트
          </div>
          <!-- 유저랑 다른영화 -->
          <!-- <div v-if="this.$store.state.user.id!==user.id" class="row">
            유저랑 다른 리스트
            <Combination :comuser="userObj={'a':user.id, 'b':this.$store.state.user.id}"/>
          </div> -->
        </div>
      </div>

      <div class="row">
          <FollowersVue
              :usercomp="user"
          />
          <h1>hello?</h1>
      </div>
      
      
    </div>
</template>

<script>
import FollowersVue from '@/components/profile/Followers.vue'
import Combination from '@/components/profile/Combination'
import Playlist from '@/components/profile/Playlist.vue'
import Likelist from '@/components/profile/Likelist.vue'
import axios from 'axios'
export default {
name: 'Profile',
components: {
    FollowersVue,
    Combination,
    Playlist,
    Likelist,
},
data(){
  return{
    username: null,
    user:null,
    followObj: null,
    userplaylist : null,
  }
},
computed:{
    follow(){
        return this.followObj
    },
    userPL() {
      return this.userplaylist
    }
},
props: {
    // user: Object
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
      .then(() => {
        this.getFollow()
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
        // console.log(response.data)
        this.followObj=response.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  getFollow(){
      // console.log(this.user.id)
      const user_pk=this.user.id
      
      axios({
        method: 'get',
        url : `http://127.0.0.1:8000/accounts/${this.user?.id}/follow/`,
        headers: {
        Authorization: `Bearer ${localStorage.getItem('jwt')}`
      }

      })
      .then((response) => {
        // console.log('getFollow')
        this.followObj=response.data
      })
      .then(() => {
        this.getUserPlaylist()
      })
      .catch((error) => {
        console.log(error)
      })
  },
  getUserPlaylist() {
    let user_pk = this.followObj?.id
    console.log(user_pk)
    axios({
      method: 'get',
      url : `http://127.0.0.1:8000/community/profileplaylist/${user_pk}/`
    })
    .then((res) => {
      // console.log(res)
      this.userplaylist = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }
},
created() {
  this.getUserName()
  this.getProfile()

  // this.getFollow()
  // this.getUserPlaylist()
}
}
</script>

<style scoped>
section.profile {
	 position: relative;
	 width: 325px;
	 border: 1px solid #171a1f;
	 border-radius: 8px;
	 text-transform: uppercase;
}
 section.profile::after {
	 display: block;
	 position: absolute;
	 top: 100%;
	 left: 3%;
	 z-index: -1;
	 width: 94%;
	 height: 1px;
	 box-shadow: 0 0 12px rgba(0, 0, 0, 0.9);
	 content: '';
}
 .profile-header {
	 height: 140px;
	 border-radius: 7px 7px 0 0;
	 overflow: hidden;
	 background: #e8decd;
}
 .profile-header img {
	 object-fit: cover;
}
 .profile-content {
	 padding: 0 30px 30px;
	 border-radius: 0 0 5px 5px;
	 color: #e7e0d0;
	 text-align: center;
	 background: #2f363e;
}
 .profile-content img {
	 margin-top: -75px;
	 width: 150px;
	 height: 150px;
	 border: 5px solid #e7e0cf;
	 border-radius: 100%;
	 background: #e7e0cf;
}
 .profile-content h1 {
	 margin: 25px 0 0;
	 font-size: 1.4em;
	 font-weight: 200;
	 letter-spacing: 0.05em;
}
 .profile-content p {
	 margin: 5px 0 0;
	 color: #b49e6b;
	 font-size: 0.8125em;
	 font-weight: 200;
}
 button {
	 margin-top: 25px;
	 padding: 10px 20px;
	 min-width: 160px;
	 background: #222259;
	 border: 1px solid #0f1721;
	 border-radius: 4px;
	 box-shadow: inset 0 1px 0 0 #18183e;
	 color: #e7e0cf;
	 font-family: inherit;
	 font-size: 0.8em;
	 font-weight: 600;
	 text-shadow: 0 1px 1px rgba(0, 0, 0, .25);
	 transition: background ease-out 0.15s;
}
 button:hover, button:focus {
	 background: #35358b;
}
 button:focus {
	 outline: none;
	 box-shadow: inset 0 1px 0 0 #18183e, 0 0 0 3px #e7e0cf;
}
 button:active {
	 background: rgb(79, 79, 199);
	 transition: none;
}
 ul {
	 display: flex;
	 margin: 0;
	 padding: 0;
	 border-top: 1px solid #171a1f;
	 border-radius: 0 0 7px 7px;
	 list-style: none;
	 background: #2f363e;
}
 ul li {
	 display: flex;
	 flex: 0 1 50%;
	 justify-content: center;
	 align-items: center;
	 border-top: 1px solid #3e424d;
	 padding: 20px 10px;
	 color: #c54b30;
	 font-weight: 600;
	 font-size: 1.2em;
}
 ul li + li {
	 border-left: 1px solid #171a1f;
	 box-shadow: -1px 0 0 #3e424d;
}
 ul span {
	 display: inline-block;
	 margin-left: 0.4em;
	 color: #a9a9a9;
	 font-weight: 300;
	 font-size: 0.8em;
}
 html {
	 height: 100%;
	 background: #2d353d;
}
 body {
	 display: flex;
	 margin: 0;
	 padding: 20px;
	 min-height: 100%;
	 box-sizing: border-box;
	 align-items: center;
	 justify-content: center;
	 font-family: helvetica neue, sans-serif;
	 background: url('http://dir.agosto.nl/dump/profile.png');
}

 
</style>