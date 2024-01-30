// Step 1: Use the Fetch API to get data from the provided URL
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    // Step 2: Convert the response to JSON
    return response.json();
  })
  .then(data => {
    // Step 3: Get the element with id "character"
    let characterElement = document.getElementById('character');
    
    // Step 4: Update the text content of the "character" div with the fetched name
    characterElement.textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
