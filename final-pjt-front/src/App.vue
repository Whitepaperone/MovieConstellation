<template>
  <div id="app">
    <b-navbar type="dark" variant="dark" fill="true" class="d-flex justify-content-between">
      <b-navbar-brand href="http://localhost:8080/">
        <img src="./assets/ssasfy.png" alt="logo" style="width:50px; height:50px;" >
      </b-navbar-brand>
      <div>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown right text="Movie">
              <div class="m-0">
                <router-link
                  :to="{name: 'movieview'}"
                  tag="b-dropdown-item"
                  class="router-link"
                  
                >
                <b>All</b>
                </router-link>
              </div>
              <!-- <router-link
                :to="{name: 'randomview'}"
                tag="b-dropdown-item"
                class="router-link"
              >
                <b>Ramdom</b>
              </router-link> -->
              <router-link
                :to="{name : 'searchmovie'}"
                tag="b-dropdown-item"
                class="router-link"
              >
                <b>Search</b>
              </router-link>
            </b-nav-item-dropdown>
            

            <b-nav-item-dropdown right text="User" class="me-5">
              <router-link
                v-if="!isLogIn"
                :to="{name : 'Login'}"
                tag="b-dropdown-item"
                class="router-link"
              >
                <b>Login</b>
              </router-link>
              <router-link
                v-if="!isLogIn"
                :to="{name : 'Signup'}"
                tag="b-dropdown-item"
                class="router-link"
              >
                <b>Signup</b>
              </router-link>
              <router-link
                v-if="isLogIn"
                :to="{ 
                  name : 'Profile',
                  params : { username:username },  
                }"
                tag="b-dropdown-item"
                class="router-link"
              >
                <b>Profile</b>
              </router-link>
              <router-link
                v-if="isLogIn"
                :to="{ name : 'Logout' }"
                tag="b-dropdown-item"
                class="router-link"
              >
                <b>Logout</b>
              </router-link>
              <!-- <router-link
                v-if="isLogIn"
                :to="{ name : 'PlayListView' }"
                tag="b-dropdown-item"
                class="router-link"
              >
                <b>PlayList</b>
              </router-link>
              <router-link
                v-if="isLogIn"
                :to="{name : 'watchlist'}"
                tag="b-dropdown-item"
                class="router-link"
              >
                <b>Liked</b>
              </router-link> -->
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
    <div class="container">
      <div class="row justify-content-center">
        <div class="frame">
            <router-link class="frame" :to="{ name: 'randomview' }">
              <div class="ball"></div>
            </router-link>
          <div class="center">
            <div class="ball"></div>
            <div class="blubb-1"></div>
            <div class="blubb-2"></div>
            <div class="blubb-3"></div>
            <div class="blubb-4"></div>
            <div class="blubb-5"></div>
            <div class="blubb-6"></div>
            <div class="blubb-7"></div>
            <div class="blubb-8"></div>
            <div class="sparkle-1"></div>
            <div class="sparkle-2"></div>
            <div class="sparkle-3"></div>
            <div class="sparkle-4"></div>
            <div class="sparkle-5"></div>
            <div class="sparkle-6"></div>
            <div class="sparkle-7"></div>
            <div class="sparkle-8"></div>
            <div class="sparkle-9"></div>
            <div class="sparkle-10"></div>
          </div>
        </div>
      </div>
      <div class="row">
        
        <router-view
          @login="logIn"
          @logout="logOut"
          :user="user"
        />
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      isLogIn: false,
      username : ''
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    user() {
      return this.$store.state.user
    },
  },
  methods: {
    logIn(username) {
      this.isLogIn = true
      this.$store.state.username = username
    },
    logOut() {
      this.isLogIn = false
      this.username = null
    }, 
    checkJWT() {
      if (localStorage.getItem('jwt')) {
        this.isLogIn = true
      } else {
        this.isLogIn = false
      }
    },
    updateUserInfo() {
      this.username = localStorage.getItem('username')
      if (localStorage.getItem('username')) {
        this.$store.dispatch("getUser")
      }
    }
  },
  created() {
    this.$store.dispatch("getMovie")
    this.checkJWT()
    this.updateUserInfo()
  },
}
document.body.addEventListener("pointermove", (e)=>{
  const { currentTarget: el, clientX: x, clientY: y } = e;
  const { top: t, left: l, width: w, height: h } = el.getBoundingClientRect();
  el.style.setProperty('--posX',  x-l-w/2);
  el.style.setProperty('--posY',  y-t-h/2);
})

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #bcc4cc;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #ae1717;
}
body{
  height:100vh;
  width: 100vw;
  margin: 0;
  --x: calc(var(--posX, 0) * 1px);
  --y: calc(var(--posY, 0) * 1px);
  background-image: 
    linear-gradient(115deg, rgb(211 255 215), rgb(0 0 0)), 
    radial-gradient( 90% 100% at calc( 50% + var(--x)) calc( 0% + var(--y)), rgb(200 200 200), rgb(022 000 045)), 
    radial-gradient(100% 100% at calc( 50% + var(--x)) calc( 0% + var(--y)), rgb(254, 255, 198), rgb(036 000 000)), 
    linear-gradient(15deg, rgb(87, 87, 87), rgb(110, 0, 133)),
    radial-gradient(150% 210% at calc(100% + var(--x)) calc( 0% + var(--y)), rgb(148, 216, 195), rgb(0, 3, 90)), 
    radial-gradient(100% 100% at calc(100% - var(--x)) calc(30% - var(--y)), rgb(141, 42, 0), rgb(163, 207, 219)), 
    linear-gradient(60deg, rgb(248, 166, 166), rgb(120 086 255));
  background-blend-mode: overlay, overlay, difference, difference, difference, difference, normal;

  background-repeat: no-repeat;
    background-attachment: fixed;
}

