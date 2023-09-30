'use strict';



/**
 * PRELOAD
 * 
 * loading will be end after document is loaded
 */

const preloader = document.querySelector("[data-preaload]");

window.addEventListener("load", function () {
    preloader.classList.add("loaded");
    document.body.classList.add("loaded");
});



/**
 * add event listener on multiple elements
 */

const addEventOnElements = function (elements, eventType, callback) {
    for (let i = 0, len = elements.length; i < len; i++) {
        elements[i].addEventListener(eventType, callback);
    }
}



/**
 * NAVBAR
 */

const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function () {
    navbar.classList.toggle("active");
    overlay.classList.toggle("active");
    document.body.classList.toggle("nav-active");
}

addEventOnElements(navTogglers, "click", toggleNavbar);

// Function to toggle scroll buttons based on screen size
function toggleScrollButtons() {
    const scrollContainer = document.querySelector(".scroll-container");
    const scrollButtons = document.querySelector(".scroll-buttons");

    if (scrollContainer.scrollWidth > scrollContainer.clientWidth) {
        scrollButtons.style.display = "block";
    } else {
        scrollButtons.style.display = "none";
    }
    const nextButton = document.querySelector(".next-button");

    nextButton.addEventListener("click", () => {
        scrollContainer.scrollLeft += 300; //The distance to be moved?
    });
}
// const nextButton = document.querySelector(".next-button");

// nextButton.addEventListener("click", () => {
//     scrollContainer.scrollLeft += 300; //The distance to be moved?
// });


window.addEventListener("resize", toggleScrollButtons);

//toggle checking
toggleScrollButtons();
// const starInputs = document.querySelectorAll('.star-rating input[type="radio"]');

// starInputs.forEach((input) => {
//     input.addEventListener('change', (event) => {
//         const selectedRating = event.target.value;
//         console.log('Selected rating:', selectedRating);
        
//     });
// });
