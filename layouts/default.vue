<template>
  <v-app v-resize="Onresize" v-scroll="onScroll">
    <navDrawer></navDrawer>
    <infoNav></infoNav>
    <nuxt></nuxt>
    <bottomFooter></bottomFooter>
    <copyright></copyright>
  </v-app>
</template>

<script>
import uiFunctions from "~/mixins/uiFunctions";
import navDrawer from "~/components/layout/navDrawer";
import infoNav from "~/components/layout/infoNav";
import bottomFooter from "~/components/layout/bottomFooter";
import copyright from "~/components/layout/copyright";

export default {
  components: { navDrawer, infoNav, bottomFooter,copyright },
  mixins: [uiFunctions],
  mounted() {
    this.checkWindowsW();
  },
  methods: {
    Onresize() {
      this.checkWindowsW();
    },
    checkWindowsW() {
      this.windowWidth = window.innerWidth;
      if (window.innerWidth < 769) {
        this.isMobileW = true;
      } else {
        this.isMobileW = false;
      }
    },
  },
};
</script>