</style>

<style scoped>
.router-link {
  width: 76%;
}
b {
  color: #0f0f2a;
}
body {
	background: #201c28;
}
.frame {
  top: 50%;
  left: 50%;
  width: 50vw;
  height: 50vh;
  border-radius: 2px;
  filter: contrast(25);
}
.center {
  position: absolute;
  top: 50%;
  left: 50%;
}

.ball {
  width: 90px;
  height: 90px;
  border-radius: 50%;
          filter: blur(15px);
}

.blubb-1 {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 50px;
  height: 50px;
          transform: rotate(150deg);
}
.blubb-1:after {
  position: absolute;
  display: block;
  content: '';
  width: 50px;
  height: 50px;
  background: rgb(0, 0, 0);
  background-blend-mode: difference;

  border-radius: 50%;
          transform-origin: 37px 37px;
          animation: rotate 2.7s ease-in-out 0.2s infinite;
          filter: blur(5px);
}

.blubb-2 {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 50px;
  height: 50px;
          transform: rotate(276deg);
}
.blubb-2:after {
  position: absolute;
  display: block;
  content: '';
  width: 50px;
  height: 50px;
  background: rgb(0, 0, 0);
  background-blend-mode: difference;
  border-radius: 50%;
          transform-origin: 34px 34px;
          animation: rotate 2.9s ease-in-out 0.4s infinite;
          filter: blur(5px);
}

.blubb-3 {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 50px;
          transform: rotate(76deg);
}
.blubb-3:after {
  position: absolute;
  display: block;
  content: '';
  width: 50px;
  height: 50px;
  background: rgb(0, 0, 0);
  background-blend-mode: overlay;
  border-radius: 50%;
          transform-origin: 31px 31px;
          animation: rotate 3.1s ease-in-out 0.6s infinite;
          filter: blur(5px);
}

.blubb-4 {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 50px;
  height: 50px;
          transform: rotate(295deg);
}
.blubb-4:after {
  position: absolute;
  display: block;
  content: '';
  width: 50px;
  height: 50px;
  background: #000;
  border-radius: 50%;
          transform-origin: 28px 28px;
          animation: rotate 3.3s ease-in-out 0.8s infinite;
          filter: blur(5px);
}

.blubb-5 {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 50px;
  height: 50px;
          transform: rotate(92deg);
}
.blubb-5:after {
  position: absolute;
  display: block;
  content: '';
  width: 50px;
  height: 50px;
  background: #000;
  border-radius: 50%;
          transform-origin: 25px 25px;
          animation: rotate 3.5s ease-in-out 1s infinite;
          filter: blur(5px);
}

.blubb-6 {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 50px;
  height: 50px;
          transform: rotate(83deg);
}
.blubb-6:after {
  position: absolute;
  display: block;
  content: '';
  width: 50px;
  height: 50px;
  background: #000;
  border-radius: 50%;
          transform-origin: 22px 22px;
          animation: rotate 3.7s ease-in-out 1.2s infinite;
          filter: blur(5px);
}

.blubb-7 {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 50px;
  height: 50px;
          transform: rotate(215deg);
}
.blubb-7:after {
  position: absolute;
  display: block;
  content: '';
  width: 50px;
  height: 50px;
  background: #000;
  border-radius: 50%;
          transform-origin: 19px 19px;
          animation: rotate 3.9s ease-in-out 1.4s infinite;
          filter: blur(5px);
}

.blubb-8 {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 50px;
  height: 50px;
          transform: rotate(158deg);
}
.blubb-8:after {
  position: absolute;
  display: block;
  content: '';
  width: 50px;
  height: 50px;
  background: #000;
  border-radius: 50%;
          transform-origin: 16px 16px;
          animation: rotate 4.1s ease-in-out 1.6s infinite;
          filter: blur(5px);
}

