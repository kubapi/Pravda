console.log("Chrome extension go!");

let paragraphs = document.getElementsByTagName("div");
for (element of paragraphs) {
    element.style['background-color'] = "red";
}