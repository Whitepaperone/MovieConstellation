<template>
  <div class="container">
    <div class="row">
      <div class="box col">
        <div class="shadow"></div>
        <div class="content">
            {{inter_per()}}    
          <div class="percent" data-text="Same" :style="`--num: ${tmp}`">
            <div class="dot"></div>
            <svg>
              <circle cx="70" cy="70" r="70"></circle>
              <circle cx="70" cy="70" r="70"></circle>
            </svg>
            <div class="number">
              <h2>{{tmp}}<span>%</span></h2>
            </div>
          </div>
        </div>    
      </div>
    </div> 
    <div class="row col movie_div mx-2 p-4 d-flex justify-content-center">
      <div class="d-flex justify-content-align ps-0 mb-3">
        <h1 class="text-center px-2" style="padding-top:6px">겹치는 영화</h1>
      </div>
      <div class="d-flex row justify-content-center align-self-center moviecardzone " style="overflow:scroll; width:900px; height: 480px; ">
        <MovieViewCard
        class="justify-content-center"
              v-for="movie in movies.intersection"
              :key="movie.id"
              :movie="movie"
            />
      </div>
    </div>
    <div class="row movie_div mx-2 p-4 d-flex justify-content-center">
      <div class="d-flex justify-content-align ps-0 mb-3">
        <h1 class="text-center px-2" style="padding-top:6px">  {{ this.$route.params.username }}님이 좋아하는 영화는 어떠세요?</h1>
      </div>
      <div class=" d-flex row justify-content-center moviecardzone" style="overflow:scroll; width:900px; height: 480px;">
       
        <MovieViewCard
          class="justify-content-center"
          v-for="movie in movies.b_complement"
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>
  </div>
      <!-- <div class="col-1">

        <div class="box">
      
        <div class="shadow"></div>
            <div class="content">
                {{inter_per()}}    
              <div class="percent" data-text="Same" :style="`--num: ${tmp}`">
                <div class="dot"></div>
                <svg>
                  <circle cx="70" cy="70" r="70"></circle>
                  <circle cx="70" cy="70" r="70"></circle>
                </svg>
              <div class="number">
                <h2>{{tmp}}<span>%</span></h2>
              </div>
            </div>
            </div>

              
        </div>
      </div> -->
     

</template>

<script>
import MovieViewCard from '@/views/movie/MovieViewCard'
import axios from 'axios'
export default {
  name: 'CombinationView',
  components: {
    MovieViewCard,
  },
  props:{
    comuser:Object
  },
  data(){
    return{
      movies:[],
      number:1,
      total_n:0,
      a_set_len:0,
      b_set_len:0,
      inter_len:0,
      tmp:0
    }
  },
 
  methods:{
    combinationMovie(){
      const user_id=this.comuser.a
      const another_user_id=this.comuser.b

      console.log(another_user_id,user_id)
       axios({
          method: 'get',
          url : `http://127.0.0.1:8000/movies/${user_id}/combination/${another_user_id}`,

        })
        .then((response) => {
          this.movies=response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    a_set(){
      this.a_set_len=this.movies.a_complement.length
      return this.a_set_len
    },
    b_set(){
      this.b_set_len=this.movies.b_complement.length
      return this.b_set_len
    },
    intersection(){
      this.inter_len=this.movies.intersection.length
      
      return this.inter_len
    },
    total(){
      var a=this.a_set()
      var b=this.b_set()
      var inter=this.intersection()
      this.total=a+b+inter
      return this.total
    },
    inter_per(){
      var inter=this.intersection()
      var total=this.total()
      var a=(inter/total)*100
      this.tmp=Math.floor(a)
    },
  },
  created(){
    this.combinationMovie()
    this.inter_per()
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@100;300;400;500;600;700;800;900&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

.container {
  width: 100%;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 80px 100px;
  overflow: hidden;
}

.box {
  position: relative;
  width: 240px;
  height: 250px;
  display: flex;
  justify-content: center;
  align-items: center;
}


.box .content .percent {
  position: relative;
  width: 150px;
  height: 150px;
}

.box .content .percent::before {
  content: attr(data-text);
  position: absolute;
  inset: 20px;
  background: #555;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
  font-size: 1.75rem;
  letter-spacing: 0.1rem;
  text-transform: uppercase;
}

.box .content .percent svg {
  position: relative;
  width: 150px;
  height: 150px;
  transform: rotate(270deg);
}

.box .content .percent svg circle {
  width: 100%;
  height: 100%;
  fill: transparent;
  stroke-width: 3;
  stroke: rgba(0,0,0,0.05);
  transform: translate(5px, 5px);
}

.box .content .percent svg circle:nth-child(2) {
  stroke: #555;
  stroke-dasharray: 440;
  stroke-dashoffset: calc(440 - (440 * var(--num)) / 100);
  opacity: 0;
  animation: fadeIn 1s linear forwards;
  animation-delay: 2.5s;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.box .content .percent .dot {
  position: absolute;
  inset: 5px;
  z-index: 10;
  animation: animateDot 2s linear forwards;
}

@keyframes animateDot {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(calc(3.6deg * var(--num)));
  }
}

.box .content .percent .dot::before {
  content: '';
  position: absolute;
  top: -7px;
  left: 50%;
  transform: translateX(-50%);
  width: 14px;
  height: 14px;
  background: #555;
  border-radius: 50%;
}

.box .content .number {
  position: relative;
  inset: 0;
  opacity: 0;
  animation: fadeIn 1s linear forwards;
  animation-delay: 2.5s;
}

.box .content .number h2 {
  font-size: 2.5rem;
  color: rgb(255, 255, 255);
  text-shadow: 1px 0 10px #555;
}

.box .content .number h2 span {
  font-weight: 300;
  font-size: 1.5rem;
}
</style>

<style lnag="ssas" scoped>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');
.scrollbar{
  overflow-x:hidden;
}
::-webkit-scrollbar{
  display: none;
}
.movie_div{
  background-color: rgba(159, 157, 157, 0.5);
  border-radius: 10px;
}
.moviecardzone {
  background-color: rgba(226, 226, 226, 0.095);
  border-radius: 10px;
}
h1 {
  font-family: 'Black Han Sans', sans-serif;
  color: rgb(35, 35, 35);
  width:auto;
  background-color: rgba(226, 226, 226, 0.095);
  border-radius: 10px;
}
</style>