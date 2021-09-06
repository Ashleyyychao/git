<template>
  <div class="container d-flex flex-row" style="max-width: 1170px">
    <div style="width: 30%" v-if='windowWidth>900'>
      <asideSection></asideSection>
    </div>
    <div :style="`${windowWidth > 900 ? 'width: 70%' : ''}`"
      >
      <div class="d-flex" style="100%" :class="`${windowWidth < 900 ? 'flex-column' : ''}`">
        <div  :style="`${windowWidth < 900 ? 'width: 80%' : 'width: 40%'}`">
          <v-img
            :src="require('~/assets/img/product1515378669651533.jpg')"
          ></v-img>
        </div>
        <div style="width: 60%" :class="`${windowWidth < 900 ? 'pa-6' : ''}`">
          <div style="font-size: 26px; margin: 0px 0px 30px">鑄鐵塗模劑</div>
          <div style="font-size: 18px; margin: 0px 0px 6px">
            產品特點:醇基泛用型石墨塗模劑(FK)系列
          </div>
          <div style="font-size: 18px">產品規格:TN-168</div>
        </div>
      </div>
      <v-divider></v-divider>

      <div class="d-flex" style="100%" :class="`${windowWidth < 900 ? 'flex-column' : ''}`">
        <div :style="`${windowWidth < 900 ? 'width: 80%' : 'width: 40%'}`">
          <v-img
            :src="require('~/assets/img/product1515378669651533.jpg')"
          ></v-img>
        </div>
        <div style="width: 60%" :class="`${windowWidth < 900 ? 'pa-6' : ''}`">
          <div style="font-size: 26px; margin: 0px 0px 30px">鑄鐵塗模劑</div>
          <div style="font-size: 18px; margin: 0px 0px 6px">
            產品特點:醇基泛用型石墨塗模劑(FK)系列
          </div>
          <div style="font-size: 18px">產品規格:TN-168</div>
        </div>
      </div>
      <v-divider></v-divider>

      <div class="d-flex" style="100%" :class="`${windowWidth < 900 ? 'flex-column' : ''}`">
        <div  :style="`${windowWidth < 900 ? 'width: 80%' : 'width: 40%'}`">
          <v-img
            :src="require('~/assets/img/product1515378669651533.jpg')"
          ></v-img>
        </div>
        <div style="width: 60%" :class="`${windowWidth < 900 ? 'pa-6' : ''}`">
          <div style="font-size: 26px; margin: 0px 0px 30px">鑄鐵塗模劑</div>
          <div style="font-size: 18px; margin: 0px 0px 6px">
            產品特點:醇基泛用型石墨塗模劑(FK)系列
          </div>
          <div style="font-size: 18px">產品規格:TN-168</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import asideSection from "~/components/section/asideSection";
import uiFunctions from "~/mixins/uiFunctions";

export default {
  components: { asideSection },
    mixins: [uiFunctions],
};
</script>
