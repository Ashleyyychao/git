<template>
  <div class="container" style='max-width:1170px' :style="`${windowWidth < 900 ? 'border-bottom:5px solid #ffc005' : ''}`">
   <div class="d-flex py-6">
      <div class="logo">
        <v-img
          width="356px"
          height="53px"
          :src="require('~/assets/img/logo.png')"
        ></v-img>
      </div>
      <v-spacer></v-spacer>
      <div class='d-flex align-center' v-if="windowWidth > 900">
        <div class='pr-6'>
          <a href="" class='pa-2' style='font-weight: bold;color:#000000;'>En</a>
          <a href="" class='pa-2' style='font-weight: bold;color:#000000'>繁中</a>
        </div>
        <button style=' border: 1px solid #000000;padding: 15px 35px;'>客戶專區</button>
      </div>
      <div v-else>
        <button>
         <v-icon large>mdi-menu</v-icon>
         </button>
      </div>
    </div>
    
  </div>
  
</template>
<script>
import uiFunctions from "~/mixins/uiFunctions";

export default {
  mixins:[uiFunctions],

}
</script>


<style scoped>

a {
  text-decoration: none;
  color: #000000;
  font-weight: bold;
  border-right:8px;

}
</style>
