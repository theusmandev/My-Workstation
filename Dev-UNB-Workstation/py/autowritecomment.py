# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# import time

# # Step 1: Authentication
# SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# def authenticate():
#     flow = InstalledAppFlow.from_client_secrets_file(
#         "client_secrets.json", SCOPES
#     )
#     credentials = flow.run_local_server(port=0)
#     return build("youtube", "v3", credentials=credentials)

# # Step 2: Get all uploaded videos
# def get_uploaded_videos(youtube, channel_id):
#     video_ids = []
#     request = youtube.search().list(
#         part="id",
#         channelId=channel_id,
#         maxResults=50,
#         type="video"
#     )
#     response = request.execute()
    
#     for item in response.get("items", []):
#         video_ids.append(item["id"]["videoId"])

#     return video_ids

# # Step 3: Post a comment
# def post_comment(youtube, video_id, comment_text):
#     request = youtube.commentThreads().insert(
#         part="snippet",
#         body={
#             "snippet": {
#                 "videoId": video_id,
#                 "topLevelComment": {
#                     "snippet": {
#                         "textOriginal": comment_text
#                     }
#                 }
#             }
#         }
#     )
#     response = request.execute()
#     return response["id"]  # Comment ID for pinning

# # Step 4: Pin the comment
# def pin_comment(youtube, comment_id):
#     request = youtube.comments().setModerationStatus(
#         id=comment_id,
#         moderationStatus="published"
#     )
#     request.execute()

# # Main function
# if __name__ == "__main__":
#     youtube = authenticate()
#     channel_id = "UC9QUvaen12xQfY2HT14H7qw"  # Replace with your channel ID
#     whatsapp_link = "https://whatsapp.com/channel/0029VaurdEY0wajrnyeAl50Y"  # Replace with your WhatsApp channel link
#     comment_text = f"📢 Join our WhatsApp Channel for Novel PDFS: {whatsapp_link}"

#     video_ids = get_uploaded_videos(youtube, channel_id)
#     for video_id in video_ids:
#         print(f"Posting comment on video: {video_id}")
#         comment_id = post_comment(youtube, video_id, comment_text)
#         time.sleep(2)  # Avoid rate limits
#         print(f"Pinning comment: {comment_id}")
#         pin_comment(youtube, comment_id)
#         time.sleep(2)

#     print("✅ All comments posted and pinned successfully!")









from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import random
import time

# Step 1: Authentication
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json", SCOPES
    )
    credentials = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=credentials)

# Step 2: Get all uploaded videos
def get_uploaded_videos(youtube, channel_id):
    video_ids = []
    request = youtube.search().list(
        part="id,snippet",
        channelId=channel_id,
        maxResults=50,
        type="video"
    )
    response = request.execute()
    
    for item in response.get("items", []):
        video_ids.append((item["id"]["videoId"], item["snippet"]["title"]))

    return video_ids

# Step 3: Generate random engaging comment
def generate_comment(video_title, whatsapp_link):
    variations = [
        f"📢 {video_title} dekhne ke baad aur novels parhna chahte hain? Free PDFs ke liye hamare WhatsApp channel ko join karein: {whatsapp_link}",
        f"📖 Aapko {video_title} pasand aya? To Urdu novels ka treasure house join karein: {whatsapp_link}",
        f"📚 Exclusive Urdu Novels ke liye hamare WhatsApp channel ka hissa banein! Link: {whatsapp_link}",
        f"🔥 {video_title} jese aur bhi zabardast novels chahiye? Hamara WhatsApp channel join karein: {whatsapp_link}",
        f"💡 Free Urdu novels aur exclusive updates ke liye abhi join karein: {whatsapp_link}",
        f"📜 Novel lovers ka ek hi adda! Urdu novels ki duniya ka hissa banne ke liye join karein: {whatsapp_link}",
        f"🌟 Best Urdu novels aur daily updates chahiye? Join our exclusive WhatsApp channel now! {whatsapp_link}",
        f"📌 Har roz naye novels aur special recommendations! WhatsApp channel join karein: {whatsapp_link}",
        f"📖 Urdu novel lovers ki community ka hissa banein aur naye novels sab se pehle hasil karein! {whatsapp_link}",
        f"📝 Free novel PDFs, exclusive recommendations aur special discussions ke liye join karein: {whatsapp_link}",
        f"🔔 Urdu novels aur kahaniyon ki har nai update sab se pehle paane ke liye join karein: {whatsapp_link}",
        f"📚 Urdu novels ka unlimited collection! Abhi hamare WhatsApp channel ka hissa banein: {whatsapp_link}",
        f"🎉 Best-selling Urdu novels aur hidden gems ki list chahiye? Join WhatsApp now: {whatsapp_link}",
        f"✨ Urdu adab aur naye novels ka treasure hunt! Free PDFs ke liye WhatsApp join karein: {whatsapp_link}",
        f"💖 Urdu novels ki duniya ka hissa banein! Naye aur rare novels ke liye abhi join karein: {whatsapp_link}",
        f"🌟 {video_title} pasand aya? Aur bhi mazaydar Urdu novels milengi sirf hamare WhatsApp channel par! {whatsapp_link}",
    ]
    return random.choice(variations)

# Step 4: Post a comment
def post_comment(youtube, video_id, comment_text):
    request = youtube.commentThreads().insert(
        part="snippet",
        body={
            "snippet": {
                "videoId": video_id,
                "topLevelComment": {
                    "snippet": {
                        "textOriginal": comment_text
                    }
                }
            }
        }
    )
    response = request.execute()
    return response["id"]  # Comment ID for pinning

# Step 5: Pin the comment
def pin_comment(youtube, comment_id):
    request = youtube.comments().setModerationStatus(
        id=comment_id,
        moderationStatus="published"
    )
    request.execute()

# Main function
if __name__ == "__main__":
    youtube = authenticate()
    channel_id = "UC9QUvaen12xQfY2HT14H7qw"  # Replace with your channel ID
    whatsapp_link = "https://whatsapp.com/channel/0029VaurdEY0wajrnyeAl50Y"  # Replace with your WhatsApp channel link

    video_data = get_uploaded_videos(youtube, channel_id)

    for video_id, video_title in video_data:
        comment_text = generate_comment(video_title, whatsapp_link)
        print(f"Posting comment on video: {video_id} - {video_title}")

        try:
            comment_id = post_comment(youtube, video_id, comment_text)
            time.sleep(2)  # Avoid rate limits
            
            print(f"Pinning comment: {comment_id}")
            pin_comment(youtube, comment_id)
            time.sleep(2)

        except Exception as e:
            print(f"❌ Error on {video_id}: {e}")

    print("✅ All comments posted and pinned successfully!")
