<template>
  <div></div>
</template>

<script>
export default {
  name: 'Logout',
  data() {
    return {}
  },
  methods: {
    logOut() {
      if (localStorage.getItem('jwt')) {
        this.$store.commit('REMOVE_USER')
        localStorage.removeItem('jwt')
        localStorage.removeItem('username')
        this.$emit('logout')
        this.$router.push({name: 'Login'})
      } else {
        this.$router.push({name: 'Login'})
      }
    }
  },
  created() {
    this.logOut()
  },

}
</script>

<style>

</style>