<template></template>

<script>
import { mapGetters, mapMutations } from "vuex";
export default {
  computed: {
    ...mapGetters({
      IsMobileW: "ui/isMobileW",
      IsScrolledDown: "ui/isScrolledDown",
      IsNavDrawer: "ui/isNavDrawer",
      WindowWidth: "ui/windowWidth",
    }),
    isMobileW: {
      get() {
        return this.IsMobileW;
      },
      set(value) {
        this.setisMobileW(value);
      },
    },
    isScrolledDown: {
      get() {
        return this.IsScrolledDown;
      },
      set(val) {
        this.setisScrolledDown(val);
      },
    },
    isNavDrawer: {
      get() {
        return this.IsNavDrawer;
      },
      set(value) {
        this.setIsNavDrawer(value);
      },
    },
    windowWidth: {
      get() {
        return this.WindowWidth;
      },
      set(value) {
        this.setWindowWidth(value);
      },
    },
  },
  methods: {
    ...mapMutations({
      setisMobileW: "ui/setisMobileW",
      setisScrolledDown: "ui/setisScrolledDown",
      setIsNavDrawer: "ui/setIsNavDrawer",
      setWindowWidth: "ui/setWindowWidth",
    }),
    onScroll(e) {
      let ScrollTop = window.pageYOffset || document.documentElement.scrollTop;
      if (this.isScrolledDown == true && ScrollTop == 0) {
        this.isScrolledDown = false;
        return;
      }
      if (ScrollTop > 48) {
        this.isScrolledDown = true;
        return;
      } else {
        this.isScrolledDown = false;
        return;
      }
    },
  },
  watch: {
    isMobileW() {
      if (this.isMobileW == false) {
        this.isNavDrawer = false;
      }
    },
  },
};
</script>

<style>
</style>