import os 
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
from topics import YOUTUBE_KEYWORDS

# Load environment variables
load_dotenv()
YouTube_API_KEY = os.getenv("YOUTUBE_API_KEY")

#Create output directory
os.makedirs("data", exist_ok=True)

#Set up API parameters
all_videos = []

#Loop through each keyword and fetch data using YouTube API
for topic in YOUTUBE_KEYWORDS:
    print(f"Fetching YouTube videos for topic: {topic}")

    params = {
        "part": "snippet",
        "q": topic,
        "type": "video",
        "maxResults": 20,
        "order": "date",
        "key": YouTube_API_KEY
    }
    response =requests.get("https://www.googleapis.com/youtube/v3/search", params=params)   

    #Extract video details
    if response.status_code == 200:
        data = response.json()
        videos = data.get("items", [])
        print(f"Found {len(videos)} videos for topic: {topic}")
        for video in videos:
            video_data = {
                "title": video["snippet"]["title"],
                "description": video["snippet"]["description"],
                "publishedAt": video["snippet"]["publishedAt"],
                "channelTitle": video["snippet"]["channelTitle"],
                "videoId": video["id"]["videoId"]
            }
            all_videos.append(video_data)
    else:
        print(f"Failed to fetch videos for topic: {topic}. Status code: {response.status_code}")

#Save combined videos details to one JSON file

date_str = datetime.now().strftime("%Y-%m-%d")
file_path = os.path.join("data", f"youtube_{date_str}.json")
with open(file_path, "w") as f:
    json.dump(all_videos, f, indent=2)
print(f"Saved {len(all_videos)} videos to {file_path}")
if all_videos:
    print(f"First video title: {all_videos[0]['title']}")
