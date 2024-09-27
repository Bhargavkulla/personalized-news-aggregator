import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_bbc():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.find_all('article'):  # Adjust to the correct tag for articles
        title = item.find('h2').text if item.find('h2') else 'No Title'
        summary = item.find('p').text if item.find('p') else 'No Summary'
        pub_date = item.find('time')['datetime'] if item.find('time') else datetime.now().strftime('%Y-%m-%d')
        source = 'BBC'
        link = item.find('a')['href']
        
        # Ensure the link is complete
        if not link.startswith('http'):
            link = 'https://www.bbc.com' + link
        
        articles.append({
            'Title': title,
            'Summary': summary,
            'Publication Date': pub_date,
            'Source': source,
            'URL': link
        })
    
    return articles

def save_to_csv(articles):
    if articles:  # Check if there are any articles to save
        keys = articles[0].keys()
        with open('news_articles.csv', 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(articles)
        print(f"Saved {len(articles)} articles to news_articles.csv")
    else:
        print("No articles to save.")

# Main execution
if __name__ == "__main__":
    bbc_articles = scrape_bbc()
    save_to_csv(bbc_articles)

