slider = new juxtapose.JXSlider('#juxtapose',
    [
        {
            src: 'images/with_hub.svg'
        },
        {
            src: 'images/without_hub.svg'
        }
    ],
    {
        animate: true,
        showLabels: true,
        showCredits: true,
        startingPosition: "50%",
        makeResponsive: true
    }
);


window.addEventListener('load', function () {
    let stages = [
        [30, 750],
        [70, 1000],
        [50, 1250]
    ];

    let time = 0;
    stages.forEach((item, index) => {
        time += parseInt(item[1]);
        setTimeout(() => slider.updateSlider(item[0], true), time);
    });
  
})
