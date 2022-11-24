<template>
    <div class="playlist m-2">
      <div>
        <div class="p-2">
          <h5 class="playlisttitle px-2 py-1" style="width:fit-content;">{{playlist?.title}}</h5>
        </div>
        <div class="playcontent d-flex">
          <span class="ms-3">
            <p>{{playlist?.content}}</p>
          </span>
          <span class="ms-3">
            <router-link
              :to="{
                name: 'PlayListDetailView',
                params: {id:playlist.id}
              }"
            >
              <i class="icon bi bi-box-arrow-in-right"></i>
            </router-link>
          </span>
        </div>

      </div>
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
  
  <style scoped>
  /* div{
    border: 1px solid;
    border-color: red;
  }
span {
  border: 1px solid;
  border-color: yellow;
} */
.icon {
  font-size: 24px;
  color: #ffeba7;
}
.playlisttitle{
  color: #363636d0;
  width:auto;
  background-color: #a8a8a88a;
  border-radius: 10px;
}
.playlist{
  background-color: #a8a8a87a;
  border-radius: 10px;
  border: #1026709b solid 2px;
}
p{
  font-size: 20px;
  color: #171717d0;
}
  </style>