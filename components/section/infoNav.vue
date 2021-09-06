<template>
  <div class="container" style="max-width: 1170px">
    <nav role="navigation" class="d-flex" style='width:100%'>
      <div class="dropdown" style='width:20%'>
        <button class="dropbtn" style='width:100%'>關於我們</button>
        <div class="dropdown-content" style='width:100%'>
          <nuxt-link to="/about">公司簡介</nuxt-link>
          <nuxt-link to="/about/agent">代理品牌</nuxt-link>
          <nuxt-link to="/about/application">產品應用產業</nuxt-link>
        </div>
      </div>
      <div class="dropdown"  style='width:20%'>
        <button class="dropbtn" style='width:100%'>最新消息</button>
        <div class="dropdown-content">
        <nuxt-link to="/news">公司簡介</nuxt-link>
          <nuxt-link to="/news/newproduct">代理品牌</nuxt-link>
        </div>
      </div>
      <div class="dropdown"  style='width:20%'>
        <button class="dropbtn" style='width:100%'>產品介紹</button>
        <div class="dropdown-content">
          <a href="/product">塗膜劑</a>
        
        </div>
      </div>
      <div class="dropdown"  style='width:20%'>
        <button class="dropbtn" style='width:100%'>創新技術</button>
        <div class="dropdown-content">
         <nuxt-link to="/technology">公司簡介</nuxt-link>
          <nuxt-link to="/technology/customized">代理品牌</nuxt-link>
        </div>
      </div>
      <div class="dropdown"  style='width:20%'>
        <button class="dropbtn" style='width:100%'>聯絡我們</button>
        <div class="dropdown-content">
           <nuxt-link to="/contact">公司簡介</nuxt-link>
          <nuxt-link to="/contact/agent">代理品牌</nuxt-link>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
    };
  },
};
</script>

<style scoped>
.dropbtn {

  color: black;
  padding: 10px 15px 14px;
  font-size: 16px;
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
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #666;color:white}

.dropdown:hover .dropdown-content {display: block;}

.dropdown:hover .dropbtn {border-bottom:5px solid #ffc052}
</style>
