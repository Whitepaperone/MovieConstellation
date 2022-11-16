<template>
  <div>
    <div class="mx-3 p-3" style="margin-top: 50px; background-color: #e3f2fd;">
      <h1>보고싶은 영화</h1>
      <input
        class="mt-3"
        type="text"
        v-model.trim="inputData"
        @keyup.enter="addMovie"
      >
      <button
        type="button" class="btn btn-outline-primary"
        style="margin-left:16px;"
        @click="addMovie"
      >
        add
      </button>
    </div>
    <div class="m-0">
      <WatchListItemVue
        v-for="movie in movieList"
        :key = movie.id
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import WatchListItemVue from './WatchListItem.vue';
export default {
  name: 'WatchList',
  components: {
    WatchListItemVue
  },
  data() {
    return {
      id: 0,
      inputData: '',
    }
  },
  computed: {
    movieList() {
      return this.$store.state.picked
    }
  },
  methods: {
    addMovie() {
      this.movieList.push({title:this.inputData, id:this.id})
      this.id = this.id+1
      this.inputData=''
    }
  }
}
</script>

<style>

</style>