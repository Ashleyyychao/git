<template>
  <div
    style="
      border-top: 1px solid #eee;
      border-bottom: 1px solid #eee;
      padding: 24px 0;
      margin-top: -8px;
      background: #fcfcfc;
      margin: 0;
      padding: 0;
    "
  >
    <div
      class="container d-flex align-center"
      style="max-width: 1170px;font-size:13px;color: #777;font-family: 'Raleway','微軟正黑體', 'Microsoft JhengHei', sans-serif;"
      :style="`${windowWidth < 900 ? ';height:52px' : ';height:70px'}`"
    >
    首頁 :: 
    </div>
    

  </div>
</template>
<script>
import uiFunctions from "~/mixins/uiFunctions";

export default {
  mixins: [uiFunctions],
  
};
</script>
