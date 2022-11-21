<template>
  <div class="mx-5">
    <div class="card" style="width: 20rem;">
        <h5 class="card-title"><b>
        <router-link :to="{ name: 'Profile' , params: { username : follow.username} }">[Profile]</router-link>
          {{ follow.username }}</b></h5>
    </div>
  </div>
</template>

<script>
export default {
name: 'MovieViewCard',
  props: {
    follow: Object
  },
  data() {
    return {
      username: this.follows.username,
    }
  },
}
</script>

<style>

</style>