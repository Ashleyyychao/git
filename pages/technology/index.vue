<template>
  <div class="container d-flex" style=" max-width: 1170px">
    <div class="d-flex flex-column" style="width:80%;margin: auto">
      <!-- step-1 -->
      <div>
        <div class='pa-8'>
          <div
            class="text-center"
            style="color: #ffc005; font-size: 30px; font-weight: bold"
          >
            Step1
            <br />
            <v-icon style="color: #ffc005; font-size: 30px; font-weight: bold"
              >mdi-chevron-down</v-icon
            >
          </div>
          <div class="text-center pt-3" style="font-size: 26px; font-weight: bold;font-family:source-han-serif-tc;letter-spacing: 10px;">
            嚴選原料
          </div>
        </div>
        <div class="d-flex py-8" style="width: 100%" :class="`${windowWidth < 900 ? 'flex-column' : ''}`">
          <div class='pr-7' :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <v-img
              :src="require('~/assets/img/quality1514971823896602.jpg')"
            ></v-img>
          </div>
          <div class="d-flex flex-column " :class="`${windowWidth < 900 ? 'py-6' : 'pl-7'}`" :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <div style='font-size:24px'>原礦與加工</div>
            <div style='font-size:24px'>一</div>
            <div style='font-size:18px'>
              絕佳的塗模劑，來自於絕佳的耐火礦物。我們總是親自深入原礦產區，找尋耐火度最佳的礦源，長期監測成分指標，審慎與加工廠訂出研磨規範，確保最完美的粒度分布。我們隨時準備上千噸的原料庫存，甚至和礦場預先包下整層蘊藏量高達數千噸的礦脈，只為搶得適合塗模劑使用的特殊礦源。
            </div>
          </div>
        </div>
        <div class="d-flex py-8" style="width: 100%" :class="`${windowWidth < 900 ? 'flex-column' : ''}`">
          <div class='pr-7' :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <v-img
              :src="require('~/assets/img/quality1515030394059367.jpg')"
            ></v-img>
          </div>
          <div class="d-flex flex-column" :class="`${windowWidth < 900 ? 'py-6' : 'pl-7'}`" :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <div style='font-size:24px'>頂尖化學科技</div>
            <div style='font-size:24px'>一</div>
            <div style='font-size:18px'>
              塗模劑是高度複合型的產品，我們長期和日本及全球頂尖化學公司保持密切合作關係，我們塗模劑所使用的化學材料，來自包括航太、半導體、製藥等多項先進產業，以新科技，不斷突破塗模劑的效能極限。
            </div>
          </div>
        </div>
      </div>
      <!-- step-2 -->
      <div>
         <div class='pa-8'>
          <div
            class="text-center"
            style="color: #ffc005; font-size: 30px; font-weight: bold"
          >
            Step2
            <br />
            <v-icon style="color: #ffc005; font-size: 30px; font-weight: bold"
              >mdi-chevron-down</v-icon
            >
          </div>
          <div class="text-center pt-3" style="font-size: 26px; font-weight: bold;font-family:source-han-serif-tc;letter-spacing: 10px;">
            混料製程
          </div>
        </div>
        <div class="d-flex py-8" style="width: 100%" :class="`${windowWidth < 900 ? 'flex-column' : ''}`">
          <div class='pr-7' :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <v-img
              :src="require('~/assets/img/quality1515030632843367.jpg')"
            ></v-img>
          </div>
          <div class="d-flex flex-column " :class="`${windowWidth < 900 ? 'py-6' : 'pl-7'}`" :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <div style='font-size:24px'>日本工匠級製程-追求完美</div>
            <div style='font-size:24px'>一</div>
            <div style='font-size:18px'>
              我們整體的生產設備都是由日本西村黑鉛株式會社規畫、設計與技術移轉，傳承發展近百年的塗料生產工藝，製藥級的重型混料設備，力求每一微粒的耐火礦粉和化學材料都能完美的結合，發揮最大的複合綜效。
            </div>
          </div>
        </div>
        <div class="d-flex py-8" style="width: 100%" :class="`${windowWidth < 900 ? 'flex-column' : ''}`">
          <div class='pr-7' :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <v-img
              :src="require('~/assets/img/quality1515030735107867.jpg')"
            ></v-img>
          </div>
          <div class="d-flex flex-column " :class="`${windowWidth < 900 ? 'py-6' : 'pl-7'}`" :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <div style='font-size:24px'>自動化生產線-精準、效率</div>
            <div style='font-size:24px'>一</div>
            <div style='font-size:18px'>
              2013年建造，以最先進的電腦控制系統，進行所有的集料與送料作業，系統以克為單位，精準監控所有配料流程，將不良率降至接近於零，並大幅提升三倍以上產能，透過此系統，所有產品皆有詳實的電腦生產紀錄，給予客戶最放心穩定的產品品質。
            </div>
          </div>
        </div>
      </div>
      <!-- step3 -->
      <div>
         <div class='pa-8'>
          <div
            class="text-center"
            style="color: #ffc005; font-size: 30px; font-weight: bold"
          >
            Step3
            <br />
            <v-icon style="color: #ffc005; font-size: 30px; font-weight: bold"
              >mdi-chevron-down</v-icon
            >
          </div>
          <div class="text-center pt-3" style="font-size: 26px; font-weight: boldf;ont-family:source-han-serif-tc;letter-spacing: 10px;">
            包裝品檢
          </div>
        </div>
        <div class="d-flex py-8" style="width: 100%" :class="`${windowWidth < 900 ? 'flex-column' : ''}`">
          <div class='pr-7' :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <v-img
              :src="require('~/assets/img/quality1515030798901867.jpg')"
            ></v-img>
          </div>
          <div class="d-flex flex-column " :class="`${windowWidth < 900 ? 'py-6' : 'pl-7'}`" :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <div style='font-size:24px'>源頭控管</div>
            <div style='font-size:24px'>一</div>
            <div style='font-size:18px'>
              我們有豐富的四十年耐火礦物檢測經驗和專業耐火塗料實驗室，所有的礦物與化學原料在進倉前，皆須抽樣並通過1700度高溫爐高溫測試，詳細檢驗燒失量、觀察高溫結晶體等方式，用以斷定是否符合標準，方可入庫投產。
            </div>
          </div>
        </div>
        <div class="d-flex py-8" style="width: 100%" :class="`${windowWidth < 900 ? 'flex-column' : ''}`">
          <div class='pr-7' :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <v-img
              :src="require('~/assets/img/quality1515030845161867.jpg')"
            ></v-img>
          </div>
          <div class="d-flex flex-column" :class="`${windowWidth < 900 ? 'py-6' : 'pl-7'}`" :style="`${windowWidth < 900 ? '' : 'width: 50%'}`">
            <div style='font-size:24px'>出廠檢驗</div>
            <div style='font-size:24px'>一</div>
            <div style='font-size:18px'>
              所有出產的產品皆須經過抽樣品檢，方可進行入庫與出貨作業，我們會測試塗料的各項性能，包含懸浮性、垂流性、濃度、比重、色澤等多項測試，通過測試合格，方可進行入庫與出貨。
            </div>
          </div>
        </div>
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

<style scoped>
</style>