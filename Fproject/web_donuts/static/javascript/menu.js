const nav = document.querySelector(".nav"),
    searchIcon = document.querySelector("#searchIcon"),
    navOpenBtn = document.querySelector(".navOpenBtn"),
    navCloseBtn = document.querySelector(".navCloseBtn"),
    cartIcon = document.querySelector("#cart"); // Select the cart icon element
    profileIcon = document.querySelector("#profile")

navOpenBtn.addEventListener("click", () => {
    nav.classList.add("openNav");
    nav.classList.remove("openSearch");
    searchIcon.classList.replace("uil-times", "uil-search");
    cartIcon.classList.remove("hidden-cart"); // Ensuring that the cart icon is visible 
    profileIcon.classList.remove("hidden-profile");
});

navCloseBtn.addEventListener("click", () => {
    nav.classList.remove("openNav");
});


// concerning search box
// const searchBox = document.querySelector('#search-bar');
// searchBox.addEventListener("input",function(){
//     console.log("Input value: ",searchBox.value.toLowerCase());
// })

const searchBox = document.querySelector('#search-bar');
const donuts = document.querySelectorAll('.donut');
const categories = document.querySelectorAll('.category');

searchIcon.addEventListener("click", () => {
    nav.classList.toggle("openSearch");
    // nav.classList.remove("openNav");
    if (nav.classList.contains("openSearch")) {
        searchIcon.classList.replace("uil-search", "uil-times");
        // hiding the cart and profile
        cartIcon.classList.add("hidden-cart");
        profileIcon.classList.add("hidden-profile");
    } else {
        // shapshifter search icon
        searchIcon.classList.replace("uil-times", "uil-search");
        // showing the cart again!
        cartIcon.classList.remove("hidden-cart"); 
        profileIcon.classList.remove("hidden-profile"); 
        if (!nav.classList.contains("openSearch")) {
            // Clearing the search box input and displaying all categories and donuts
            document.querySelector('#search-bar').value = "";
            // donuts.forEach(donut => {
            //     donut.style.display = 'block';
            // });
            // categories.forEach(category => {
            //     category.style.display = 'block';
            // });
            donuts.forEach(donut => {
                donut.classList.remove("hide");
            });

            // Remove the hide class to display all categories
            categories.forEach(category => {
                category.classList.remove("hide");
            });
        }
    }
});

searchBox.addEventListener("input", function () {
    const searchTerm = searchBox.value.toLowerCase().trim();

    // Add the hide class to hide all donuts and categories
    donuts.forEach(donut => {
        donut.classList.add("hide");
    });
    categories.forEach(category => {
        category.classList.add("hide");
    });

    // Filtering and displaying donuts and categories based on the search term inputted
    donuts.forEach(donut => {
        const donutName = donut.querySelector('.donut-name').textContent.toLowerCase();
        const donutCategory = donut.closest('.category');
        const categoryTitle = donutCategory.querySelector('h2').textContent.toLowerCase();

        if (donutName.includes(searchTerm) || categoryTitle.includes(searchTerm) ) {
            donut.classList.remove("hide");
            donutCategory.classList.remove("hide");
        }
    });

    // Show all categories if the search box is empty and hopefully it is 
    if (searchTerm === "") {
        categories.forEach(category => {
            category.classList.remove("hide");
        });
    }
});

function addToCart(donutId, quantity) {
    console.log('Adding donut to cart with ID:', donutId, 'Quantity:', quantity);
// ajax request
    $.ajax({
        url: '/add_to_cart/' + donutId + '/?quantity=' + quantity,
        method: 'GET',
        // callback function
        success: function (data) {
            // Update the cart count in the menu
            $('#cart-count').text(data.cart_count);
        },
        error: function (error) {
            console.log('Error:', error);
        }
    });
}