<template>
  <div class="container" style="max-width: 1170px; padding: 0px; height: 47px">
    <nav
      role="navigation"
      class="d-flex"
      style="max-width: 1170px; width: 100%; height: 100%"
    >
      <div class="dropdown" style="width: 20%">
        <nuxt-link to="/about"
          ><button class="dropbtn" style="width: 100%">
            關於我們
          </button></nuxt-link
        >
        <div class="dropdown-content" style="width: 100%">
          <nuxt-link to="/about">公司簡介</nuxt-link>
          <nuxt-link to="/about/agent">代理品牌</nuxt-link>
          <nuxt-link to="/about/application">產品應用產業</nuxt-link>
        </div>
      </div>
      <div class="dropdown" style="width: 20%">
        <nuxt-link to="/news"
          ><button class="dropbtn" style="width: 100%">
            最新消息
          </button></nuxt-link
        >
        <div class="dropdown-content" style="width: 100%">
          <nuxt-link to="/news">公司新訊</nuxt-link>
          <nuxt-link to="/news/newproduct">新品消息</nuxt-link>
        </div>
      </div>
      <div class="dropdown" style="width: 20%">
        <nuxt-link to="/news">
          <button class="dropbtn" style="width: 100%">
            產品介紹
          </button></nuxt-link
        >
        <div class="dropdown-content" style="width: 100%">
          <a href="/product">塗膜劑</a>
        </div>
      </div>
      <div class="dropdown" style="width: 20%">
        <nuxt-link to="/news"
          ><button class="dropbtn" style="width: 100%">
            創新技術
          </button></nuxt-link
        >
        <div class="dropdown-content" style="width: 100%">
          <nuxt-link to="/technology">品質控管</nuxt-link>
          <nuxt-link to="/technology/customized">技術服務</nuxt-link>
        </div>
      </div>
      <div class="dropdown" style="width: 20%">
        <nuxt-link to="/news"
          ><button class="dropbtn" style="width: 100%">
            聯絡我們
          </button></nuxt-link
        >
        <div class="dropdown-content" style="width: 100%">
          <nuxt-link to="/contact">立即詢價</nuxt-link>
          <nuxt-link to="/contact/agent">營銷網絡</nuxt-link>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style scoped>
.dropbtn {
  color: black;
  padding: 10px 15px 14px;
  font-size: 15px;
  border-bottom: 1px solid #eee;
  border-right: 1px solid #eee;
  border-left: 1px solid #eee;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  background: white;
  display: none;
  position: absolute;
  min-width: 175px;
  z-index: 1;
  text-align: center;
}

.dropdown-content a {
  color: #666;
  border-bottom: 1px solid #eee;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background-color: #666;
  color: white;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropbtn {
  border-bottom: 5px solid #ffc052;
}
</style>
