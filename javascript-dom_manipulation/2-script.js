// Select the element with id "red_header"
let redHeaderElement = document.getElementById('red_header');

// Add an event listener for the click event
redHeaderElement.addEventListener('click', function() {
    // Select the header element and add the class "red"
    document.querySelector('header').classList.add('red');
});
