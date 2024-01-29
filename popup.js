// popup.js
document.addEventListener('DOMContentLoaded', function() {
  fetch('http://localhost:5000/scrape-data')  // Adjust the URL based on your server setup
    .then(response => response.json())
    .then(data => {
      const dataContainer = document.getElementById('data-container');
      
      if (data.error) {
        dataContainer.textContent = `Error: ${data.error}`;
      } else if (data.news_titles && data.news_titles.length > 0) {
        const ul = document.createElement('ul');
        data.news_titles.forEach(title => {
          const li = document.createElement('li');
          li.textContent = title;
          ul.appendChild(li);
        });
        dataContainer.appendChild(ul);
      } else {
        dataContainer.textContent = 'No data available.';
      }
    })
    .catch(error => console.error('Error fetching data:', error));
});
