let gigotte = false;
let gigotteInterval = null;
let gigotteEvent = null;

let stages, gigotteStages, time, slider, initiated;

function initSlider() {
    if (document.getElementById("juxtapose") == null)
        return;

    if (initiated) 
        clearInterval(gigotteInterval);
    
    initiated = true;

    stages = [
        [0, 1000], // Percent Time
        [ [100, 5000], 9000 ] // [EndPercent, time], Timee
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
    if (document.getElementById("juxtapose") == null)
        return;
        
    time = 0;
    stages.forEach((item) => {
        time += parseInt(item[1]);

        if (!Array.isArray(item[0]))
            setTimeout(() => slider.updateSlider(item[0], true), time);
        else {
            let slideData = item[0];

            for (let percent = 0; percent < slideData[0]; percent++) {
                setTimeout(() => slider.updateSlider(percent, true), time);
                time += parseInt(slideData[1]/100);
            }
        }
    });

    setTimeout(() => {
        time = 0;
        gigotteInterval = setInterval(() => {
            gigotteStages.forEach((item) => {
                time += parseInt(item[1]);
                setTimeout(() => slider.updateSlider(item[0], true), time);
            });
        }, 7000);
    }, 17000);
  

    gigotteEvent = document.getElementById("juxtapose").addEventListener("mousedown", (e) => {
        clearInterval(gigotteInterval);
    });
}

function removePercent(num) {
    return num.replace("%","");
}