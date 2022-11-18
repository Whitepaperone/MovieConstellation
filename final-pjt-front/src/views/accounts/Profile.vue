<template>
    <div>
        <h1>{{ username }}'s Profile</h1>
        <p>profile.vue user = {{user}}</p>
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
props: {
    user: Object
},
data() {
    return {
    }
},
computed: {
    
},
methods: {
    getUserName() {
        this.username = localStorage.getItem('username')
    },
},
created() {
    this.getUserName()
}
}
</script>

<style>

</style>