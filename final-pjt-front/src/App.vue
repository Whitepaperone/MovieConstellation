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
              <router-link
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
                Liked
              </router-link>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
    <div>
      <router-link :to="{ name: 'randomview' }">[BLACKHOLE]</router-link>
    </div>
    <!-- <div>
      <router-link :to="{ name: 'combinationMovie' }">[Another Movie]</router-link>
    </div> -->
    <router-view
      @login="logIn"
      @logout="logOut"
      :user="user"
    />
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
  color: #2c3e50;
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
</style>