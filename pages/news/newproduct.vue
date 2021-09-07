<template>
  <div class="container d-flex flex-row" style="max-width: 1170px">
    <div style="width: 30%" v-if='windowWidth>900'>
      <asideSection></asideSection>
    </div>
    <newsArrived></newsArrived>
   
  </div>
</template>
<script>
import asideSection from "~/components/section/asideSection";
import newsArrived from "~/components/section/newsArrived";
import uiFunctions from "~/mixins/uiFunctions";

export default {
  components: { asideSection,newsArrived },
    mixins: [uiFunctions],
};
</script>
