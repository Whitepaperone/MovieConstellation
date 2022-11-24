<template>
    <div class="">
        <PlayListItemVue
            v-for="playlist in playlists"
            :key="playlist.id"
            :playlist="playlist"
        />
    </div>
</template>

<script>
import PlayListItemVue from './PlayListItem.vue';

export default {
    name: 'PlayListList',
    components: {
        PlayListItemVue,
    },
    computed: {
        playlists() {
            return this.$store.state.playlists
        }
    }
}
</script>
  
<style scoped>
</style>