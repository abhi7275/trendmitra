from trendmitra.config import NEWS_API_KEY, REDDIT_CLIENT_ID, REDDIT_SECRET, YOUTUBE_API_KEY
import requests
import praw

def test_news_api():
    print("\n📰 Testing NewsAPI...")
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        print("✅ NewsAPI key is valid.")
    else:
        print(f"❌ NewsAPI failed with status: {response.status_code} - {response.text}")

def test_reddit_api():
    print("\n👽 Testing Reddit API...")
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_SECRET,
            user_agent="trendmitra-test-script"
        )
        subreddit = reddit.subreddit("india")
        for post in subreddit.hot(limit=1):
            print("✅ Reddit API key is valid.")
            return
        print("❌ Reddit fetch failed.")
    except Exception as e:
        print(f"❌ Reddit API failed: {e}")

def test_youtube_api():
    print("\n📺 Testing YouTube API...")
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=IN&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        print("✅ YouTube API key is valid.")
    else:
        print(f"❌ YouTube API failed with status: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_news_api()
    test_reddit_api()
    test_youtube_api()
