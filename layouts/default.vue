<template>
  <v-app v-resize="Onresize" v-scroll="onScroll">
    <navDrawer></navDrawer>
    <infoNav></infoNav>
    <breadCrumbs></breadCrumbs>
    <nuxt></nuxt>
    <bottomFooter></bottomFooter>
    <copyright></copyright>
  </v-app>
</template>

<script>
import uiFunctions from "~/mixins/uiFunctions";
import navDrawer from "~/components/section/navDrawer";
import infoNav from "~/components/section/infoNav";
import bottomFooter from "~/components/section/bottomFooter";
import copyright from "~/components/section/copyright";
import breadCrumbs from "~/components/section/breadCrumbs";

export default {
  components: { navDrawer, infoNav, bottomFooter,copyright,breadCrumbs },
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
