<template>
  <div class="movie mx-1 px-3">{{movie.title}}</div>
</template>

<script>
export default {
  name: 'ProfilePlaylistItem',
  props: {
    movie : Object,
  }
}
</script>

<style scoped>
.movie{
  background-color: #ffeba7;
  border-radius: 20px;
  padding-top: 2px;
  color: #102770;
}
</style>