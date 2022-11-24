<template>
  <div
    :class="[{isselected:selected}, {isnotselected:!selected}]"
    @click="cancleLine"
    style="margin-left:1rem; margin-right:1rem;">
    {{ movie.title }}
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
    movie: Object
  },
  data() {
    return {
      selected: false,
    }
  },
  methods: {
    cancleLine() {
      this.selected = !this.selected
    }
  }

}
</script>

<style scoped>
.isselected{
  text-decoration-line: line-through;
  color: gray;
  background-color:rgb(200, 200, 200);
} 
.isnotselected{
  background-color:rgb(224, 224, 224);
}
</style>