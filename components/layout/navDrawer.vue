<template>
  <div class="container">
   <div class="topbar d-flex pt-10">
      <div class="logo">
        <v-img
          width="356px"
          height="53px"
          :src="require('~/assets/img/logo.png')"
        ></v-img>
      </div>
      <v-spacer></v-spacer>
      <div class='d-flex align-center'>
        <div class='pr-6'>
          <a href="" class='pa-2' style='font-weight: bold;color:#000000;'>En</a>
          <a href="" class='pa-2' style='font-weight: bold;color:#000000'>繁中</a>
        </div>
        <button>客戶專區</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  background-color: rgb(130, 131, 131);
}
a {
  text-decoration: none;
  color: #000000;
  font-weight: bold;
  border-right:8px;

}

button {
  border: 1px solid #000000;
  padding: 15px 35px;
}
</style>
