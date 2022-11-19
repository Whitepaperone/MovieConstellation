<template>
    <div>
      <h5>{{playlist.title}}</h5>
      <p>{{playlist.content}}</p>
      <router-link
        :to="{
          name: 'PlayListDetailView',
          params: {id:playlist.id}
        }"
      >
        [Detail]
      </router-link>
      <hr>
    </div>
  </template>
  
  <script>
  export default {
      name: 'PlayListItem',
      props: {
          playlist: Object
      }
  }
  </script>
  
  <style>
  
  </style>