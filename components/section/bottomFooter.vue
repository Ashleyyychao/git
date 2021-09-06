<template>
  <div class="css">
    <div class="container d-flex" style='width:100%;max-width:1170px' :class="`${windowWidth < 900 ? 'flex-column' : ''}`">
      <div class="pa-7" style='font-size:24px' :class="`${windowWidth < 900 ? '' : 'width:25%'}`">有任何問題、建議請與我們連繫</div>
      <div class="pa-7" :class="`${windowWidth < 900 ? '' : 'width:25%'}`">
        <div>台北辦公室</div>

        <div>新北市三重區河邊北街98號</div>
        <div>TEL | +886-2-29722438</div>
        <div>FAX | +886-2-29738384</div>
      </div>
      <div class="pa-7" :class="`${windowWidth < 900 ? '' : 'width:25%'}`">
        <div>台中總部</div>

        <div>TEL | +886-4-2212-5555</div>
        <div>FAX | +886-4-22121735</div>
      </div>
      <div class="pa-7" :class="`${windowWidth < 900 ? '' : 'width:25%'}`">
        <div>服務信箱</div>
        <div>chieh@jenyuh.com.tw</div>
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
.css {
  background-color: black;
  color: white;
}
li {
  list-style: none;
}
</style>