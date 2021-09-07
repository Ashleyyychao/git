<template>
  <div class="css"  :style="`${windowWidth < 900 ? 'padding: 63px 0px' : 'padding: 85px 0px;'}`">
    <div
      class="container d-flex"
      style="width: 100%;max-width: 1170px"
      :class="`${windowWidth < 900 ? 'flex-column px-7' : ''}`"
    >
      <div
        :class="`${windowWidth < 900 ? 'py-5' : 'pr-10'}`"
        style="font-size: 24px"
        :style="`${windowWidth < 900 ? '' : 'width:25%'}`"
      >
        有任何問題、建議請與我們連繫
      </div>
      <div
        :class="`${windowWidth < 900 ? 'py-5' : 'pr-10'}`"
        style="font-size: 15px"
        :style="`${windowWidth < 900 ? '' : 'width:25%'}`"
      >
        <div class="mb-1">台北辦公室</div>

        <div>新北市三重區河邊北街98號</div>
        <div>TEL | +886-2-29722438</div>
        <div>FAX | +886-2-29738384</div>
      </div>
      <div
        :class="`${windowWidth < 900 ? 'py-5' : 'pr-10'}`"
        style="font-size: 15px"
        :style="`${windowWidth < 900 ? '' : 'width:25%'}`"
      >
        <div class="mb-1">台中總部</div>

        <div>TEL | +886-4-2212-5555</div>
        <div>FAX | +886-4-22121735</div>
      </div>
      <div
        :class="`${windowWidth < 900 ? 'py-5' : 'pr-10'}`"
        style="font-size: 15px"
        :style="`${windowWidth < 900 ? '' : 'width:25%'}`"
      >
        <div class="mb-1">服務信箱</div>
        <div>chieh@jenyuh.com.tw</div>
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
.css {
 
  background-image: url("../../assets/img/footbg.jpg");
  color: white;
}
li {
  list-style: none;
}

@media (max-width: 900px) {
  .css {
  
  background-image: url("../../assets/img/footbgm.jpg");
  background-size: cover;
  color: white;
}
}
</style>