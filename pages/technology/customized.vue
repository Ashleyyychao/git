<template>
  <div class="container" style='max-width:1170px'>
    <div
      class="d-flex flex-column align-center text-center py-6"
      style="margin: auto"
    >
      <div style='font-size:26px;'>台日核心技術服務團隊</div>
      <div style='font-size:26px'>一</div>
      <div class=' py-6' style='font-size:18px'>
        台灣正裕與日本西村形成跨國研究聯盟，彼此分享交流最新的塗模劑科技，當我們的客戶遇到技術問題時，可以同時享有台日兩大塗模劑領導品牌台日核心技術服務團隊。
      </div>
      <div class='d-flex py-6' style='width:100%' :class="`${windowWidth < 900 ? 'flex-column' : ''}`">
        <div class='pa-4'  :style="`${windowWidth < 900 ? '' : 'width: 50%'}`"><v-img :src="require('~/assets/img/custom4.jpg')"></v-img></div>
        <div  :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
          <div class='pa-4'><v-img :src="require('~/assets/img/custom5.jpg')"></v-img></div>
          <div class='pa-4'><v-img :src="require('~/assets/img/custom6.jpg')"></v-img></div>
        </div>
      </div>
    </div>
    <!-- 跨國策略聯盟 -->
    <div
      class="d-flex flex-column align-center text-center py-6"
      style="margin: auto"
    >
      <div style='font-size:26px;'>跨國策略聯盟</div>
       <div style='font-size:26px'>一</div>

      <div class="d-flex py-6" :class="`${windowWidth < 900 ? 'flex-column align-center' : 'justify-space-around'}`" style="width:100%;">
       
          <div class="pa-4" :style="`${windowWidth < 900 ? '' : 'width: 30%'}`">
            <div style='font-size:30px;color:#ffc005;font-weight: bold'>01</div>
            <div  class='pt-5' style='font-size:16px;letter-spacing: 10px;font-weight:bold'>日本技術</div>
            <div class='py-5' style='font-size:16px;'>專注先進科技、難題技術支援</div>
            <div>
              <v-img :src="require('~/assets/img/custom7.jpg')"></v-img>
            </div>
          </div>
          <v-icon v-if='windowWidth<900' style="color: #ffc005; font-size: 50px; font-weight: bold"
              >mdi-chevron-down</v-icon>
          <div class="pa-4" :style="`${windowWidth < 900 ? '' : 'width: 30%'}`">
            <div style='font-size:30px;color:#ffc005;font-weight: bold'>02</div>
            <div   class='pt-5' style='font-size:16px;letter-spacing: 10px;font-weight:bold'>臺灣生產</div>
            <div  class='py-5' style='font-size:16px;'>專注生產、品管、技術支援</div>
            <div>
              <v-img :src="require('~/assets/img/custom8.jpg')"></v-img>
            </div>
          </div>
           <v-icon v-if='windowWidth<900' style="color: #ffc005; font-size: 50px; font-weight: bold"
              >mdi-chevron-down</v-icon>
          <div class="pa-4" :style="`${windowWidth < 900 ? '' : 'width: 30%'}`">
            <div style='font-size:30px;color:#ffc005;font-weight: bold' >03</div>
            <div class='pt-5' style='font-size:16px;letter-spacing: 10px;font-weight:bold'>海外代理商</div>
            <div class='py-5' style='font-size:16px;'>技術服務、問題回報</div>
            <div>
              <v-img :src="require('~/assets/img/custom9.jpg')"></v-img>
            </div>
          </div>

      </div>
    </div>
    <!-- 政府和學術單位合作開發案 -->
    <div
      class="d-flex flex-column align-center text-center py-6"
      style="margin: auto"
    >
        <div style='font-size:26px;'>政府和學術單位合作開發案</div>
      <div style='font-size:26px'>一</div>
      <div class='py-6'>
        我們經常和台灣金屬中心以及經濟部技術處進行技術開發專案，幫助提升台灣鑄造科技，包括水性環保砂模塗模劑與水性消失模塗模劑等專案，提供政府與學術單位專業諮詢與材料支援。
      </div>
      <div class="d-flex justify-center py-6" style="width: 50%; margin: auto">
        <div style="width: 50%">
          <v-img  width='254px' height="87px" :src="require('~/assets/img/MIRDC.jpg')"></v-img>
        </div>
        <div style="width: 50%">
          <v-img width='254px' height="87px" :src="require('~/assets/img/DOIT.jpg')"></v-img>
        </div>
      </div>
    </div>
    <!-- 獲獎經歷 -->
    <div
      class="d-flex flex-column align-center text-center py-6"
      style="margin: auto"
    >
      <div style='font-size:26px;'>獲獎經歷</div>
      <div style='font-size:26px'>一</div>

      <div class='py-6'>
        正裕化工技術部經理吳政翰先生，成功開發友善環境之水性消失模與砂模塗模劑，榮獲台灣區鑄造品工業同業公會頒發，民國102年度優秀鑄造經理人獎。
      </div>
      <div
        class="d-flex flex-column align-center py-6"
        style="width: 50%; margin: auto"
      >
        <div style='width:370px'><v-img :src="require('~/assets/img/custom10.jpg')"></v-img></div>
        <div class='py-6' style='font-size:18px'>
          正裕化工專案經理吳政頡先生，因協助多間鑄造廠進行塗模劑改善與品質提升計畫，榮獲台灣區鑄造品工業同業公會頒發，民國106年度優秀鑄造經理人獎。
        </div>
        <div class='py-6' style='width:370px'><v-img :src="require('~/assets/img/award2.jpg')"></v-img></div>
      </div>
    </div>
  </div>
</template>
<script>
import uiFunctions from "~/mixins/uiFunctions";
export default {
    mixins: [uiFunctions],
}
</script>