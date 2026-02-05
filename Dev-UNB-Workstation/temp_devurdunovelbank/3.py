# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import xml.etree.ElementTree as ET

# # Blogger Sitemap URL
# SITEMAP_URL = "https://itsurdu.blogspot.com/sitemap.xml?page=1"

# # Headers to avoid blocking
# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
# }

# # Step 1: Extract all post URLs from sitemap
# response = requests.get(SITEMAP_URL, headers=HEADERS)

# if response.status_code == 200:
#     root = ET.fromstring(response.content)
#     post_urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
#     print(f"✅ Found {len(post_urls)} posts to scrape.")

# else:
#     print("❌ Failed to fetch sitemap.")
#     exit()

# # Step 2: Function to Scrape Each Novel Post
# def scrape_post(post_url):
#     """ Extracts title and download links from a Blogger post """
#     try:
#         response = requests.get(post_url, headers=HEADERS)
#         if response.status_code != 200:
#             print(f"❌ Failed to fetch {post_url}")
#             return None, "No Link Found"

#         soup = BeautifulSoup(response.text, "html.parser")

#         # Extract Title
#         title_tag = soup.find("h1", class_="post-title entry-title")  # Default Blogger title class
#         if not title_tag:
#             title_tag = soup.find("h3", class_="post-title")  # Alternative Blogger title class
#         if not title_tag:
#             title_tag = soup.find("title")  # Last fallback to <title> tag

#         title = title_tag.text.strip() if title_tag else "No Title Found"

#         # Extract Download Links (Google Drive / Mediafire)
#         links = [a["href"] for a in soup.find_all("a", href=True) if "drive.google" in a["href"] or "mediafire" in a["href"]]
#         download_links = ", ".join(links) if links else "No Link Found"

#         return title, download_links

#     except Exception as e:
#         print(f"⚠ Error scraping {post_url}: {e}")
#         return None, "Error"

# # Step 3: Scrape Each Post & Save Data
# novels_data = []

# for idx, url in enumerate(post_urls[:100]):  # Limit to 100 posts for testing
#     print(f"🔍 Scraping {idx+1}/{len(post_urls)}: {url}")
#     title, download_links = scrape_post(url)
#     if title:
#         novels_data.append({"Title": title, "Download Links": download_links})

#     time.sleep(1)  # Delay to avoid getting blocked

# # Step 4: Save to Excel
# df = pd.DataFrame(novels_data)
# df.to_excel("Blogger_Novels.xlsx", index=False)

# print("✅ Scraping complete! Data saved in 'Blogger_Novels.xlsx'.")









# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import xml.etree.ElementTree as ET

# # Blogger Sitemap URL
# SITEMAP_URL = "https://itsurdu.blogspot.com/sitemap.xml?page=1"

# # Headers to avoid blocking
# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
# }

# # Step 1: Extract all post URLs from sitemap
# response = requests.get(SITEMAP_URL, headers=HEADERS)

# if response.status_code == 200:
#     root = ET.fromstring(response.content)
#     post_urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
#     print(f"✅ Found {len(post_urls)} posts to scrape.")

# else:
#     print("❌ Failed to fetch sitemap.")
#     exit()

# # Step 2: Function to Scrape Each Novel Post
# def scrape_post(post_url):
#     """ Extracts title and ALL download links from a Blogger post """
#     try:
#         response = requests.get(post_url, headers=HEADERS)
#         if response.status_code != 200:
#             print(f"❌ Failed to fetch {post_url}")
#             return None, "No Link Found", "No Link Found"

#         soup = BeautifulSoup(response.text, "html.parser")

#         # Extract Title
#         title_tag = soup.find("h1", class_="post-title entry-title")  # Default Blogger title class
#         if not title_tag:
#             title_tag = soup.find("h3", class_="post-title")  # Alternative Blogger title class
#         if not title_tag:
#             title_tag = soup.find("title")  # Last fallback to <title> tag

#         title = title_tag.text.strip() if title_tag else "No Title Found"

#         # Extract Download Links
#         all_links = [a["href"] for a in soup.find_all("a", href=True)]
        
#         # Separate Google Drive & Mediafire Links
#         google_drive_links = [link for link in all_links if "drive.google" in link]
#         mediafire_links = [link for link in all_links if "mediafire" in link]

#         google_drive_links_str = ", ".join(google_drive_links) if google_drive_links else "No Google Drive Link"
#         mediafire_links_str = ", ".join(mediafire_links) if mediafire_links else "No Mediafire Link"

#         return title, google_drive_links_str, mediafire_links_str

#     except Exception as e:
#         print(f"⚠ Error scraping {post_url}: {e}")
#         return None, "Error", "Error"

# # Step 3: Scrape Each Post & Save Data
# novels_data = []

# for idx, url in enumerate(post_urls[:100]):  # Limit to 100 posts for testing
#     print(f"🔍 Scraping {idx+1}/{len(post_urls)}: {url}")
#     title, google_drive_links, mediafire_links = scrape_post(url)
#     if title:
#         novels_data.append({
#             "Title": title,
#             "Google Drive Links": google_drive_links,
#             "Mediafire Links": mediafire_links
#         })

#     time.sleep(1)  # Delay to avoid getting blocked

# # Step 4: Save to Excel
# df = pd.DataFrame(novels_data)
# df.to_excel("Blogger_Novels.xlsx", index=False)

# print("✅ Scraping complete! Data saved in 'Blogger_Novels.xlsx'.")



#FOR BLOGGER SITEMAP 
#RANDOM SITEMAP







# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import xml.etree.ElementTree as ET

# # Blogger Sitemap URL
# SITEMAP_URL = "https://itsurdu.blogspot.com/sitemap.xml?page=1"

