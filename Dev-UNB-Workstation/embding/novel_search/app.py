# from flask import Flask, render_template, request
# import requests
# from bs4 import BeautifulSoup

# app = Flask(__name__)

# # ✅ List of Urdu novel websites
# novel_sites = [
#     "https://kitabnagri.com",
#     "https://urdureadings.com"
# ]

# # ✅ Scraper function
# def search_novel_on_site(site_url, query):
#     search_url = site_url + "/?s=" + query.replace(" ", "+")
#     headers = {"User-Agent": "Mozilla/5.0"}

#     try:
#         response = requests.get(search_url, headers=headers, timeout=10)
#         soup = BeautifulSoup(response.text, "html.parser")

#         post_links = []
#         for a_tag in soup.find_all("a", href=True):
#             href = a_tag['href']
#             if site_url in href and ("/20" in href or "novel" in href):
#                 post_links.append(href)

#         result_links = []
#         query_lower = query.lower()

#         for post_link in post_links:
#             try:
#                 post_res = requests.get(post_link, headers=headers, timeout=10)
#                 post_soup = BeautifulSoup(post_res.text, "html.parser")

#                 # ✅ Check title or h1 for novel match
#                 title_text = post_soup.title.string if post_soup.title else ""
#                 h1_text = post_soup.find("h1").text if post_soup.find("h1") else ""
#                 full_text = title_text + " " + h1_text
#                 if query_lower not in full_text.lower():
#                     continue  # Skip unrelated posts

#                 # ✅ Find download links
#                 for a in post_soup.find_all("a", href=True):
#                     href = a['href']
#                     if "drive.google.com" in href or "mediafire.com" in href:
#                         result_links.append(href)

#             except:
#                 continue
#         return result_links

#     except:
#         return []


# # ✅ Loop through all sites
# def search_all_sites(query):
#     all_links = []
#     for site in novel_sites:
#         links = search_novel_on_site(site, query)
#         all_links.extend(links)
#     return all_links

# # ✅ Routes
# @app.route("/", methods=["GET", "POST"])
# def index():
#     results = []
#     query = ""
#     if request.method == "POST":
#         query = request.form.get("query")
#         results = search_all_sites(query)
#     return render_template("index.html", results=results, query=query)

# if __name__ == "__main__":
#     app.run(debug=True)











from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# ✅ Your novel websites list (add more later)
novel_sites = [
    "https://kitabnagri.com",
    "https://urdureadings.com",
]

headers = {"User-Agent": "Mozilla/5.0"}

# ✅ Scrape a single site
def search_novel_on_site(site_url, query):
    search_url = site_url + "/?s=" + query.replace(" ", "+")
    result_links = []
    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        post_links = []
        for a_tag in soup.find_all("a", href=True):
            href = a_tag['href']
            if site_url in href and ("/20" in href or "novel" in href):
                post_links.append(href)

        query_lower = query.lower()

        for post_link in post_links:
            try:
                post_res = requests.get(post_link, headers=headers, timeout=10)
                post_soup = BeautifulSoup(post_res.text, "html.parser")

                title_text = post_soup.title.string if post_soup.title else ""
                h1_text = post_soup.find("h1").text if post_soup.find("h1") else ""
                full_text = title_text + " " + h1_text

                if query_lower not in full_text.lower():
                    continue  # Skip unrelated posts

                for a in post_soup.find_all("a", href=True):
                    href = a['href']
                    if "drive.google.com" in href or "mediafire.com" in href:
                        result_links.append(href)
            except:
                continue

    except:
        pass

    return result_links

# ✅ Multi-threaded scraping
def search_all_sites(query):
    all_links = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(search_novel_on_site, site, query) for site in novel_sites]
        for future in futures:
            try:
                links = future.result()
                all_links.extend(links)
            except:
                continue
    return all_links

# ✅ Flask route
@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query")
        results = search_all_sites(query)
    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True)
