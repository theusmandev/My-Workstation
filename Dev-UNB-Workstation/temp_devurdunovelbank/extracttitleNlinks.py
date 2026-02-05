import requests
import pandas as pd

API_KEY = "YOUR_YOUTUBE_API_KEY"
CHANNEL_ID = "YOUR_CHANNEL_ID"
BASE_URL = "https://www.googleapis.com/youtube/v3/search"

videos = []
next_page_token = None

while True:
    params = {
        "key": API_KEY,
        "channelId": CHANNEL_ID,
        "part": "snippet",
        "order": "date",
        "maxResults": 50,
        "pageToken": next_page_token
    }
    
    response = requests.get(BASE_URL, params=params).json()
    
    for item in response.get("items", []):
        video_title = item["snippet"]["title"]
        video_id = item["id"].get("videoId")
        if video_id:
            video_link = f"https://www.youtube.com/watch?v={video_id}"
            videos.append([video_title, video_link])
    
    next_page_token = response.get("nextPageToken")
    if not next_page_token:
        break

df = pd.DataFrame(videos, columns=["Title", "Link"])
df.to_excel("YouTube_Videos.xlsx", index=False)
print("Excel file saved successfully!")
