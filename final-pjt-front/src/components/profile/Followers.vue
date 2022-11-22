<template>
  <div>
    <!-- <p>{{user.id}}</p> -->
    <!-- <p @click="print">components followers.vue user = {{userinfo}}</p>
    <p>components followings = {{user.followings.length}}</p>
    <p>user.id = {{userinfo.id}}</p> -->
    {{usercomp}}
    <main>
      <section class="profile">
        <div class="profile-header"><img src="" alt="BGIMG"/></div>
        <div class="profile-content"><img src="" alt="PFIMG"/>
          <h1>{{username}}</h1>
          <button v_if="is_followed" type="button">Follow</button>
        </div>
        <ul aria-label="Statistics">
          <li>{{follow_info.followers_count}}<span>followers</span></li>
          <li>{{follow_info.followings_count}}<span>following</span></li>
        </ul>
      </section>
    </main>

    <!-- <button @click="getFollowInfo">getfollowinfo</button> -->
    <FollowListItem
      v-for="follow in followings"
      :key="follow.username"
      :follow="follow"
    />
    <FollowListItem
      v-for="follow in followers"
      :key="follow.username"
      :follow="follow"
    />
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
      follow_info : null,
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
        console.log('#########################')
        console.log(response.data)
        this.follow_info = response.data
      })
      .catch((error) => {
        console.log(error.response.data)
      })
    },

  },
  created() {
    this.getFollowInfo()
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