# # Headers to avoid blocking
# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
# }

# # Step 1: Extract all post URLs from sitemap
# response = requests.get(SITEMAP_URL, headers=HEADERS)

# if response.status_code == 200:
#     root = ET.fromstring(response.content)
#     post_urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
#     print(f"✅ Found {len(post_urls)} posts to scrape.")

# else:
#     print("❌ Failed to fetch sitemap.")
#     exit()

# # Step 2: Function to Scrape Each Novel Post
# def scrape_post(post_url):
#     """ Extracts title and ALL download links from a Blogger post """
#     try:
#         response = requests.get(post_url, headers=HEADERS)
#         if response.status_code != 200:
#             print(f"❌ Failed to fetch {post_url}")
#             return None, "No Link Found", "No Link Found"

#         soup = BeautifulSoup(response.text, "html.parser")

#         # Extract Title
#         title_tag = soup.find("h1", class_="post-title entry-title")  # Default Blogger title class
#         if not title_tag:
#             title_tag = soup.find("h3", class_="post-title")  # Alternative Blogger title class
#         if not title_tag:
#             title_tag = soup.find("title")  # Last fallback to <title> tag

#         title = title_tag.text.strip() if title_tag else "No Title Found"

#         # Extract Download Links
#         all_links = [a["href"] for a in soup.find_all("a", href=True)]
        
#         # Separate Google Drive & Mediafire Links
#         google_drive_links = [link for link in all_links if "drive.google" in link]
#         mediafire_links = [link for link in all_links if "mediafire" in link]

#         google_drive_links_str = ", ".join(google_drive_links) if google_drive_links else "No Google Drive Link"
#         mediafire_links_str = ", ".join(mediafire_links) if mediafire_links else "No Mediafire Link"

#         return title, google_drive_links_str, mediafire_links_str

#     except Exception as e:
#         print(f"⚠ Error scraping {post_url}: {e}")
#         return None, "Error", "Error"

# # Step 3: Scrape Each Post & Save Data
# novels_data = []

# for idx, url in enumerate(post_urls):  # Scrape ALL posts
#     print(f"🔍 Scraping {idx+1}/{len(post_urls)}: {url}")
#     title, google_drive_links, mediafire_links = scrape_post(url)
#     if title:
#         novels_data.append({
#             "Title": title,
#             "Google Drive Links": google_drive_links,
#             "Mediafire Links": mediafire_links
#         })

#     time.sleep(1)  # Delay to prevent blocking

# # Step 4: Save to Excel
# df = pd.DataFrame(novels_data)
# df.to_excel("Blogger_Novels.xlsx", index=False)

# print("✅ Scraping complete! Data saved in 'Blogger_Novels.xlsx'.")




import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import xml.etree.ElementTree as ET
import os

# Blogger Sitemap URL
SITEMAP_URL = "https://urdureadings.com/post-sitemap2.xml"

# Headers to prevent blocking
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

# Load last progress
PROGRESS_FILE = "progress.txt"
if os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, "r") as f:
        last_index = int(f.read().strip())
else:
    last_index = 0  # Start from 0 if no progress file exists

# Step 1: Extract all post URLs from sitemap
response = requests.get(SITEMAP_URL, headers=HEADERS)

if response.status_code == 200:
    root = ET.fromstring(response.content)
    post_urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    print(f"✅ Found {len(post_urls)} posts to scrape.")

else:
    print("❌ Failed to fetch sitemap.")
    exit()

# Step 2: Function to Scrape Each Novel Post
def scrape_post(post_url):
    """ Extracts title and ALL download links from a Blogger post """
    try:
        response = requests.get(post_url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            print(f"❌ Failed to fetch {post_url}")
            return None, "No Link Found", "No Link Found"

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract Title with better error handling
        title = "No Title Found"
        title_tags = ["h1.post-title.entry-title", "h3.post-title", "title"]
        for tag in title_tags:
            found_tag = soup.select_one(tag)
            if found_tag:
                title = found_tag.text.strip()
                break

        # Extract Download Links
        all_links = [a["href"] for a in soup.find_all("a", href=True)]
        
        # Separate Google Drive & Mediafire Links
        google_drive_links = [link for link in all_links if "drive.google" in link]
        mediafire_links = [link for link in all_links if "mediafire" in link]

        google_drive_links_str = ", ".join(google_drive_links) if google_drive_links else "No Google Drive Link"
        mediafire_links_str = ", ".join(mediafire_links) if mediafire_links else "No Mediafire Link"

        return title, google_drive_links_str, mediafire_links_str

    except Exception as e:
        print(f"⚠ Error scraping {post_url}: {e}")
        return None, "Error", "Error"

# Step 3: Scrape Each Post & Save Data
novels_data = []

for idx in range(last_index, len(post_urls)):  # Resume from last index
    url = post_urls[idx]
    print(f"🔍 Scraping {idx+1}/{len(post_urls)}: {url}")

    title, google_drive_links, mediafire_links = scrape_post(url)
    
    if title:
        novels_data.append({
            "Title": title,
            "Google Drive Links": google_drive_links,
            "Mediafire Links": mediafire_links
        })

    # Save progress after every 10 posts
    if idx % 10 == 0:
        with open(PROGRESS_FILE, "w") as f:
            f.write(str(idx))

    time.sleep(2)  # Increase delay to prevent blocking

# Step 4: Save to Excel
df = pd.DataFrame(novels_data)
df.to_excel("Blogger_Novels.xlsx", index=False)

# Delete progress file after successful completion
if os.path.exists(PROGRESS_FILE):
    os.remove(PROGRESS_FILE)

print("✅ Scraping complete! Data saved in 'Blogger_Novels.xlsx'.")
