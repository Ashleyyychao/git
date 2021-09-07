<template>
  <div class="container" style="max-width: 1170px; width: 100%; padding: 0px">
    <div>
      <div class="banner">
        <div>
          <div
            style="
              font-size: 50px;
              color: #fff;
              font-family: 'source-han-serif-tc';
              letter-spacing: 25px;
              padding:70px
              font-weight: 600;
            "
          >
            六十年<br />
            鑄造塗模劑專家，<br />
            台灣領導品牌<br /><sapn
              style="
                color: #ffc005;
                font-weight: bold;
                letter-spacing: 10px;
                font-size: 25px;
                line-height: 35px;
              "
              >勇赴熔焰，成就完美</sapn
            >
          </div>
        </div>
      </div>
      <div class="d-flex" style="width: 100%">
        <div
          class="banner1"
          style="width: 50%; min-height: 286px; position: relative"
        >
          <div style="position: absolute;right: 48px; bottom:48px;width:193px">
            <div
              style="
                font-family: 'source-han-serif-tc';
                font-size: 25px;
                font-weight: 700;
                margin-bottom: 10px;
              "
            >
              主要產品
            </div>
            <div>各式鑄造塗模劑、日本鑄造材料、耐火材料、鑄造材料</div>
            <div><nuxt-link to="/technology"><button style='color: #000000;padding:10px 27px;border:1px solid #000000;margin:25px 0px 0px'>詳細內容</button></nuxt-link></div>
          </div>
        </div>
        <div
          class="banner2"
          style="width: 25%; min-height: 286px; position: relative"
        >
          <div style="position: absolute; left: 50px;bottom:48px;width:193px">
            <div
              style="
                font-family: 'source-han-serif-tc';
                font-size: 25px;
                font-weight: 700;
                margin-bottom: 10px;
                color: #fff;
              "
            >
              品質管控
            </div>
            <div style='color: #fff;'>日本百年工匠級生產工法，導入台灣先進自動化製...</div>
            <div><nuxt-link to="/technology"><button style='color: #fff;padding:10px 27px;border:1px solid #fff;margin:25px 0px 0px'>詳細內容</button></nuxt-link></div>
          </div>
        </div>
        <div
          class="banner3"
          style="width: 25%; min-height: 286px; position: relative"
        >
          <div style="position: absolute; left: 50px;bottom:48px;width:193px">
            <div
              style="
                font-family: 'source-han-serif-tc';
                font-size: 25px;
                font-weight: 700;
                margin-bottom: 10px;
              "
            >
              客戶專區 標題
            </div>
            <div>中文簡介</div>
            <div><nuxt-link to="/technology"><button style='color: #000000;padding:10px 27px;border:1px solid #000000;margin:25px 0px 0px'>客戶登入</button></nuxt-link></div>
          </div>
        </div>
      </div>
    </div>
    <div style='padding:72px 0px' >
      <div style='font-size: 24px;font-family: "source-han-serif-tc";font-weight: 700;text-align: center;padding-bottom:48px'>新品消息</div>
      <div style="width:100%"  :class="`${windowWidth > 768 ? 'd-flex' : ''}`">
        <div class='section'>
          <div class='product-img pa-2' >
            <v-img
              :src="require('~/assets/img/product1515378669651533.jpg')"
            ></v-img>
          </div>
          <div class='product-text pa-2'>
            <div style='font-size:18px;font-weight: bold;margin-bottom: 13px;'>鑄鐵塗模劑</div>
            <div style='font-size: 15px;line-height: 25px;'>
              產品特點:醇基泛用型石墨塗模劑(FK)系列
            </div>
            <div style='font-size: 15px;line-height: 25px;'>產品規格:TN-168</div>
          </div>
        </div>
        <div class='section'>
          <div class='product-img pa-2' >
            <v-img
              :src="require('~/assets/img/product1515378669651533.jpg')"
            ></v-img>
          </div>
          <div class='product-text pa-2'>
            <div style='font-size:18px;font-weight: bold;margin-bottom: 13px;'>鑄鐵塗模劑</div>
            <div style='font-size: 15px;line-height: 25px;'>
              產品特點:醇基泛用型石墨塗模劑(FK)系列
            </div>
            <div style='font-size: 15px;line-height: 25px;'>產品規格:TN-168</div>
          </div>
        </div>
        <div class='section'>
          <div class='product-img pa-2' >
            <v-img
              :src="require('~/assets/img/product1515378669651533.jpg')"
            ></v-img>
          </div>
          <div class='product-text pa-2'>
            <div style='font-size:18px;font-weight: bold;margin-bottom: 13px;'>鑄鐵塗模劑</div>
            <div style='font-size: 15px;line-height: 25px;'>
              產品特點:醇基泛用型石墨塗模劑(FK)系列
            </div>
            <div style='font-size: 15px;line-height: 25px;'>產品規格:TN-168</div>
          </div>
        </div>
      </div>
      <div style='padding-bottom:100px'>
        <div class='dot' >
        <nuxt-link to="/news/newproduct" style='color: black;padding: 12px 16px;text-decoration: none;'>更多</nuxt-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import uiFunctions from "~/mixins/uiFunctions";
export default {
  mixins: [uiFunctions],
};
</script>
<style scoped>
.banner {
  background-image: url("../assets/img/home1514964981580654.jpg");
  background-size: cover;
}
.banner1 {
  background-image: url("../assets/img/home1515141616941534.jpg");
  background-size: cover;
}
.banner2 {
  background-image: url("../assets/img/home1515141711432725.jpg");
  background-size: cover;
}
.banner3 {
  background-image: url("../assets/img/home1515141732969725.jpg");
  background-size: cover;
}
.dot{
    background-image: url("../assets/img/ind-dot.png") ;
    background-position: center;
    background-size: 6px;
    text-align: center;
    padding-top: 118px;
}

@media screen and (min-width: 768px) and (max-width: 1000px) {
  .section{
    display: flex;
    width:33%;
    flex-direction: column;
  }
}

@media (min-width: 1001px) {
  .section{
    display: flex;
    width:33%;
  }
  .product-img{
    width:30%;
  }
  .product-text{
    width:70%;
  }
}

</style>
