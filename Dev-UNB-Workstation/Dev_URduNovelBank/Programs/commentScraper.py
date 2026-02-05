from googleapiclient.discovery import build
import pandas as pd
from googleapiclient.errors import HttpError

# Define your API key and playlist ID here
api_key = 'AIzaSyA0VXy54BnQNbvWsqt9BuWuSEhSRg1QBeY'
playlist_ids = ['PL34VcAFITZsiN-kZao404k1uR6jvo4wnu']  # Replace with your actual playlist ID

# Build the YouTube client
youtube = build('youtube', 'v3', developerKey=api_key)

# Function to get all video IDs from a playlist
def get_all_video_ids_from_playlists(youtube, playlist_ids):
    all_videos = []
    for playlist_id in playlist_ids:
        next_page_token = None
        while True:
            playlist_request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            playlist_response = playlist_request.execute()
            all_videos.extend([item['contentDetails']['videoId'] for item in playlist_response['items']])
            next_page_token = playlist_response.get('nextPageToken')
            if not next_page_token:
                break
    return all_videos

# Get all video IDs from the playlist
video_ids = get_all_video_ids_from_playlists(youtube, playlist_ids)

# Function to get replies for a specific comment
def get_replies(youtube, parent_id, video_id):
    replies = []
    next_page_token = None
    while True:
        try:
            reply_request = youtube.comments().list(
                part="snippet",
                parentId=parent_id,
                textFormat="plainText",
                maxResults=100,
                pageToken=next_page_token
            )
            reply_response = reply_request.execute()
            for item in reply_response['items']:
                comment = item['snippet']
                replies.append({
                    'Timestamp': comment['publishedAt'],
                    'Username': comment['authorDisplayName'],
                    'VideoID': video_id,
                    'Comment': comment['textDisplay'],
                    'Date': comment.get('updatedAt', comment['publishedAt'])
                })
            next_page_token = reply_response.get('nextPageToken')
            if not next_page_token:
                break
        except HttpError as e:
            print(f"An error occurred while fetching replies: {e}")
            break
    return replies

# Function to get all comments (including replies) for a single video
def get_comments_for_video(youtube, video_id):
    all_comments = []
    next_page_token = None
    while True:
        try:
            comment_request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=next_page_token,
                textFormat="plainText",
                maxResults=100
            )
            comment_response = comment_request.execute()
            for item in comment_response['items']:
                top_comment = item['snippet']['topLevelComment']['snippet']
                all_comments.append({
                    'Timestamp': top_comment['publishedAt'],
                    'Username': top_comment['authorDisplayName'],
                    'VideoID': video_id,
                    'Comment': top_comment['textDisplay'],
                    'Date': top_comment.get('updatedAt', top_comment['publishedAt'])
                })
                # Fetch replies if there are any
                if item['snippet']['totalReplyCount'] > 0:
                    all_comments.extend(get_replies(youtube, item['snippet']['topLevelComment']['id'], video_id))
            next_page_token = comment_response.get('nextPageToken')
            if not next_page_token:
                break
        except HttpError as e:
            print(f"An error occurred with video ID {video_id}: {e}")
            break
    return all_comments

# Fetch comments from all videos in the playlist
all_comments = []
for video_id in video_ids:
    video_comments = get_comments_for_video(youtube, video_id)
    all_comments.extend(video_comments)
    print(f"Fetched {len(video_comments)} comments for video ID {video_id}. Total comments so far: {len(all_comments)}")

# Convert the comments to a DataFrame
comments_df = pd.DataFrame(all_comments)

# Save the DataFrame to a CSV file
csv_file = 'comments_data.csv'
comments_df.to_csv(csv_file, index=False)

print(f"Comments and replies have been saved to {csv_file}")
print(f"Total comments and replies saved: {len(all_comments)}")
