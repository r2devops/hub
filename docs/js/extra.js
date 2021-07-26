const marginStruct = [0, 0];
var tab = false;

function loadListeners() {
    /*
     * This following screen is to expand md-content when we
     * select the .gitlab-ci.yml tab, and retract it to go
     * back to default state
     */

    let sidebar = document.getElementsByClassName('md-sidebar--secondary')[0];
    let content = document.getElementsByClassName('md-content')[0];
    let tabbed_1 = document.getElementById("__tabbed_1_1");
    let tabbed_2 = document.getElementById("__tabbed_1_2");

    function resizeFirst() {
        // Click on `.gitlab-ci.yml`
        marginStruct[0] = screen.width;

        // Handling different screen resolutions
        if (screen.width <= 768)
        {
            tab = true;
        }
        else {
            if (screen.width <= 1220)
                marginStruct[1] = 0;
            else marginStruct[1] = 1;

            sidebar.style.display = "none"
            content.style.maxWidth = `calc(100% - 12.1rem * ${marginStruct[1]})`
            tab = true;
        }
    }

    function resizeSecond() {
        // Click on `Documentation`
        marginStruct[0] = screen.width;

        // Handling different screen resolutions
        if (screen.width <= 768)
        {
            tab = false;
        }
        else {
            if (screen.width <= 1220)
                marginStruct[1] = 1;
            else marginStruct[1] = 2

            sidebar.style.display = "block"
            content.style.maxWidth = `calc(100% - 12.1rem * ${marginStruct[1]})`
            tab = false;
        }
    }

    function resizeListener() {
        // In case the user doesn't event click on .gitlab-ci.yml
        if (marginStruct[0] === 0)
            return;

        if (tab && screen.width <= 1220 && marginStruct[0] > 1220
            || screen.width <= 768 && marginStruct[0] > 768
            || tab && screen.width > 768 && marginStruct[0] <= 768) {
            sidebar.style.display = "none"
            marginStruct[1] = 0;
        }
        else if (!tab && screen.width <= 1220 && marginStruct[0] > 1220) {
            sidebar.style.display = "block"
            marginStruct[1] = 1;
        }
        else if (tab && screen.width > 1220 && marginStruct[0] <= 1220) {
            sidebar.style.display = "none"
            marginStruct[1] = 1;
        }
        else if (!tab && screen.width > 1220 && marginStruct[0] <= 1220) {
            sidebar.style.display = "block"
            marginStruct[1] = 2;
        }
        else if (!tab && screen.width > 768 && marginStruct[0] <= 768) {
            sidebar.style.display = "block"
            marginStruct[1] = 1;
        }

        marginStruct[0] = screen.width;
        content.style.maxWidth = `calc(100% - 12.1rem * ${marginStruct[1]})`
    }

    tabbed_1.onchange = resizeSecond;
    tabbed_2.onchange = resizeFirst;
    window.onresize = resizeListener;
}


<!-- HotJar -->
function hotjar(h,o,t,j,a,r){
    h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
    h._hjSettings={hjid:2507435,hjsv:6};
    a=o.getElementsByTagName('head')[0];
    r=o.createElement('script');r.async=1;
    r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
    a.appendChild(r);
}

/**
 * Explicit consent has been given
 */
const consent = function(state) {
    console.log("Cookie consent has been given");
    hotjar(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=')
}

function consentUpdate() {
    const item = localStorage.getItem("tibrrCookieConsent");
    if (item && new Date().getDate() < parseInt(item))
        hotjar(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=')
}

window.addEventListener('load', () => {
    const cookieButtons = document.getElementsByClassName("tibrr-cookie-consent-button");
    for (let item of cookieButtons) {
        item.addEventListener('click', () => consent(true), false);
    }
});

// We check whether the user has already something in the localStorage for it & so fetch needed plugins
consentUpdate();
<!-- End HotJar -->
