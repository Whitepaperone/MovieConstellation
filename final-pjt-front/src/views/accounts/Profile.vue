<template>
    <div>
        <h1>{{ username }}'s Profile</h1>
        <div>
            <FollowersVue
                :user="user"
            />
        </div>
    </div>
</template>

<script>
import FollowersVue from '@/components/profile/Followers.vue'
export default {
name: 'Profile',
components: {
    FollowersVue,
},
data() {
    return {
        // user : localStorage.getItem('user'),
        user: null,
        username : null
    }
},
computed: {
    
},
methods: {
    getUserName() {
        this.username = this.$store.state.username
    },
    getUserInfo() {
        this.user=this.$store.state.user
    }
},
created() {
    this.getUserName()
    this.getUserInfo()
}
}
</script>

<style>

</style>