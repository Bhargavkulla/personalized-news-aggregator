import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('news_articles.csv')

# Define categories and keywords
category_keywords = {
    'Politics': ['government', 'election', 'vote', 'politics', 'president', 'policy'],
    'Technology': ['technology', 'tech', 'AI', 'software', 'hardware', 'innovation'],
    'Sports': ['sports', 'football', 'basketball', 'game', 'player', 'team'],
    'Health': ['health', 'medicine', 'virus', 'disease', 'treatment'],
    'Business': ['business', 'market', 'economy', 'finance', 'startup'],
    'Entertainment': ['entertainment', 'movie', 'music', 'celebrity', 'show'],
}

# Function to categorize articles
def categorize_article(summary):
    summary = summary.lower()  # Convert to lowercase for matching
    for category, keywords in category_keywords.items():
        if any(keyword in summary for keyword in keywords):
            return category
    return 'Other'  # Default category if no keywords match

# Apply categorization to each article
df['Category'] = df['Summary'].apply(categorize_article)

# Save the updated DataFrame back to CSV
df.to_csv('news_articles.csv', index=False)

print("Categories added successfully!")
