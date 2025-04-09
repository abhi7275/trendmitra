import os
import json
from datetime import datetime
from dotenv import load_dotenv
import praw
from topics import REDDIT_KEYWORDS

# Load environment variables
load_dotenv()
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_SECRET")  # Match your .env key
user_agent = "reddit_api"

# Initialize Reddit client
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Collect posts
all_posts = []

for sub in REDDIT_KEYWORDS:
    print(f"Fetching top posts from r/{sub}...")
    try:
        subreddit = reddit.subreddit(sub)
        for post in subreddit.top(time_filter="day", limit=20):
            all_posts.append({
                "title": post.title,
                "url": post.url,
                "created_utc": post.created_utc,
                "subreddit": post.subreddit.display_name,
                "score": post.score,
                "num_comments": post.num_comments
            })
    except Exception as e:
        print(f"Failed to fetch from r/{sub}: {e}")

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Save posts to JSON
date_str = datetime.now().strftime("%Y-%m-%d")
file_path = os.path.join("data", f"reddit_{date_str}.json")

with open(file_path, "w") as f:
    json.dump(all_posts, f, indent=2)

print(f"\n Saved {len(all_posts)} posts to {file_path}")
if all_posts:
    print(f" First headline: {all_posts[0]['title']}")
else:
    print(" No posts found.")
