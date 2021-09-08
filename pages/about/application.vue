<template>
  <div >
    <div class="container" style="max-width: 1170px;padding:50px 0px">
      <div class="pa-10">
        <div
          class="text-center"
          style="font-family: 'source-han-serif-tc';font-size: 20px;color: #ffc005;font-weight: bold;margin-bottom: 22px;"
        >
          塗模劑應用
        </div>
        <div
          class="text-center"
          style="
            font-family: 'source-han-serif-tc';
            font-size: 26px;
            font-weight: bold;
            letter-spacing: 10px;
          "
        >
          鑄鋼領域
        </div>
      </div>
      <div
        class="d-flex flex-wrap"
        :class="`${windowWidth < 900 ? 'flex-column' : 'flex-wrap'}`"
      >
        <div
          class="pa-4"
          :style="`${windowWidth < 900 ? 'width:100%' : 'width:25%'}`"
          v-for="(item, index) in data"
          :key="index"
        >
          <div>
            <v-img :src="item.img"></v-img>
          </div>
          <div class="pa-4" style='font-size:18px'>{{ item.title }}</div>
        </div>
      </div>
    </div>
    <v-divider></v-divider>
    <div class="container" style="max-width: 1170px;padding:50px 0px">
      <div class="pa-10">
        <div
          class="text-center"
          style="
            font-family: 'source-han-serif-tc';
            font-size: 20px;
            color: #ffc005;
            font-weight: bold;
            margin-bottom: 22px;
          "
        >
          塗模劑應用
        </div>
        <div
          class="text-center"
          style="
            font-family: 'source-han-serif-tc';
            font-size: 26px;
            font-weight: bold;
            letter-spacing: 10px;
          "
        >
          鑄鋼領域
        </div>
      </div>
      <div
        class="d-flex flex-wrap"
        :class="`${windowWidth < 900 ? 'flex-column' : 'flex-wrap'}`"
      >
        <div
          class="pa-4"
          :style="`${windowWidth < 900 ? 'width:100%' : 'width:25%'}`"
          v-for="(item, index) in data2"
          :key="index"
        >
          <div>
            <v-img :src="item.img"></v-img>
          </div>
          <div class="pa-4" style='font-size:18px'>{{ item.title }}</div>
        </div>
      </div>
    </div>
    <v-divider></v-divider>
     <div class="container" style="max-width: 1170px;padding:50px 0px 150px">
      <div class="pa-10">
        <div
          class="text-center"
          style="
            font-family: 'source-han-serif-tc';
            font-size: 26px;
            font-weight: bold;
            letter-spacing: 10px;
          "
        >
          石墨應用領域

        </div>
      </div>
      <div
        class="d-flex flex-wrap"
        :class="`${windowWidth < 900 ? 'flex-column' : 'flex-wrap'}`"
      >
        <div
          class="pa-4"
          :style="`${windowWidth < 900 ? 'width:100%' : 'width:25%'}`"
          v-for="(item, index) in data3"
          :key="index"
        >
          <div>
            <v-img :src="item.img"></v-img>
          </div>
          <div class="pa-4" style='font-size:18px'>{{ item.title }}</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import uiFunctions from "~/mixins/uiFunctions";
export default {
  mixins: [uiFunctions],
  middleware: 'metaTitle',
  meta: {title: '產品應用產業',redirect: '/about/application'},
  data() {
    return {
      data: [
        {
          img: require("~/assets/img/application_pic1515042878004423.jpg"),
          title: "各類碳鋼／不銹鋼／合金鋼",
        },
        {
          img: require("~/assets/img/image-YXBwbGljYXRpb25fcGlj--application_pic1515042879880423.jpg"),
          title: "各類碳鋼／不銹鋼／合金鋼",
        },
        {
          img: require("~/assets/img/application_pic1515042881293423.jpg"),
          title: "高錳鋼／耐磨製品",
        },
        {
          img: require("~/assets/img/application_pic1515042882829423.jpg"),
          title: "離心鑄造",
        },
        {
          img: require("~/assets/img/application_pic1515042884359423.jpg"),
          title: "離心鑄造",
        },
        {
          img: require("~/assets/img/application_pic1515042885730423.jpg"),
          title: "離心鑄造",
        },
        {
          img: require("~/assets/img/application_pic1515042887134423.jpg"),
          title: "大型鑄鋼件",
        },
      ],
      data2:[
          {
          img: require("~/assets/img/application_pic1515043637427875.jpg"),
          title: "風力發電／球墨鑄鐵",
        },
         {
          img: require("~/assets/img/application_pic1515043640243151.jpg"),
          title: "汽車產業",
        },
         {
          img: require("~/assets/img/application_pic1515043641769304.jpg"),
          title: "汽車產業",
        },
         {
          img: require("~/assets/img/application_pic1515043643395464.jpg"),
          title: "大型鑄鐵",
        },
         {
          img: require("~/assets/img/application_pic1515043644889611.jpg"),
          title: "工具機鑄件",
        },
         {
          img: require("~/assets/img/application_pic1515043646271747.jpg"),
          title: "工具機鑄件",
        },

      ],
      data3:[
        {
          img: require("~/assets/img/application_pic1515043894109011.jpg"),
          title: "焊材",
        },
        {
          img: require("~/assets/img/application_pic1515043899949748.jpg"),
          title: "耐火",
        },
        {
          img: require("~/assets/img/application_pic1515043906860035.jpg"),
          title: "導電",
        },
        {
          img: require("~/assets/img/application_pic1515043909190130.jpg"),
          title: "潤滑",
        },

      ]
    };
  },
};
</script>
