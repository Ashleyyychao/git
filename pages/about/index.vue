<template>
  <div class="banner" style="width: 100%">
    <div class="container" style="max-width: 1170px; width: 100%">
      <div
        class="pb-15"
        style="width: 33%; min-width: 385px; margin: 100px 120px"
      >
        <div
          style="
            font-size: 35px;
            line-height: 45px;
            color: #ffc005;
            margin-bottom: 35px;
            font-weight: bold;
          "
        >
          創立於西元1970年，<br />
          為台灣耐火材料之先驅
        </div>
        <div style="color: #fff; font-size: 18px; line-height: 28px !important">
          從石墨批發開始做起，逐漸擴大到各類鑄造用耐火材料。四十多年來不斷精進努力，累積了厚實的技術實力及良好的信譽，成為台灣鑄造塗模劑領導品牌。
        </div>
      </div>
      <div>
        <div class="d-flex" style="width: 100%">
          <div style="width: 50%">
            <v-img :src="require('~/assets/img/about-box-1.jpg')"></v-img>
          </div>
          <div style="width: 50%; background-color: #f9b233;padding:70px">
            <div class='font-weight-bold' style='font-size: 35px;margin-bottom: 16px;'>高品質鑄造塗模劑的代名詞</div>
            <div>
              正裕化工於1980年初期，正式代理於日本擁有近百年歷史的西村黑鉛株式會社之各項鑄造塗模劑產品，更率先取得日本授權，於台灣建置生產工廠，開始大量生產，大幅提升台灣鑄造塗模劑之水準，擁有良好的口碑與市占率。
            </div>
          </div>
        </div>
        <div>
          <div class="d-flex" style="width: 100%">
            <div style="width: 50%; background-color: #000000; color: white;padding:70px">
              <div class='font-weight-bold' style='font-size: 35px;margin-bottom: 16px;'>亞太地區最專業<br/>鑄造塗模劑生產中心</div>
              <div style="color: white">
                為追求品質的最佳化和加大整體產能，於2013年，和西村聯手建置了先進的電腦自動化生產系統，此系統結合了日本工匠精神與台灣先進的電控系統，將傳承了百年的鑄造塗料經驗，進行最完美的昇華，成為西村最重要的海外生產基地，也是亞太地區最專業的鑄造塗模劑生產中心。
              </div>
            </div>
            <div style="width: 50%">
              <v-img :src="require('~/assets/img/about-box-2.jpg')"></v-img>
            </div>
          </div>
        </div>
        <div class="section d-flex justify-end" style="width: 100%"> 
          <div class='d-flex flex-column justify-center' style="width: 50%;padding:70px">
            <div
              style="
                font-size: 35px;
                line-height: 45px;
                color: #ffc005;
                margin-bottom: 35px;
                font-weight: bold;
              "
            >
              不畏鑄造的艱難挑戰，<br />
              長期深耕鑄造用塗模劑領域
            </div>
            <div
              style="color: #fff; font-size: 18px; line-height: 28px !important"
            >
              不斷推出符合各種產業鑄件需求的專業化塗料，並提供客製化的服務。此外，我們也樂於和客戶長期合作，一同解決鑄造上的難題，共同開創技術先河，不負客戶對我們產品的期望，實踐勇赴熔焰，成就完美的精神。
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  name: "AboutUs",
  middleware: 'metaTitle',
  meta: {title: '公司簡介',redirect: '/about/index'},
}
</script>
<style scoped>
.banner {
  padding: 0px;
  margin:0px;
  background-image: url("../../assets/img/indexbanner.jpg");
  background-position: top;
  background-size: 100% 690px;
}
.section {
  background-image: url("../../assets/img/about-box-3.jpg");
  background-size: cover;
  height:625px
}
</style>

