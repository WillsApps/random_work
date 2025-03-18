function removeCssPropertyFromClass(className, property) {
    // Loop through all stylesheets
    for (let i = 0; i < document.styleSheets.length; i++) {
        let sheet = document.styleSheets[i];

        try {
            // Loop through all CSS rules in the stylesheet
            let rules = sheet.cssRules || sheet.rules;
            for (let j = 0; j < rules.length; j++) {
                let rule = rules[j];

                // Check if the rule applies to the specified class
                if (rule.selectorText === `.${className}`) {
                    rule.style.removeProperty(property);
                    return; // Exit after modifying the first matching rule
                }
            }
        } catch (e) {
            // Some stylesheets may be restricted due to CORS, so we ignore those
            console.warn("Could not access stylesheet:", sheet.href);
        }
    }
}


function setCssProperty(className, property, value,) {
    // Select all elements with the given class
    const elements = document.querySelectorAll(className);
    const element = document.getElementById(className);
    console.log(`className: ${className}
property: ${property}
value: ${value}
Elements: ${elements}
element: ${element}
Length: ${elements.length}`);
    if (element){
    element.style.setProperty(property, value);
    }
    elements.forEach(element => {
        // Remove the specific CSS property
        element.style.setProperty(property, value);
    });
}
function removeCssProperty(className, property) {
    // Select all elements with the given class
    const elements = document.querySelectorAll(className);
    console.log(`Elements: ${elements}`);

    elements.forEach(element => {
        // Remove the specific CSS property
        element.style.removeProperty(property);
    });
}


function fixTextArea(){
    setCssProperty("read-only-cursor-text-area", "font-size", "14px");
    setCssProperty("read-only-cursor-text-area", "font-family", "Comic Code");
    // setCssProperty("read-only-cursor-text-area", "padding-left", "64px");
}

const properties = [
"font-family",
'font-size'
];
properties.forEach(property => {
    removeCssPropertyFromClass("react-code-text", property);
    removeCssPropertyFromClass("react-blob-print-hide", property);
});
setCssProperty("body", "font-size", "14px");

setTimeout(fixTextArea, 3000);