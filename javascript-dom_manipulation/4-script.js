// Step 1: Get the element with id "add_item"
let addItemElement = document.getElementById('add_item');

// Step 2: Add an event listener for the click event on this element
addItemElement.addEventListener('click', function() {

    // Step 3: Create a new list item
    let newListItem = document.createElement('li');
    newListItem.textContent = 'Item';

    // Step 4: Get the list with class "my_list"
    let myList = document.querySelector('.my_list');

    // Step 5: Append the new list item to this list
    myList.appendChild(newListItem);
});
