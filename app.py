# app.py
from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask World!'

@app.route('/scrape-data')
def scrape_data():
    # Example: Web scraping logic to get titles of top news articles from CNN
    url = 'https://www.cnn.com/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Adjust the selector based on the actual HTML structure of the website
        news_titles = [title.text.strip() for title in soup.select('.container__headline-text')]
        scraped_data = {"news_titles": news_titles}
        return jsonify(scraped_data)
    else:
        return jsonify({"error": "Failed to fetch data"})

if __name__ == '__main__':
    app.run(debug=True)
