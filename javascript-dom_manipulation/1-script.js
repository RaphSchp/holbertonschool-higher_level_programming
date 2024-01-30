// Select the element with id "red_header"
let redHeaderElement = document.getElementById('red_header');

// Add an event listener for the click event
redHeaderElement.addEventListener('click', function() {
    // Select the header element and change its color to red (#FF0000)
    document.querySelector('header').style.color = '#FF0000';
});