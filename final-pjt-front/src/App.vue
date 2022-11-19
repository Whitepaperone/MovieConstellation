<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg" style="background-color: #e3f2fd;">
      <div class="container-fluid">
        <div>
          <img src="./assets/ssasfy.png" alt="numbnut" style="width:50px; height:50px;" >
        </div>
        <div>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarScroll">
            <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
              
              <li class="nav-item me-5 ">
                <router-link :to="{name: 'movieview'}">
                  Movie
                </router-link> 
              </li>

              <li class="nav-item me-5">
                <router-link :to="{name: 'randomview'}">
                  Random
                </router-link>
              </li>

              <li class="nav-item me-5 dropdown">
                <router-link :to="{name : 'watchlist'}">
                  WatchList
                </router-link>
              </li>
              <li class="nav-item me-5 dropdown">
                <router-link :to="{name : 'searchmovie'}">
                  Search
                </router-link>
              </li>

              <li 
                v-if="!isLogIn" 
                class="nav-item me-5 dropdown">
                <router-link :to="{name : 'Login'}">
                  Login
                </router-link>
              </li>

              <li 
                v-if="!isLogIn"
                class="nav-item me-5 dropdown">
                <router-link :to="{name : 'Signup'}">
                  Signup
                </router-link>
              </li>

              <li
                v-if="isLogIn" 
                class="nav-item me-5 dropdown">
                <router-link
                  :to="{ 
                    name : 'Profile',
                    params : { username:username },  
                  }"
                >
                  Profile
                </router-link>
              </li>

              <li
                v-if="isLogIn" 
                class="nav-item me-5 dropdown">
                <router-link :to="{ name : 'Logout' }">
                  Logout
                </router-link>
              </li>

              <li
                v-if="isLogIn" 
                class="nav-item me-5 dropdown">
                <router-link :to="{ name : 'PlayListView' }">
                  PlayList
                </router-link>
              </li>

            </ul>
          </div>        
        </div>
      </div>
      
    </nav>
    <div>
      <router-link :to="{ name: 'randomview' }">[BLACKHOLE]</router-link>
    </div>
    <router-view
      @login="logIn"
      @logout="logOut"
      :user="user"
    />
    <p>state.user = {{this.$store.state.user}}</p>
    <p>computed.user = {{user}}</p>
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
    this.$store.dispatch("getLikeMovie",this.$store.state.user.id)
    this.checkJWT()
    this.updateUserInfo()
  },
}
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
  color: #42b983;
}


</style>

