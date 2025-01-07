function myFunction() {
    const root = document.getElementById("root");
    for (const node in root.shadowRoot.querySelectorAll('code')) {
        if (node.style) {
            node.style.fontFamily = 'Comic Code';
        }
    }
}

setTimeout(myFunction, 3000);