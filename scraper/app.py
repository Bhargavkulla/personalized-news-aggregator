from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route for the root URL
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the News Aggregator API!"})

# Route to fetch articles
@app.route('/articles')
def articles():
    articles_data = [
        {
            "category": "Health",
            "published_at": "2024-09-27",
            "source": "BBC",
            "summary": "More than 600 people have been killed by Israeli airstrikes in Lebanon since Monday, health officials say.",
            "title": "Israel striking Hezbollah with ‘full force’ despite ceasefire calls"
        }
    ]
    return jsonify(articles_data)

if __name__ == '__main__':
    app.run(debug=True)
