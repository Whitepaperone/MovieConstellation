<template>
    <div>
        <div class="d-flex justify-content-center">
            <div class="col-12 text-center d-flex justify-content-center" style="width:800px">
                <div class="text-center justify-content-center p-5" style="background-color:rgba(159, 157, 157, 0.5); border-radius: 15px; width: 700px;">
                    <div class="card-front p-3" style="width:600px">
                        <div class="text-center p-3">
                            <h4 class="mb-4 pb-3">New Playlist!</h4>
                                <div class="form-group">
                                    <input type="text" name="PLtitle" class="form-style" placeholder="Playlist Title" id="PLtitle" autocomplete="off" v-model.trim="title" >
                                    <i class="input-icon bi bi-camera-reels-fill"></i>
                                </div>
                                <div class="form-group mt-2">
                                    <textarea name="logpass" class="form-style" placeholder="Simple Description" id="PLcontent" cols="30" rows="10" autocomplete="off" v-model.trim="content" ></textarea>
                                    <i class="input-icon bi bi-chat-dots"></i>
                                </div>
                                <SearchMovieView/>
                            <a @click="createPlaylist" class="btn mt-4">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-file-earmark-plus" viewBox="0 0 16 16">
                                    <path d="M8 6.5a.5.5 0 0 1 .5.5v1.5H10a.5.5 0 0 1 0 1H8.5V11a.5.5 0 0 1-1 0V9.5H6a.5.5 0 0 1 0-1h1.5V7a.5.5 0 0 1 .5-.5z"/>
                                    <path d="M14 4.5V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h5.5L14 4.5zm-3 0A1.5 1.5 0 0 1 9.5 3V1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V4.5h-2z"/>
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import SearchMovieView from '../movie/SearchMovieView.vue';
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: "CreatePlayListView",
    data() {
        return {
            title: null,
            content: null,
            movies: [],
        }
    },
    components:{
    SearchMovieView
    },
    methods: {
        createPlaylist() {
            const title = this.title
            const content = this.content
            const movies = this.$store.state.selected_movies
            console.log(movies)
            if (title && content) {
                axios({
                    method: 'post',
                    url:`${API_URL}/community/`,
                    data: {title, content, movies},
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('jwt')}`
                    }
                })
                .then((res) => {
                    console.log(res)
                    this.$store.dispatch('updateSeletedMovies',[])
                    console.log(this.$store.state.selected_movies)
                    this.$router.push({name: 'PlayListView'})
                })
                .catch((err) => {
                    console.log(err)
                })
            } else{
                alert('입력을 확인하세요.')
            }
        }
    }
}
</script>

<style lang="scss" scoped>
body {
font-family: 'Poppins', sans-serif;
font-weight: 300;
font-size: 15px;
line-height: 1.7;
color: #c4c3ca;
background-color: #1f2029;
overflow-x: hidden;
}
a {
  cursor: pointer;
  transition: all 200ms linear;
}
a:hover {
  text-decoration: none;
}
p {
  font-weight: 500;
  font-size: 14px;
  line-height: 1.7;
}
h4 {
  font-weight: 600;
  color: #c4c3ca;
}
h6 span {
  padding: 0 20px;
  text-transform: uppercase;
  font-weight: 700;
  color: #102770;
}

.card-front{
  background-color: #2a2b38;
  background-image: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/1462889/pat.svg");
  background-position: bottom center;
  background-repeat: no-repeat;
  background-size: 300%;
  border-radius: 6px;
}

.form-group {
  position: relative;
  display: block;
  margin: 0;
  padding: 0;
}
.form-style {
  padding: 13px 20px;
  padding-left: 55px;
  height: 48px;
  width: 100%;
  font-weight: 500;
  border-radius: 4px;
  font-size: 14px;
  line-height: 22px;
  letter-spacing: 0.5px;
  outline: none;
  color: #c4c3ca;
  background-color: #1f2029;
  border: none;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21, 21, 21, 0.2);
}
.form-style:focus,
.form-style:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21, 21, 21, 0.2);
}

.form-group input:-ms-input-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input::-moz-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input:-moz-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input::-webkit-input-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input:focus:-ms-input-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input:focus::-moz-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input:focus:-moz-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input:focus::-webkit-input-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.input-icon {
  position: absolute;
  top: 0;
  left: 18px;
  height: 48px;
  font-size: 24px;
  line-height: 48px;
  text-align: left;
  color: #ffeba7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.btn {
  border-radius: 4px;
  height: 44px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  padding: 0 30px;
  letter-spacing: 1px;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-align-items: center;
  -moz-align-items: center;
  -ms-align-items: center;
  align-items: center;
  -webkit-justify-content: center;
  -moz-justify-content: center;
  -ms-justify-content: center;
  justify-content: center;
  -ms-flex-pack: center;
  text-align: center;
  border: none;
  background-color: #ffeba7;
  color: #102770;
  box-shadow: 0 8px 24px 0 rgba(255, 235, 167, 0.2);
}
.btn:active,
.btn:focus {
  background-color: #102770;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16, 39, 112, 0.2);
}
.btn:hover {
  background-color: #102770;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16, 39, 112, 0.2);
}
  </style>