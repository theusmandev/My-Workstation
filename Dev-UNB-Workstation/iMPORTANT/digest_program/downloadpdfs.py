# # import pandas as pd
# # import os
# # import re
# # import requests
# # from bs4 import BeautifulSoup

# # # Input Excel file
# # input_file = r"D:\unb-workstation\writers\digest\Shua_sorted by time.xlsx"
# # output_folder = r"D:\unb-workstation\writers\downloads"

# # os.makedirs(output_folder, exist_ok=True)

# # # Read Excel
# # df = pd.read_excel(input_file)

# # def get_gdrive_direct_link(url):
# #     match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
# #     if match:
# #         file_id = match.group(1)
# #         return f"https://drive.google.com/uc?export=download&id={file_id}"
# #     return None

# # def get_mediafire_direct_link(url):
# #     try:
# #         page = requests.get(url).text
# #         soup = BeautifulSoup(page, "html.parser")
# #         dl_link = soup.find("a", {"id": "downloadButton"})["href"]
# #         return dl_link
# #     except Exception as e:
# #         print(f"❌ Mediafire link error: {e}")
# #         return None

# # def download_file(url, title):
# #     try:
# #         r = requests.get(url, stream=True)
# #         if r.status_code == 200:
# #             file_path = os.path.join(output_folder, f"{title}.pdf")
# #             with open(file_path, "wb") as f:
# #                 for chunk in r.iter_content(1024):
# #                     f.write(chunk)
# #             print(f"✅ Downloaded: {file_path}")
# #         else:
# #             print(f"❌ Failed: {title}")
# #     except Exception as e:
# #         print(f"⚠️ Error downloading {title}: {e}")

# # # Loop through rows
# # for _, row in df.iterrows():
# #     title = str(row["Titles"]).strip()
# #     link = str(row["Links"]).strip()

# #     if "drive.google.com" in link:
# #         direct_link = get_gdrive_direct_link(link)
# #     elif "mediafire.com" in link:
# #         direct_link = get_mediafire_direct_link(link)
# #     else:
# #         print(f"⚠️ Unknown link type: {link}")
# #         continue

# #     if direct_link:
# #         download_file(direct_link, title)









# import pandas as pd
# import os
# import re
# import requests
# from bs4 import BeautifulSoup

# # Input Excel file
# input_file = r"D:\unb-workstation\writers\digest\Shua_sorted by time.xlsx"
# output_folder = r"D:\unb-workstation\writers\downloads"

# os.makedirs(output_folder, exist_ok=True)

# # Read Excel
# print("📂 Reading Excel file...")
# df = pd.read_excel(input_file)
# print(f"✅ Loaded {len(df)} rows from {input_file}")

# def get_gdrive_direct_link(url):
#     match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
#     if match:
#         file_id = match.group(1)
#         return f"https://drive.google.com/uc?export=download&id={file_id}"
#     return None

# def get_mediafire_direct_link(url):
#     try:
#         page = requests.get(url).text
#         soup = BeautifulSoup(page, "html.parser")
#         btn = soup.find("a", {"id": "downloadButton"})
#         if btn and "href" in btn.attrs:
#             return btn["href"]
#         else:
#             print("⚠️ Mediafire download button not found")
#             return None
#     except Exception as e:
#         print(f"❌ Mediafire link error: {e}")
#         return None

# def download_file(url, title):
#     try:
#         print(f"⬇️ Downloading: {title} from {url}")
#         r = requests.get(url, stream=True)
#         if r.status_code == 200:
#             file_path = os.path.join(output_folder, f"{title}.pdf")
#             with open(file_path, "wb") as f:
#                 for chunk in r.iter_content(1024):
#                     f.write(chunk)
#             print(f"✅ Saved as: {file_path}")
#         else:
#             print(f"❌ Failed with status {r.status_code}: {title}")
#     except Exception as e:
#         print(f"⚠️ Error downloading {title}: {e}")

# # Loop through rows
# for i, row in df.iterrows():
#     title = str(row["Titles"]).strip()
#     link = str(row["Links"]).strip()

#     print(f"\n[{i+1}] Processing: {title}")
#     if "drive.google.com" in link:
#         direct_link = get_gdrive_direct_link(link)
#         print(f"   → Google Drive link detected")
#     elif "mediafire.com" in link:
#         direct_link = get_mediafire_direct_link(link)
#         print(f"   → Mediafire link detected")
#     else:
#         print(f"⚠️ Unknown link type: {link}")
#         continue

#     if direct_link:
#         download_file(direct_link, title)
#     else:
#         print(f"❌ Could not extract direct link for {title}")





# import pandas as pd
# import os
# import re
# import requests
# from bs4 import BeautifulSoup

# # Input Excel file
# input_file = r"D:\unb-workstation\writers\digest\Shua_sorted by time.xlsx"
# output_folder = r"D:\unb-workstation\writers\digest\downloads"

# os.makedirs(output_folder, exist_ok=True)

# # Read Excel
# print("📂 Reading Excel file...")
# df = pd.read_excel(input_file)
# print(f"✅ Loaded {len(df)} rows from {input_file}")

# def get_gdrive_direct_link(url):
#     match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
#     if match:
#         file_id = match.group(1)
#         return f"https://drive.google.com/uc?export=download&id={file_id}"
#     return None

# def get_mediafire_direct_link(url):
#     try:
#         page = requests.get(url).text
#         soup = BeautifulSoup(page, "html.parser")
#         btn = soup.find("a", {"id": "downloadButton"})
#         if btn and "href" in btn.attrs:
#             return btn["href"]
#         else:
#             return None
#     except Exception:
#         return None

