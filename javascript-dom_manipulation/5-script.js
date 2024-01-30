// Step 1: Get the element with id "update_header"
let updateHeaderElement = document.getElementById('update_header');

// Step 2: Add an event listener for the click event on this element
updateHeaderElement.addEventListener('click', function() {

    // Step 3: Get the header element
    let headerElement = document.querySelector('header');

    // Step 4: Update the text content of the header element
    headerElement.textContent = 'New Header!!!';
});
