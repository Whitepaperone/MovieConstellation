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
        <!-- intersection percent -->
        <div class="container col-8">
          <div class="container col">
  <section>
    <article>
      <div class="chart">
        <div class="bar bar-60 white">
          <div class="face top">
            <div class="growing-bar"></div>
          </div>
          <div class="face side-0">
            <div class="growing-bar"></div>
          </div>
          <div class="face floor">
            <div class="growing-bar"></div>
          </div>
          <div class="face side-a"></div>
          <div class="face side-b"></div>
          <div class="face side-1">
            <div class="growing-bar"></div>
          </div>
        </div>
      </div>
    </article>
  </section>
  
</div>
<!-- list들 -->
<div class="col-8">
  <!-- 플레이리스트 -->
  <div>
    <h5>[내 저장목록]</h5>
            <Playlist
              v-for="PL in userPL"
              :key="PL?.id"
              :PL="PL"
              />
              
            </div>
            <!-- 좋아요리스트 -->
            <div>
              <h5>[내가 좋아하는 영화]</h5>
              <div class="d-flex justify-content-start">
                <p>영화 목록 : </p>
                <Likelist
                  v-for="LL in userLL"
                  :key="LL?.id"
                  :LL="LL"
                  />
                </div>
              </div>
            <button @click="getLikeMovie">버튼</button>
          
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
    user: null,
    followObj: null,
    userplaylist: null,
    userlikelist: null,
  }
},
computed:{
    follow(){
        return this.followObj
    },
    userPL() {
      return this.userplaylist
    },
    userLL() {
      return this.userlikelist
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
    // console.log(username)
      axios({
        method: 'get',
        url : `http://127.0.0.1:8000/accounts/profile/${username}/`,

      })
      .then((response) => {
        // console.log(response.data)
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
      const user_pk=this.user?.id
      
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
        this.getLikeMovie()
      })
      .catch((error) => {
        console.log(error)
      })
  },
  getUserPlaylist() {
    let user_pk = this.followObj?.id
    // console.log(user_pk)
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
  },
  getLikeMovie() {
    let user_pk = this.user?.id

    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${user_pk}/like/`
    })
    .then((res) => {
      // console.log(res.data)
      this.userlikelist = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }
    
},
created() {
  this.getUserName()
  this.getProfile()
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


/* intersection style */
@import url(https://fonts.googleapis.com/css?family=Open+Sans:700,300);
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
  margin: 0;
  padding: 0;
  border: 0;
  font: inherit;
  font-size: 100%;
  vertical-align: baseline;
}

html {
  line-height: 1;
}

ol, ul {
  list-style: none;
}

table {
  border-collapse: collapse;
  border-spacing: 0;
}

caption, th, td {
  text-align: left;
  font-weight: normal;
  vertical-align: middle;
}

q, blockquote {
  quotes: none;
}
q:before, q:after, blockquote:before, blockquote:after {
  content: "";
  content: none;
}

a img {
  border: none;
}

article, aside, details, figcaption, figure, footer, header, hgroup, main, menu, nav, section, summary {
  display: block;
}

body {
  font-family: 'Open Sans', sans-serif;
  font-size: 16px;
  font-weight: 300;
  line-height: 1em;
  text-align: center;
  color: #444;
  background: #d0d0d0;
}

h1 {
  font-size: 2.5em;
  margin: 2em 0 .5em;
}

h2 {
  margin-bottom: 3em;
}

em,
strong {
  font-weight: 700;
}

input {
  display: none;
}

header p {
  margin-bottom: 0;
}

section {
  display: flex;
  justify-content: center;
  flex-direction: column;
  margin-bottom: 2em;
  padding: 0;
}
section:last-of-type {
  margin-bottom: 0;
}
section article {
  align-self: center;
  width: 20em;
  margin-bottom: 2em;
}
section article p, section article:last-of-type {
  margin-bottom: 0;
}

p {
  line-height: 1.5em;
  max-width: 20em;
  margin: 1.5em auto 2em;
  padding-bottom: 1.5em;
}
p span {
  display: block;
}

.container {
  z-index: 1;
  display: flex;
  overflow: hidden;
  flex-direction: column;
  justify-content: center;
  margin-bottom: 4em;
}

/*
*
*
START // CHART'S RULES
 -> "if you're picking code, don't forget the variables :)"
*/
.chart {
  font-size: 1em;
  perspective: 1000px;
  perspective-origin: 50% 50%;
  -webkit-backface-visibility: visible;
          backface-visibility: visible;
}

.bar {
  font-size: 1em;
  position: relative;
  height: 10em;
  transition: all 0.3s ease-in-out;
  transform: rotateX(60deg) rotateY(0deg);
  transform-style: preserve-3d;
}
.bar .face {
  font-size: 2em;
  position: relative;
  width: 100%;
  height: 2em;
  background-color: rgba(254, 254, 254, 0.3);
}
.bar .face.side-a, .bar .face.side-b {
  width: 2em;
}
.bar .side-a {
  transform: rotateX(90deg) rotateY(-90deg) translateX(2em) translateY(1em) translateZ(1em);
}
.bar .side-b {
  transform: rotateX(90deg) rotateY(-90deg) translateX(4em) translateY(1em) translateZ(-1em);
  position: absolute;
  right: 0;
}
.bar .side-0 {
  transform: rotateX(90deg) rotateY(0) translateX(0) translateY(1em) translateZ(-1em);
}
.bar .side-1 {
  transform: rotateX(90deg) rotateY(0) translateX(0) translateY(1em) translateZ(3em);
}
.bar .top {
  transform: rotateX(0deg) rotateY(0) translateX(0em) translateY(4em) translateZ(2em);
}
.bar .floor {
  box-shadow: 0 0.1em 0.6em rgba(0, 0, 0, 0.3), 0.6em -0.5em 3em rgba(0, 0, 0, 0.3), 1em -1em 8em #fefefe;
}

.growing-bar {
  transition: all 0.3s ease-in-out;
  background-color: rgba(236, 0, 140, 0.6);
  width: 100%;
  height: 2em;
}

.bar.yellow .side-a,
.bar.yellow .growing-bar {
  background-color: rgba(241, 196, 15, 0.6);
}
.bar.yellow .side-0 .growing-bar {
  box-shadow: -0.5em -1.5em 4em rgba(241, 196, 15, 0.8);
}
.bar.yellow .floor .growing-bar {
  box-shadow: 0em 0em 2em rgba(241, 196, 15, 0.8);
}

.bar.red .side-a, input[id='red']:checked ~ .chart .side-a,
.bar.red .growing-bar,
input[id='red']:checked ~ .chart .growing-bar {
  background-color: rgba(236, 0, 140, 0.6);
}
.bar.red .side-0 .growing-bar, input[id='red']:checked ~ .chart .side-0 .growing-bar {
  box-shadow: -0.5em -1.5em 4em rgba(236, 0, 140, 0.8);
}
.bar.red .floor .growing-bar, input[id='red']:checked ~ .chart .floor .growing-bar {
  box-shadow: 0em 0em 2em rgba(236, 0, 140, 0.8);
}

.bar.cyan .side-a, input[id='cyan']:checked ~ .chart .side-a,
.bar.cyan .growing-bar,
input[id='cyan']:checked ~ .chart .growing-bar {
  background-color: rgba(87, 202, 244, 0.6);
}
.bar.cyan .side-0 .growing-bar, input[id='cyan']:checked ~ .chart .side-0 .growing-bar {
  box-shadow: -0.5em -1.5em 4em #57caf4;
}
.bar.cyan .floor .growing-bar, input[id='cyan']:checked ~ .chart .floor .growing-bar {
  box-shadow: 0em 0em 2em #57caf4;
}

.bar.navy .side-a,
.bar.navy .growing-bar {
  background-color: rgba(10, 64, 105, 0.6);
}
.bar.navy .side-0 .growing-bar {
  box-shadow: -0.5em -1.5em 4em rgba(10, 64, 105, 0.8);
}
.bar.navy .floor .growing-bar {
  box-shadow: 0em 0em 2em rgba(10, 64, 105, 0.8);
}

.bar.lime .side-a, input[id='lime']:checked ~ .chart .side-a,
.bar.lime .growing-bar,
input[id='lime']:checked ~ .chart .growing-bar {
  background-color: rgba(118, 201, 0, 0.6);
}
.bar.lime .side-0 .growing-bar, input[id='lime']:checked ~ .chart .side-0 .growing-bar {
  box-shadow: -0.5em -1.5em 4em #76c900;
}
.bar.lime .floor .growing-bar, input[id='lime']:checked ~ .chart .floor .growing-bar {
  box-shadow: 0em 0em 2em #76c900;
}

.bar.white .side-a,
.bar.white .growing-bar {
  background-color: rgba(254, 254, 254, 0.6);
}
.bar.white .side-0 .growing-bar {
  box-shadow: -0.5em -1.5em 4em #fefefe;
}
.bar.white .floor .growing-bar {
  box-shadow: 0em 0em 2em #fefefe;
}

.bar.gray .side-a,
.bar.gray .growing-bar {
  background-color: rgba(68, 68, 68, 0.6);
}
.bar.gray .side-0 .growing-bar {
  box-shadow: -0.5em -1.5em 4em #444;
}
.bar.gray .floor .growing-bar {
  box-shadow: 0em 0em 2em #444;
}

.chart .bar.yellow-face .face {
  background-color: rgba(241, 196, 15, 0.2);
}

.chart .bar.lime-face .face {
  background-color: rgba(118, 201, 0, 0.2);
}

.chart .bar.red-face .face {
  background-color: rgba(236, 0, 140, 0.2);
}

.chart .bar.navy-face .face {
  background-color: rgba(10, 64, 105, 0.2);
}

.chart .bar.cyan-face .face {
  background-color: rgba(87, 202, 244, 0.2);
}

.chart .bar.gray-face .face {
  background-color: rgba(68, 68, 68, 0.2);
}

.chart .bar.lightGray-face .face {
  background-color: rgba(145, 145, 145, 0.2);
}

.bar-0 .growing-bar {
  width: 0%;
}

.bar-1 .growing-bar {
  width: 1%;
}

.bar-2 .growing-bar {
  width: 2%;
}

.bar-3 .growing-bar {
  width: 3%;
}

.bar-4 .growing-bar {
  width: 4%;
}

.bar-5 .growing-bar {
  width: 5%;
}

.bar-6 .growing-bar {
  width: 6%;
}

.bar-7 .growing-bar {
  width: 7%;
}

.bar-8 .growing-bar {
  width: 8%;
}

.bar-9 .growing-bar {
  width: 9%;
}

.bar-10 .growing-bar {
  width: 10%;
}

.bar-11 .growing-bar {
  width: 11%;
}

.bar-12 .growing-bar {
  width: 12%;
}

.bar-13 .growing-bar {
  width: 13%;
}

.bar-14 .growing-bar {
  width: 14%;
}

.bar-15 .growing-bar {
  width: 15%;
}

.bar-16 .growing-bar {
  width: 16%;
}

.bar-17 .growing-bar {
  width: 17%;
}

.bar-18 .growing-bar {
  width: 18%;
}

.bar-19 .growing-bar {
  width: 19%;
}

.bar-20 .growing-bar, input[id='exercise-2']:checked ~ .chart.grid .exercise .bar:nth-child(1) .growing-bar {
  width: 20%;
}

.bar-21 .growing-bar {
  width: 21%;
}

.bar-22 .growing-bar {
  width: 22%;
}

.bar-23 .growing-bar {
  width: 23%;
}

.bar-24 .growing-bar {
  width: 24%;
}

.bar-25 .growing-bar, input[id='pos-0']:checked ~ .chart .growing-bar {
  width: 25%;
}

.bar-26 .growing-bar {
  width: 26%;
}

.bar-27 .growing-bar {
  width: 27%;
}

.bar-28 .growing-bar {
  width: 28%;
}

.bar-29 .growing-bar {
  width: 29%;
}

.bar-30 .growing-bar {
  width: 30%;
}

.bar-31 .growing-bar {
  width: 31%;
}

.bar-32 .growing-bar {
  width: 32%;
}

.bar-33 .growing-bar {
  width: 33%;
}

.bar-34 .growing-bar {
  width: 34%;
}

.bar-35 .growing-bar {
  width: 35%;
}

.bar-36 .growing-bar {
  width: 36%;
}

.bar-37 .growing-bar {
  width: 37%;
}

.bar-38 .growing-bar {
  width: 38%;
}

.bar-39 .growing-bar {
  width: 39%;
}

.bar-40 .growing-bar {
  width: 40%;
}

.bar-41 .growing-bar {
  width: 41%;
}

.bar-42 .growing-bar {
  width: 42%;
}

.bar-43 .growing-bar {
  width: 43%;
}

.bar-44 .growing-bar {
  width: 44%;
}

.bar-45 .growing-bar {
  width: 45%;
}

.bar-46 .growing-bar {
  width: 46%;
}

.bar-47 .growing-bar {
  width: 47%;
}

.bar-48 .growing-bar {
  width: 48%;
}

.bar-49 .growing-bar {
  width: 49%;
}

.bar-50 .growing-bar, input[id='pos-1']:checked ~ .chart .growing-bar, input[id='exercise-2']:checked ~ .chart.grid .exercise .bar:nth-child(2) .growing-bar, input[id='exercise-4']:checked ~ .chart.grid .exercise .bar:nth-child(1) .growing-bar, input[id='exercise-4']:checked ~ .chart.grid .exercise .bar:nth-child(2) .growing-bar {
  width: 50%;
}

.bar-51 .growing-bar {
  width: 51%;
}

.bar-52 .growing-bar {
  width: 52%;
}

.bar-53 .growing-bar {
  width: 53%;
}

.bar-54 .growing-bar {
  width: 54%;
}

.bar-55 .growing-bar {
  width: 55%;
}

.bar-56 .growing-bar {
  width: 56%;
}

.bar-57 .growing-bar {
  width: 57%;
}

.bar-58 .growing-bar {
  width: 58%;
}

.bar-59 .growing-bar {
  width: 59%;
}

.bar-60 .growing-bar {
  width: 60%;
}

.bar-61 .growing-bar {
  width: 61%;
}

.bar-62 .growing-bar {
  width: 62%;
}

.bar-63 .growing-bar {
  width: 63%;
}

.bar-64 .growing-bar {
  width: 64%;
}

.bar-65 .growing-bar {
  width: 65%;
}

.bar-66 .growing-bar {
  width: 66%;
}

.bar-67 .growing-bar {
  width: 67%;
}

.bar-68 .growing-bar {
  width: 68%;
}

.bar-69 .growing-bar {
  width: 69%;
}

.bar-70 .growing-bar, input[id='exercise-3']:checked ~ .chart.grid .exercise .bar:nth-child(1) .growing-bar, input[id='exercise-3']:checked ~ .chart.grid .exercise .bar:nth-child(2) .growing-bar, input[id='exercise-3']:checked ~ .chart.grid .exercise .bar:nth-child(3) .growing-bar {
  width: 70%;
}

.bar-71 .growing-bar {
  width: 71%;
}

.bar-72 .growing-bar {
  width: 72%;
}

.bar-73 .growing-bar {
  width: 73%;
}

.bar-74 .growing-bar {
  width: 74%;
}

.bar-75 .growing-bar, input[id='pos-2']:checked ~ .chart .growing-bar {
  width: 75%;
}

.bar-76 .growing-bar {
  width: 76%;
}

.bar-77 .growing-bar {
  width: 77%;
}

.bar-78 .growing-bar {
  width: 78%;
}

.bar-79 .growing-bar {
  width: 79%;
}

.bar-80 .growing-bar, input[id='exercise-2']:checked ~ .chart.grid .exercise .bar:nth-child(3) .growing-bar {
  width: 80%;
}

.bar-81 .growing-bar {
  width: 81%;
}

.bar-82 .growing-bar {
  width: 82%;
}

.bar-83 .growing-bar {
  width: 83%;
}

.bar-84 .growing-bar {
  width: 84%;
}

.bar-85 .growing-bar {
  width: 85%;
}

.bar-86 .growing-bar {
  width: 86%;
}

.bar-87 .growing-bar {
  width: 87%;
}

.bar-88 .growing-bar {
  width: 88%;
}

.bar-89 .growing-bar {
  width: 89%;
}

.bar-90 .growing-bar {
  width: 90%;
}

.bar-91 .growing-bar {
  width: 91%;
}

.bar-92 .growing-bar {
  width: 92%;
}

.bar-93 .growing-bar {
  width: 93%;
}

.bar-94 .growing-bar {
  width: 94%;
}

.bar-95 .growing-bar {
  width: 95%;
}

.bar-96 .growing-bar {
  width: 96%;
}

.bar-97 .growing-bar {
  width: 97%;
}

.bar-98 .growing-bar {
  width: 98%;
}

.bar-99 .growing-bar {
  width: 99%;
}

.bar-100 .growing-bar, input[id='pos-3']:checked ~ .chart .growing-bar, input[id='exercise-4']:checked ~ .chart.grid .exercise .bar:nth-child(3) .growing-bar {
  width: 100%;
}

/*
END // CHART'S RULES
*
*
*/
.chart.grid {
  display: flex;
  flex-direction: row;
}
.chart.grid .exercise {
  flex: 0 0 100%;
  display: flex;
}
.chart.grid .exercise .bar {
  flex: 1;
  margin: 0 .5em;
}
.chart.grid .exercise .bar:nth-child(2) {
  z-index: 8;
  flex: 1 0 40%;
}
.chart.grid .exercise .bar:first-child {
  z-index: 10;
  margin-left: 0;
}
.chart.grid .exercise .bar:last-child {
  margin-right: 0;
}

.actions {
  display: flex;
  justify-content: center;
  margin-bottom: 0;
  padding-bottom: 2em;
  border-bottom: 1px dotted rgba(68, 68, 68, 0.4);
}

label {
  box-sizing: border-box;
  padding: 1em;
  margin: 0 .2em;
  cursor: pointer;
  transition: all .15s ease-in-out;
  color: #0a4069;
  border: 1px solid rgba(254, 254, 254, 0.6);
  border-radius: 0;
  flex: 1;
}
label:first-child {
  margin-left: 0;
  border-radius: .2em 0 0 .2em;
}
label:last-child {
  margin-right: 0;
  border-radius: 0 .2em .2em 0;
}

input[id='exercise-1']:checked ~ .actions label[for='exercise-1'],
input[id='exercise-2']:checked ~ .actions label[for='exercise-2'],
input[id='exercise-3']:checked ~ .actions label[for='exercise-3'],
input[id='exercise-4']:checked ~ .actions label[for='exercise-4'],
input[id='pos-0']:checked ~ .actions label[for='pos-0'],
input[id='pos-1']:checked ~ .actions label[for='pos-1'],
input[id='pos-2']:checked ~ .actions label[for='pos-2'],
input[id='pos-3']:checked ~ .actions label[for='pos-3'],
input[id='red']:checked ~ .actions label[for='red'],
input[id='cyan']:checked ~ .actions label[for='cyan'],
input[id='lime']:checked ~ .actions label[for='lime'] {
  color: #76c900;
  border: 1px solid #031523;
  background-color: #0a4069;
}

input[id='exercise-2']:checked ~ .chart.grid .exercise .bar:nth-child(1) {
  flex: 1 0 0%;
}
input[id='exercise-2']:checked ~ .chart.grid .exercise .bar:nth-child(2) {
  flex: 1;
}
input[id='exercise-2']:checked ~ .chart.grid .exercise .bar:nth-child(3) {
  flex: 1 0 30%;
}

input[id='exercise-3']:checked ~ .chart.grid .exercise .bar:nth-child(1), input[id='exercise-3']:checked ~ .chart.grid .exercise .bar:nth-child(2), input[id='exercise-3']:checked ~ .chart.grid .exercise .bar:nth-child(3) {
  flex: 1;
}

input[id='exercise-4']:checked ~ .chart.grid .exercise .bar:nth-child(1), input[id='exercise-4']:checked ~ .chart.grid .exercise .bar:nth-child(2) {
  flex: 1 0 30%;
}
input[id='exercise-4']:checked ~ .chart.grid .exercise .bar:nth-child(3) {
  flex: 1;
}

</style>