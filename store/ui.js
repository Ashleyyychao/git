// state
export const state = () => ({
    isMobileW: true,
    isScrolledDown: false,
    isNavDrawer: false,
    windowWidth: 760
})

export const getters = {
    isMobileW: state => { return state.isMobileW },
    isScrolledDown: state => { return state.isScrolledDown },
    isNavDrawer: state => { return state.isNavDrawer },
    windowWidth: state => { return state.windowWidth },
}

export const mutations = {
    setisMobileW(state, value) {
        state.isMobileW = value;
    },
    setisScrolledDown(state, value) {
        state.isScrolledDown = value;
    },
    setIsNavDrawer(state, value) {
        state.isNavDrawer = value;
    },
    setWindowWidth(state, value) {
        state.windowWidth = value;
    },
}

