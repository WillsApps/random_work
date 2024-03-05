let classesToChange = {
    "0.8em": [".char-info-res", ".tooltip-v2", ".item-selector", ".main-container"],
    "1.1em": [".tooltip-boundskill", ".tooltip-skill-name", ".tooltip-level"]
};
let sheets = document.styleSheets;
let divinationUpdated = false;


function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
function changeFontSizesAfterLoad() {
    for (var i = 0; i < document.styleSheets.length; i++) {
        if (sheets[i].href && !sheets[i].href.includes("grimtools")) {
            console.log("skipping", sheets[i]);
            continue;
        }
        let sheet = document.styleSheets[i];
        let cssRules = [];
        try {
            cssRules = sheet.cssRules;
            console.log("index: " + i + " processing", sheet);
        } catch (e) {
            console.log("index: " + i + " skipping", sheet);
        }
        console.log("cssRules.length", cssRules.length);
        for (var j = 0; j < cssRules.length; j++) {
            let cssRule = cssRules[j];
            if (cssRule.selectorText) {
                for (const [size, classNames] of Object.entries(classesToChange)) {
                    classNames.forEach(function (className) {
                        if (cssRule.selectorText === className) {
                            console.log("Found cssRule", cssRule);
                            cssRule.style.fontSize = size;
                        } else if (cssRule.selectorText.includes(className)) {
                            // console.log("Skipped cssRule", cssRule);
                        }
                    });
                }
            }
        }
    }
}

sleep(1000).then(() => {
    console.log("Slept 1s");
    changeFontSizesAfterLoad();
});

function changeFontAfterDivinationLoad(size) {
    divinationUpdated = true;
    document.querySelectorAll("*").forEach(function (element) {
        const classList = element.classList;
        if (!classList.contains("devotion-view-container")) {
            return;
        }
        console.log("element", element);

        // Font size not specified or set to 0, update the font size to 0.9em
        element.style.fontSize = size;
        // If you want to skip elements that already have a font size specified, remove the if statement and unconditionally set the font size:
        // element.style.fontSize = "0.9em";
    });
}

window.addEventListener("keydown",
  (event) => {
    if (event.code === "KeyD") {
        console.log("Keydown 'd'");
        sleep(1000).then(() => {
            console.log("Slept 1s");
            changeFontAfterDivinationLoad("0.8em");
        });
    }
});
//
//
// for (var i = 0; i < document.styleSheets[3].cssRules.length; i++) {
//     var style = document.styleSheets[3].cssRules[i];
//     if (style.selectorText) {
//         if (style.selectorText === ".main-container") {
//             console.log("style", style, "index", i);
//         }
//     }
// }
// var style = document.styleSheets[3].cssRules[89].style.fontSize = "0.8em";
// style.style.fontSize = "0.8em"
//
//
// for (const [size, classNames] of Object.entries(classesToChange)) {
//     classNames.forEach(function (className) {
//         document.querySelectorAll("." + className).forEach(function (element) {
//             console.log("element", element);
//             element.style.fontSize = size;
//         });
//     });
// }
//
// const elementsWithClassesToChange = ["devotion-view-container"];
// document.querySelectorAll("*").forEach(function (element) {
//     const classList = element.classList;
//     if (!classList.contains("devotion-view-container")) {
//         return;
//     }
//     console.log("element", element);
//
//     // Font size not specified or set to 0, update the font size to 0.9em
//     element.style.fontSize = "0.8em";
//     // If you want to skip elements that already have a font size specified, remove the if statement and unconditionally set the font size:
//     // element.style.fontSize = "0.9em";
// });