# def download_file(url, title, original_link):
#     try:
#         print(f"⬇️ Downloading: {title} from {url}")
#         r = requests.get(url, stream=True)
#         if r.status_code == 200 and "html" not in r.headers.get("Content-Type", ""):
#             file_path = os.path.join(output_folder, f"{title}.pdf")
#             with open(file_path, "wb") as f:
#                 for chunk in r.iter_content(1024):
#                     f.write(chunk)
#             print(f"✅ Saved as: {file_path}")
#         else:
#             # fallback: save the link in a text file
#             fallback_file = os.path.join(output_folder, f"{title}.txt")
#             with open(fallback_file, "w", encoding="utf-8") as f:
#                 f.write(f"Manual download required:\n{original_link}")
#             print(f"⚠️ Could not auto-download. Saved link instead: {fallback_file}")
#     except Exception as e:
#         print(f"⚠️ Error downloading {title}: {e}")

# # Loop through rows
# for i, row in df.iterrows():
#     title = str(row["Titles"]).strip()
#     link = str(row["Links"]).strip()

#     print(f"\n[{i+1}] Processing: {title}")
#     direct_link = None

#     if "drive.google.com" in link:
#         direct_link = get_gdrive_direct_link(link)
#         print("   → Google Drive link detected")
#     elif "mediafire.com" in link:
#         direct_link = get_mediafire_direct_link(link)
#         print("   → Mediafire link detected")
#     else:
#         print(f"⚠️ Unknown link type: {link}")
#         continue

#     # اگر direct link نہ ملے تو original link کو ہی fallback کے طور پر رکھیں
#     if direct_link:
#         download_file(direct_link, title, link)
#     else:
#         print("⚠️ No direct link found, using original link as fallback")
#         download_file(link, title, link)









# import pandas as pd
# import os
# import re
# import requests
# from bs4 import BeautifulSoup

# # Input Excel file
# input_file = r"D:\unb-workstation\writers\digest\Shua_sorted by time.xlsx"
# output_folder = r"D:\unb-workstation\writers\downloads"

# os.makedirs(output_folder, exist_ok=True)

# # Read Excel
# print("📂 Reading Excel file...")
# df = pd.read_excel(input_file)
# print(f"✅ Loaded {len(df)} rows from {input_file}")

# # List to collect non-direct links
# fallback_links = []

# def get_gdrive_direct_link(url):
#     match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
#     if match:
#         file_id = match.group(1)
#         return f"https://drive.google.com/uc?export=download&id={file_id}"
#     return None

# def get_mediafire_direct_link(url):
#     try:
#         page = requests.get(url).text
#         soup = BeautifulSoup(page, "html.parser")
#         btn = soup.find("a", {"id": "downloadButton"})
#         if btn and "href" in btn.attrs:
#             return btn["href"]
#         else:
#             return None
#     except Exception:
#         return None

# def download_file(url, title):
#     try:
#         print(f"⬇️ Downloading: {title} from {url}")
#         r = requests.get(url, stream=True)
#         if r.status_code == 200 and "html" not in r.headers.get("Content-Type", ""):
#             file_path = os.path.join(output_folder, f"{title}.pdf")
#             with open(file_path, "wb") as f:
#                 for chunk in r.iter_content(1024):
#                     f.write(chunk)
#             print(f"✅ Saved as: {file_path}")
#             return True
#         else:
#             return False
#     except Exception as e:
#         print(f"⚠️ Error downloading {title}: {e}")
#         return False

# # Loop through rows
# for i, row in df.iterrows():
#     title = str(row["Titles"]).strip()
#     link = str(row["Links"]).strip()

#     print(f"\n[{i+1}] Processing: {title}")
#     direct_link = None

#     if "drive.google.com" in link:
#         direct_link = get_gdrive_direct_link(link)
#         print("   → Google Drive link detected")
#     elif "mediafire.com" in link:
#         direct_link = get_mediafire_direct_link(link)
#         print("   → Mediafire link detected")
#     else:
#         print("⚠️ Unknown link type")

#     # Try downloading if direct link found
#     if direct_link and download_file(direct_link, title):
#         continue
#     else:
#         # Add to fallback list
#         print(f"⚠️ Could not auto-download: {title}")
#         fallback_links.append({"Title": title, "Link": link})

# # Save fallback links in Excel
# if fallback_links:
#     fallback_df = pd.DataFrame(fallback_links)
#     fallback_file = os.path.join(output_folder, "fallback_links.xlsx")
#     fallback_df.to_excel(fallback_file, index=False)
#     print(f"\n📄 Fallback links saved in: {fallback_file}")
# else:
#     print("\n✅ All files downloaded successfully, no fallback links.")






import os
import pandas as pd
import requests

# Paths
input_file = r"D:\unb-workstation\writers\digest\Shua_sorted by time.xlsx"
output_folder = r"D:\unb-workstation\writers\digest\downloaded novels"
failed_links_file = r"D:\unb-workstation\writers\digest\notdownloadedpdfs.txt"

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Read Excel
df = pd.read_excel(input_file)

# فرض کیا کہ Excel میں ایک column ہے 'link'
links = df['link'].dropna().tolist()

failed_links = []

for url in links:
    try:
        filename = url.split("/")[-1]
        file_path = os.path.join(output_folder, filename)
        
        response = requests.get(url, timeout=20)
        if response.status_code == 200 and response.headers.get("Content-Type", "").lower().startswith("application/pdf"):
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"✅ Downloaded: {filename}")
        else:
            print(f"❌ Not a direct PDF link: {url}")
            failed_links.append(url)
    except Exception as e:
        print(f"⚠️ Failed: {url} ({e})")
        failed_links.append(url)

# Save failed links
with open(failed_links_file, "w", encoding="utf-8") as f:
    for link in failed_links:
        f.write(link + "\n")

print("🔍 Process finished!")
