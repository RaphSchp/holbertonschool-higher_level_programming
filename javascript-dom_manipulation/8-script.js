// Listen for the "DOMContentLoaded" event to ensure the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Use the Fetch API to get data from the provided URL
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => {
        // Convert the response to JSON
        return response.json();
      })
      .then(data => {
        // Get the element with id "hello"
        let helloElement = document.getElementById('hello');
        
        // Set the content of the div to the "hello" value from fetched data
        helloElement.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });
  