<template>
  <div>
    <p @click="print">components followers.vue user = {{user}}</p>
    <p>components followings = {{user.followings.length}}</p>
  </div>
</template>

<script>
export default {
  name: 'Followers',
  props: {
    user: Object
  },
  data() {
    return {
      
    }
  },
  methods: {
    print() {
      console.log(user)
    }
  }

}
</script>

<style>

</style>