.sparkle-1 {
  position: absolute;
  top: 38px;
  left: 38px;
  width: 8px;
  height: 8px;
          transform: rotate(292deg);
}
.sparkle-1:after {
  position: absolute;
  display: block;
  content: '';
  width: 15px;
  height: 15px;
  background: rgb(255, 255, 255);
  background-blend-mode: difference;
  border-radius: 50%;
          transform-origin: 58px 58px;
          animation: rotate 3.7s ease-in-out 0.2s infinite;
          filter: blur(3px);
}

.sparkle-2 {
  position: absolute;
  top: 38px;
  left: 38px;
  width: 9px;
  height: 9px;
          transform: rotate(215deg);
}
.sparkle-2:after {
  position: absolute;
  display: block;
  content: '';
  width: 9px;
  height: 9px;
  background: rgb(255, 255, 255);
  border-radius: 50%;
          transform-origin: 56px 56px;
          animation: rotate 3.9s ease-in-out 0.4s infinite;
          filter: blur(3px);
}

.sparkle-3 {
  position: absolute;
  top: 38px;
  left: 38px;
  width: 15px;
  height: 15px;
          transform: rotate(127deg);
}
.sparkle-3:after {
  position: absolute;
  display: block;
  content: '';
  width: 10px;
  height: 10px;
  background: rgb(255, 255, 255);
  border-radius: 50%;
          transform-origin: 54px 54px;
          animation: rotate 4.1s ease-in-out 0.6s infinite;
          filter: blur(3px);
}

.sparkle-4 {
  position: absolute;
  top: 38px;
  left: 38px;
  width: 11px;
  height: 11px;
          transform: rotate(49deg);
}
.sparkle-4:after {
  position: absolute;
  display: block;
  content: '';
  width: 11px;
  height: 11px;
  background: rgb(255, 255, 255);
  border-radius: 50%;
          transform-origin: 52px 52px;
          animation: rotate 4.3s ease-in-out 0.8s infinite;
          filter: blur(3px);
}

.sparkle-5 {
  position: absolute;
  top: 38px;
  left: 38px;
  width: 12px;
  height: 12px;
          transform: rotate(286deg);
}
.sparkle-5:after {
  position: absolute;
  display: block;
  content: '';
  width: 12px;
  height: 12px;
  background: #000;
  border-radius: 50%;
          transform-origin: 50px 50px;
          animation: rotate 4.5s ease-in-out 1s infinite;
          filter: blur(3px);
}

.sparkle-6 {
  position: absolute;
  top: 38px;
  left: 38px;
  width: 13px;
  height: 13px;
          transform: rotate(120deg);
}
.sparkle-6:after {
  position: absolute;
  display: block;
  content: '';
  width: 13px;
  height: 13px;
  background: #000;
  border-radius: 50%;
          transform-origin: 48px 48px;
          animation: rotate 4.7s ease-in-out 1.2s infinite;
          filter: blur(3px);
}

.sparkle-7 {
  position: absolute;
  top: 38px;
  left: 38px;
  width: 14px;
  height: 14px;
          transform: rotate(196deg);
}
.sparkle-7:after {
  position: absolute;
  display: block;
  content: '';
  width: 20px;
  height: 20px;
  background: #000;
  border-radius: 50%;
          transform-origin: 46px 46px;
          animation: rotate 4.9s ease-in-out 1.4s infinite;
          filter: blur(3px);
}

.sparkle-8 {
  position: absolute;
  top: 38px;
  left: 38px;
  width: 15px;
  height: 15px;
          transform: rotate(157deg);
}
.sparkle-8:after {
  position: absolute;
  display: block;
  content: '';
  width: 15px;
  height: 15px;
  background: #000;
  border-radius: 50%;
          transform-origin: 44px 44px;
          animation: rotate 5.1s ease-in-out 1.6s infinite;
          filter: blur(3px);
}

.sparkle-9 {
  position: absolute;
  top: 38px;
  left: 38px;
  width: 16px;
  height: 16px;
          transform: rotate(36deg);
}
.sparkle-9:after {
  position: absolute;
  display: block;
  content: '';
  width: 6px;
  height: 6px;
  background: #000;
  border-radius: 50%;
          transform-origin: 42px 42px;
          animation: rotate 5.3s ease-in-out 1.8s infinite;
          filter: blur(3px);
}

.sparkle-10 {
  position: absolute;
  top: 38px;
  left: 38px;
  width: 17px;
  height: 17px;
          transform: rotate(115deg);
}
.sparkle-10:after {
  position: absolute;
  display: block;
  content: '';
  width: 20px;
  height: 20px;
  background: #000;
  border-radius: 50%;
          transform-origin: 40px 40px;
          animation: rotate 5.5s ease-in-out 2s infinite;
          filter: blur(3px);
}

@keyframes rotate {
  from {
            transform: rotate(0deg) translate3d(0, 0, 0);
  }
  to {
            transform: rotate(360deg) translate3d(0, 0, 0);
  }
}


</style>