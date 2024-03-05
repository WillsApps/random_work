browser.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === "resizeFonts") {
    document.querySelectorAll("*").forEach(function (element) {
      // Check if the element or any of its classes has a font size specified
      const computedStyle = window.getComputedStyle(element);
      const fontSize = computedStyle.getPropertyValue("font-size");

      if (fontSize === "" || fontSize === "0px" || fontSize === "0em") {
        // Font size not specified or set to 0, update the font size to 0.9em
        element.style.fontSize = "0.9em";
      }
      // If you want to skip elements that already have a font size specified, remove the if statement and unconditionally set the font size:
      // element.style.fontSize = "0.9em";
    });
  }
});
