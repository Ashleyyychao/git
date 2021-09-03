<template>
  <div class="container">
    <div>塗模劑應用</div>
    <div>鑄鋼領域</div>
    <div class="d-flex flex-wrap" style='width:100%'>
      <div  style='width:25%' >
        <div>
          <v-img
            :src="require('~/assets/img/application_pic1515042878004423.jpg')"
          ></v-img>
        </div>
        <div>各類碳鋼／不銹鋼／合金鋼</div>
      </div>
      <template  v-for="(item, index)  in items">
       <div  style='width:25%' :key="index">
        <div style='width:100%'>
          <v-img
            :src="item.img"
          ></v-img>
        </div>
        <div>{{ item.title }}</div>
      </div>
      </template>
    </div>
  </div>
</template>
<script>

export default {
data(){
return {
    items:{
        title:'各類碳鋼／不銹鋼／合金鋼',img:"require('~/assets/img/application_pic1515042878004423.jpg')"

    }
}
}
}
</script>
