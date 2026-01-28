# save as blogger_to_pinterest.py
import requests
from bs4 import BeautifulSoup
import time

# ========== CONFIG ==========
BLOG_URL = "https://YOURBLOGNAME.blogspot.com"   # <-- replace
PINTEREST_ACCESS_TOKEN = "EAAAx...your_token_here"  # <-- replace with your Pinterest Bearer token
BOARD_ID = "123456789012345678"  # <-- replace with your Pinterest board id
# optional: limit how many to process this run
MAX_POSTS = 50
DELAY_BETWEEN_PINS = 2  # seconds (be polite; adjust)
# ============================

# helper: fetch blog posts via Blogger JSON feed (public)
def fetch_posts(blog_url, max_results=100):
    feed_url = f"{blog_url.rstrip('/')}/feeds/posts/default?alt=json&max-results={max_results}"
    r = requests.get(feed_url, timeout=20)
    r.raise_for_status()
    data = r.json()
    # old Blogger JSON structure: data['feed']['entry'] often exists
    entries = data.get("feed", {}).get("entry", [])
    return entries

# helper: extract title, post url, first image url, and summary
def parse_entry(entry):
    # title
    title = entry.get("title", {}).get("$t", "") or entry.get("title", "")
    # post link (find alternate link rel)
    post_url = ""
    if "link" in entry:
        for ln in entry["link"]:
            if ln.get("rel") == "alternate":
                post_url = ln.get("href")
                break
    # content/html may be in 'content.$t' or 'summary.$t'
    content_html = entry.get("content", {}).get("$t") or entry.get("summary", {}).get("$t", "") or ""
    # parse first image
    soup = BeautifulSoup(content_html, "html.parser")
    img_tag = soup.find("img")
    image_url = img_tag["src"] if img_tag and img_tag.get("src") else None
    # build description (you can customise)
    description = soup.get_text()[:300]  # short text summary
    return {
        "title": title,
        "post_url": post_url,
        "image_url": image_url,
        "description": description,
    }

# helper: create a pin on Pinterest using image URL
def create_pin(access_token, board_id, title, description, image_url, link=None):
    url = "https://api.pinterest.com/v5/pins"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "board_id": board_id,
        "title": title,
        "alt_text": title,
        "description": description,
        # If the image is publicly accessible, we can reference it:
        "media_source": {
            "source_type": "image_url",
            "url": image_url
        }
    }
    if link:
        payload["link"] = link
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    return r

def main():
    print("Fetching posts...")
    entries = fetch_posts(BLOG_URL, max_results=MAX_POSTS)
    if not entries:
        print("No entries found. Check BLOG_URL and if blog is public.")
        return

    for i, entry in enumerate(entries, start=1):
        post = parse_entry(entry)
        title = post["title"]
        img = post["image_url"]
        link = post["post_url"]
        desc = post["description"] or title

        print(f"[{i}] {title}")
        if not img:
            print("  -> no image found in post; skipping.")
            continue

        try:
            resp = create_pin(PINTEREST_ACCESS_TOKEN, BOARD_ID, title, desc, img, link)
            if resp.status_code in (200, 201):
                print(f"  -> Pin created successfully (status {resp.status_code}).")
            else:
                print(f"  -> Failed to create pin: {resp.status_code} {resp.text}")
                # optionally: break or continue after logging
        except Exception as e:
            print(f"  -> Exception while creating pin: {e}")

        time.sleep(DELAY_BETWEEN_PINS)

if __name__ == "__main__":
    main()
