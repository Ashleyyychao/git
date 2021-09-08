<template>
  <nav role="navigation">
    <div class="dropdown d-flex align-center" style="width: 100%; height: 85px">
      <nuxt-link to="/about"
        ><button
          class="dropbtn"
          style="width: 100%; color: #393939; font-size: 19px"
        >
          關於我們
        </button></nuxt-link
      >
    </div>
    <div
      class="dropdown-content d-flex align-center"
      style="width: 100%; height: 80px"
    >
      <nuxt-link to="/about">公司簡介</nuxt-link>
    </div>
    <div
      class="dropdown-content d-flex align-center"
      style="width: 100%; height: 80px"
    >
      <nuxt-link to="/about/agent">代理品牌</nuxt-link>
    </div>
    <div
      class="dropdown-content d-flex align-center"
      style="width: 100%; height: 80px"
    >
      <nuxt-link to="/about/application">產品應用產業</nuxt-link>
    </div>
    <div class="dropdown d-flex align-center" style="width: 100%; height: 85px">
      <nuxt-link to="/news"
        ><button
          class="dropbtn"
          style="width: 100%; color: #393939; font-size: 19px"
        >
          最新消息
        </button></nuxt-link
      >
    </div>
    <div
      class="dropdown-content d-flex align-center"
      style="width: 100%; height: 80px"
    >
      <nuxt-link to="/news">公司新訊</nuxt-link>
    </div>
    <div
      class="dropdown-content d-flex align-center"
      style="width: 100%; height: 80px"
    >
      <nuxt-link to="/news/newproduct">新品消息</nuxt-link>
    </div>
    <!-- <div v-for='(item,index) in news' :key='index'>
      <div
        class="dropdown-content d-flex align-center"
        style="width: 100%; height: 80px"
      >
        <nuxt-link to=item.href>{{item.title}}</nuxt-link>
      </div>
      <div
        class="dropdown-content d-flex align-center"
        style="width: 100%; height: 80px"
      >
        <nuxt-link to="/news/newproduct">{{item.title}}</nuxt-link>
      </div>
    </div> -->
    <div class="dropdown d-flex align-center" style="width: 100%; height: 85px">
      <nuxt-link to="/product">
        <button
          class="dropbtn"
          style="width: 100%; color: #393939; font-size: 19px"
        >
          產品介紹
        </button></nuxt-link
      >
    </div>
    <div
      class="dropdown-content d-flex align-center"
      style="width: 100%; height: 80px"
    >
      <nuxt-link to="/product">塗膜劑</nuxt-link>
    </div>
    <div class="dropdown d-flex align-center" style="width: 100%; height: 85px">
      <nuxt-link to="/technology"
        ><button
          class="dropbtn"
          style="width: 100%; color: #393939; font-size: 19px"
        >
          創新技術
        </button></nuxt-link
      >
    </div>
     <div
      class="dropdown-content d-flex align-center"
      style="width: 100%; height: 80px"
    >
      <nuxt-link to="/technology">品質控管</nuxt-link>
    </div>
     <div
      class="dropdown-content d-flex align-center"
      style="width: 100%; height: 80px"
    >
      <nuxt-link to="/technology/customized">技術服務</nuxt-link>
    </div>
    <div class="dropdown d-flex align-center" style="width: 100%; height: 85px">
      <nuxt-link to="/contact"
        ><button
          class="dropbtn"
          style="width: 100%; color: #393939; font-size: 19px"
        >
          聯絡我們
        </button></nuxt-link
      >
    </div>
     <div
      class="dropdown-content d-flex align-center"
      style="width: 100%; height: 80px"
    >
       <nuxt-link to="/contact">立即詢價</nuxt-link>
    </div>
      <div
      class="dropdown-content d-flex align-center"
      style="width: 100%; height: 80px"
    >
   <nuxt-link to="/contact/agent">營銷網絡</nuxt-link>
    </div>
    <div class="dropdown d-flex align-center" style="width: 100%; height: 85px">
      <div class="pr-6">
        <a
          href="/"
          class="pa-4"
          style="color: #393939; font-size: 19px; text-decoration: none"
          >En</a
        >
        <span style="color: #c8c8c8; font-size: 14px">|</span>
        <a
          href="/"
          class="pa-4"
          style="color: #393939; font-size: 19px; text-decoration: none"
          >繁中</a
        >
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      //     news: [
      //     { title: '公司新訊' ,href:'/news'},
      //     { title: '新品消息',href:"/news/newproduct" },
      //   ],
  
    };
  },
};
</script>

<style scoped>
.dropbtn {
  color: black;
  padding: 10px 15px 14px;
  font-size: 15px;
  text-align: left;
}

.dropdown {
  display: inline-block;
  border-bottom: 1px solid #eee;
}

.dropdown-content {
  background: #f3f3f3;
  border-bottom: 1px solid #eee;
  
}

.dropdown-content a {
  color: #666;
  padding: 12px 16px;
  text-decoration: none;
  display: inline-block;
  padding:5px
}
.dropdown-content a::before{
    content: "";
     height: 2px;
    width: 10px;
    background: #ffc005;
    display: inline-block;
    bottom:-50px;
    left: 15px;
    margin: 5px 12px ;

}
</style>
