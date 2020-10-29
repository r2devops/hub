let gigotte = false;
let gigotteInterval = null;
let gigotteEvent = null;

let stages, gigotteStages, time, slider, initiated;

function initSlider() {
    if (initiated) 
        clearInterval(gigotteInterval);
    
    initiated = true;

    stages = [
        [30, 750],
        [70, 1000],
        [50, 1250]
    ];

    gigotteStages = [
        [47, 200],
        [53, 200],
        [50, 200]
    ];

    slider = new juxtapose.JXSlider('#juxtapose',
        [
            {
                src: 'images/with_hub.png'
            },
            {
                src: 'images/without_hub.png'
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

    setTimeout(() => setSliderAnims(), 500);
}

function setSliderAnims() {
    time = 0;
    stages.forEach((item) => {
        time += parseInt(item[1]);
        setTimeout(() => slider.updateSlider(item[0], true), time);
    });
  
    time = 0;
    gigotteInterval = setInterval(() => {
        gigotteStages.forEach((item) => {
            time += parseInt(item[1]);
            setTimeout(() => slider.updateSlider(item[0], true), time);
        });
    }, 7000);

    gigotteEvent = document.getElementById("juxtapose").addEventListener("mousedown", (e) => {
        clearInterval(gigotteInterval);
    });
}
