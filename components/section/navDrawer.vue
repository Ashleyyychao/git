<template>
  <div
    class="container py-6"
    style="max-width: 1170px; padding: 60px 0px;height:130px"
    :style="`${windowWidth < 1025 ? 'border-bottom:5px solid #ffc005' : ''}`"
  >
    <div class="logo d-flex justify-space-between" style='padding:20px'>
      <div>
        <nuxt-link to="/"
          ><v-img
            width="356px"
            height="53px"
            :src="require('~/assets/img/logo.png')"
          ></v-img
        ></nuxt-link>
      </div>
      <div class="d-flex align-center" v-if="windowWidth > 1025">
        <div class="pr-6">
          <a href="" class="pa-2" style="font-weight: bold; color: #000000"
            >En</a
          >
          <span style='color:#c8c8c8;font-size:12px'>|</span>
          <a href="" class="pa-2" style="font-weight: bold; color: #000000"
            >繁中</a
          >
        </div>
        <button style="border: 1px solid #c8c8c8; padding: 10px 30px">
          客戶專區
        </button>
      </div>
      <div v-else>
        <button >
          <v-icon large>mdi-menu</v-icon>
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import uiFunctions from "~/mixins/uiFunctions";
import { mapGetters, mapMutations } from "vuex";
export default {
  mixins: [uiFunctions],
  methods:{
  //  dropdown() {
  //     this.$store.commit('menubartoggle');
  //   }
  }
};
</script>


<style scoped>
a {
  text-decoration: none;
  color: #000000;
  font-weight: bold;
  border-right: 8px;
}
</style>
