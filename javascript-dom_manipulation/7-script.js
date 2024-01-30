// Step 1: Use the Fetch API to get data from the provided URL
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    // Step 2: Convert the response to JSON
    return response.json();
  })
  .then(data => {
    // Step 3: Get the element with id "list_movies"
    let moviesListElement = document.getElementById('list_movies');
    
    // Step 4: Loop through the movies in the fetched data and append them to the ul
    data.results.forEach(movie => {
      let listItem = document.createElement('li');  // Create a new 'li' element
      listItem.textContent = movie.title;           // Set the content of 'li' to the movie title
      moviesListElement.appendChild(listItem);      // Append the 'li' to the ul
    });
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
