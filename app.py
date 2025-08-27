from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv 

load_dotenv()
app = Flask(__name__)

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_API_URL = 'https://newsapi.org/v2/everything'

@app.route('/')
def home():
    """Fetches news articles and renders them on the homepage."""
    params = {
        'q': 'artificial intelligence OR machine learning', 
        'sortBy': 'publishedAt', 
        'language': 'en',        
        'pageSize': 31,          
        'apiKey': NEWS_API_KEY
    }
    
    articles = []
    error_message = None

    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()  
        data = response.json()
        
        if data.get('status') == 'ok':
            
            articles = [
                article for article in data.get('articles', [])
                if article.get('urlToImage')
            ]
        else:
            error_message = data.get('message', 'Could not fetch news.')

    except requests.exceptions.RequestException as e:
        error_message = "Network error: Could not connect to the news service."
        print(f"Error: {e}")

    return render_template('index.html', articles=articles, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)