import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import xml.etree.ElementTree as ET

# Website's Sitemap URL
SITEMAP_URL = "https://urdureadings.com/post-sitemap1.xml"

# Headers to prevent blocking
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

# List to store novel URLs
novel_urls = []

# Step 1: Fetch Sitemap and Extract Novel URLs
print("📄 Fetching Sitemap...")
sitemap_response = requests.get(SITEMAP_URL, headers=HEADERS)

if sitemap_response.status_code == 200:
    # Parse XML Sitemap
    root = ET.fromstring(sitemap_response.content)

    # Extract URLs from <loc> tags
    for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        url = elem.text
        if "/page/" not in url and "category" not in url and "tag" not in url:  # Ignore category/tag pages
            novel_urls.append(url)

    print(f"✅ Found {len(novel_urls)} novels in sitemap.")

else:
    print("❌ Failed to fetch sitemap. Exiting...")
    exit()

# Step 2: Scrape Novel Pages
novels_data = []

def scrape_novel_page(novel_url):
    """ Extracts title and download links from a novel page """
    try:
        response = requests.get(novel_url, headers=HEADERS)
        if response.status_code != 200:
            print(f"❌ Failed to fetch {novel_url}")
            return None, "No Link Found"

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract Title
        title_tag = soup.find("h1", class_="post-title entry-title")
        title = title_tag.text.strip() if title_tag else "No Title Found"

        # Extract Download Links (Google Drive / Mediafire)
        links = [a["href"] for a in soup.find_all("a", href=True) if "drive.google" in a["href"] or "mediafire" in a["href"]]
        download_links = ", ".join(links) if links else "No Link Found"

        return title, download_links

    except Exception as e:
        print(f"⚠ Error scraping {novel_url}: {e}")
        return None, "Error"

# Scrape each novel page
for idx, url in enumerate(novel_urls):
    print(f"🔍 Scraping {idx+1}/{len(novel_urls)}: {url}")
    title, download_links = scrape_novel_page(url)
    if title:
        novels_data.append({"Title": title, "Download Links": download_links})

    # Short delay to prevent blocking
    time.sleep(1)

# Step 3: Save Data to Excel
df = pd.DataFrame(novels_data)
df.to_excel("Urdu_Novels.xlsx", index=False)

print("✅ Scraping complete! Data saved in 'Urdu_Novels.xlsx'.")
