<template>
  <v-app v-resize="Onresize" v-scroll="onScroll">
    <navDrawer></navDrawer>
    <infoNav v-if="windowWidth > 1025"></infoNav>
    <!-- <mobileNav v-if="$store.state.menubar"></mobileNav> -->
    <mobileNav v-if='Mnav'></mobileNav>
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
import mobileNav from "~/components/section/mobileNav";

export default {
  components: {
    navDrawer,
    infoNav,
    bottomFooter,
    copyright,
    breadCrumbs,
    mobileNav,
  },
  mixins: [uiFunctions],
  data() {
    return {
      Mnav:false
    };
  },
  computed: {
    // menubar () {
    //   return $store.state.menubar
    //   }
  },
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
