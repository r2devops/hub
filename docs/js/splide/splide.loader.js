function initSplide() {
    console.log("Loading splide");
	var secondarySlider = new Splide( '#secondary-slider', {
		fixedWidth  : 100,
		height      : 60,
		gap         : 10,
		cover       : true,
		isNavigation: true,
		focus       : 'center',
		breakpoints : {
			'600': {
				fixedWidth: 66,
				height    : 40,
			}
        },
        autoplay: true,
        interval: 5000,
        pauseOnHover: true,
        resetProgress: true,
        rewind: true,
        pagination: false
	} ).mount();
    var primarySlider = new Splide( '#primary-slider', {
		type       : 'fade',
		width: '100%',
		height: '400px',
		pagination : false,
		arrows     : false,
		cover      : true,
    } );
    primarySlider.sync( secondarySlider ).mount();
}