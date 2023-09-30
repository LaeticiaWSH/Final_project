// const nav = document.querySelector(".nav"),
//     searchIcon = document.querySelector("#searchIcon"),
//     navOpenBtn = document.querySelector(".navOpenBtn"),
//     navCloseBtn = document.querySelector(".navCloseBtn");

// searchIcon.addEventListener("click", () => {
//     nav.classList.toggle("openSearch");
//     nav.classList.remove("openNav");
//     if (nav.classList.contains("openSearch")) {
//         return searchIcon.classList.replace("uil-search", "uil-times");
//     }
//     searchIcon.classList.replace("uil-times", "uil-search");
// });

// navOpenBtn.addEventListener("click", () => {
//     nav.classList.add("openNav");
//     nav.classList.remove("openSearch");
//     searchIcon.classList.replace("uil-times", "uil-search");
// });
// navCloseBtn.addEventListener("click", () => {
//     nav.classList.remove("openNav");
// });

const nav = document.querySelector(".nav"),
    searchIcon = document.querySelector("#searchIcon"),
    navOpenBtn = document.querySelector(".navOpenBtn"),
    navCloseBtn = document.querySelector(".navCloseBtn"),
    cartIcon = document.querySelector("#cart"); // Select the cart icon element

searchIcon.addEventListener("click", () => {
    nav.classList.toggle("openSearch");
    nav.classList.remove("openNav");
    if (nav.classList.contains("openSearch")) {
        searchIcon.classList.replace("uil-search", "uil-times");
        cartIcon.classList.add("hidden-cart"); // Add a class to hide the cart icon
    } else {
        searchIcon.classList.replace("uil-times", "uil-search");
        cartIcon.classList.remove("hidden-cart"); // Remove the class to show the cart icon
    }
});

navOpenBtn.addEventListener("click", () => {
    nav.classList.add("openNav");
    nav.classList.remove("openSearch");
    searchIcon.classList.replace("uil-times", "uil-search");
    cartIcon.classList.remove("hidden-cart"); // Ensure the cart icon is visible when opening the nav
});

navCloseBtn.addEventListener("click", () => {
    nav.classList.remove("openNav");
});


// concerning search box
const searchBox = document.querySelector('#search-bar');
searchBox.addEventListener("input",function(){
    console.log("Input value: ",searchBox.value.toLowerCase());
})