function initSplide() {
    console.log("Loading splide");
    new Splide( '.splide', {
        autoplay: true,
        interval: 5000,
        pauseOnHover: true,
        resetProgress: true,
        rewind: true,
        lazyLoad: 'nearby'
    } ).mount();
}