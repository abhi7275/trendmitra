from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
