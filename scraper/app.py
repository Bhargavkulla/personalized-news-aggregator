from flask import Flask, jsonify, request  # Import request here
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample articles data
articles_data = [
    {
        "category": "Health",
        "id": 1,
        "published_at": "2024-09-27",
        "source": "BBC",
        "summary": "More than 600 people have been killed by Israeli airstrikes in Lebanon since Monday, health officials say.",
        "title": "Israel striking Hezbollah with ‘full force’ despite ceasefire calls",
        "url": "http://example.com/article1"
    },
    {
        "category": "Technology",
        "id": 2,
        "published_at": "2024-09-26",
        "source": "CNN",
        "summary": "Tech companies are making strides in AI and automation.",
        "title": "The Rise of AI: What to Expect in the Coming Years",
        "url": "http://example.com/article2"
    }
]

# Route for the root URL
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the News Aggregator API!"})

# Route to fetch all articles
@app.route('/api/articles', methods=['GET'])
def articles():
    return jsonify(articles_data)

# Route to fetch a specific article by ID
@app.route('/api/articles/<int:id>', methods=['GET'])
def get_article(id):
    article = next((article for article in articles_data if article['id'] == id), None)
    if article:
        return jsonify(article)
    else:
        return jsonify({"error": "Article not found"}), 404

# Route to search articles by keyword
@app.route('/api/search', methods=['GET'])
def search_articles():
    query = request.args.get('q', '')
    filtered_articles = [article for article in articles_data if query.lower() in article['title'].lower()]
    return jsonify(filtered_articles)

if __name__ == '__main__':
    app.run(debug=True)
