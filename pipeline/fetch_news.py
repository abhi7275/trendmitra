import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
from topics import NEWS_KEYWORDS

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
NEWS_DIR = "data"

os.makedirs(NEWS_DIR, exist_ok=True)

all_articles = []

for keyword in NEWS_KEYWORDS:
    print(f"Fetching news for keyword: {keyword}")
    params = {
        "q": keyword,
        "language": "en",
        "pageSize": 20,
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }

    response = requests.get("https://newsapi.org/v2/everything", params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        print(f"Found {len(articles)} articles for keyword: {keyword}")
        all_articles.extend(articles)
    else:
        print(f"Failed to fetch articles for keyword: {keyword}. Status code: {response.status_code}")

# Save combined articles to one JSON file
date_str = datetime.now().strftime("%Y-%m-%d")
file_path = os.path.join(NEWS_DIR, f"news_{date_str}.json")

with open(file_path, "w") as f:
    json.dump(all_articles, f, indent=2)

print(f"Saved {len(all_articles)} articles to {file_path}")
if all_articles:
    print(f"First headline: {all_articles[0]['title']}")
