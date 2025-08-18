# import requests
# from bs4 import BeautifulSoup
# import os

# # Base URL with category ID and pagination parameter
# BASE_URL = "https://thisaccessories.com/reading-base/?cat=159&paged="
# START_PAGE = 1
# END_PAGE = 5

# # Directory to save downloaded images
# OUTPUT_DIR = "downloaded_digest_images"
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# for page_num in range(START_PAGE, END_PAGE + 1):
#     url = f"{BASE_URL}{page_num}"
#     print(f"[+] Fetching page {page_num}: {url}")

#     try:
#         response = requests.get(url)
#         if response.status_code != 200:
#             print(f"[!] Failed to load page {page_num} (status {response.status_code})")
#             continue

#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find the first image on the page
#         img_tag = soup.find('img')
#         if img_tag and 'src' in img_tag.attrs:
#             img_url = img_tag['src']
#             print(f"[+] Found image: {img_url}")

#             # Download the image
#             img_data = requests.get(img_url).content
#             img_filename = os.path.join(OUTPUT_DIR, f"page_{page_num}.jpg")

#             with open(img_filename, 'wb') as f:
#                 f.write(img_data)
#             print(f"[✓] Saved to {img_filename}")

#         else:
#             print(f"[!] No image found on page {page_num}")

#     except Exception as e:
#         print(f"[!] Error on page {page_num}: {e}")

# print("[✓] All done!")







# import requests
# from bs4 import BeautifulSoup
# import os

# # Base URL with category ID and pagination parameter
# BASE_URL = "https://thisaccessories.com/reading-base/?cat=159&paged="
# START_PAGE = 1
# END_PAGE = 5   # <-- Only scrape first 5 pages

# # Directory to save downloaded images
# OUTPUT_DIR = "downloaded_digest_images"
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# for page_num in range(START_PAGE, END_PAGE + 1):
#     url = f"{BASE_URL}{page_num}"
#     print(f"[+] Fetching page {page_num}: {url}")

#     try:
#         response = requests.get(url)
#         if response.status_code != 200:
#             print(f"[!] Failed to load page {page_num} (status {response.status_code})")
#             continue

#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find the first image on the page
#         img_tag = soup.find('img')
#         if img_tag and 'src' in img_tag.attrs:
#             img_url = img_tag['src']
#             print(f"[+] Found image: {img_url}")

#             # Download the image
#             img_data = requests.get(img_url).content
#             img_filename = os.path.join(OUTPUT_DIR, f"page_{page_num}.jpg")

#             with open(img_filename, 'wb') as f:
#                 f.write(img_data)
#             print(f"[✓] Saved to {img_filename}")

#         else:
#             print(f"[!] No image found on page {page_num}")

#     except Exception as e:
#         print(f"[!] Error on page {page_num}: {e}")

# print("[✓] All done!")






# import requests
# from bs4 import BeautifulSoup
# import os

# BASE_URL = "https://thisaccessories.com/reading-base/?cat=159&paged="
# START_PAGE = 1
# END_PAGE = 5

# OUTPUT_DIR = "downloaded_digest_images"
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# for page_num in range(START_PAGE, END_PAGE + 1):
#     url = f"{BASE_URL}{page_num}"
#     print(f"[+] Fetching page {page_num}: {url}")

#     try:
#         response = requests.get(url)
#         if response.status_code != 200:
#             print(f"[!] Failed to load page {page_num} (status {response.status_code})")
#             continue

#         soup = BeautifulSoup(response.text, 'html.parser')

#         img_tag = soup.find('img')
#         if img_tag and 'src' in img_tag.attrs:
#             img_url = img_tag['src']
#             print(f"[+] Image found: {img_url}")

#             # IMMEDIATELY download and save the image
#             img_data = requests.get(img_url).content
#             img_filename = os.path.join(OUTPUT_DIR, f"page_{page_num}.jpg")
#             with open(img_filename, 'wb') as f:
#                 f.write(img_data)

#             print(f"[✓] Image downloaded and saved as {img_filename}")

#         else:
#             print(f"[!] No image found on page {page_num}")

#     except Exception as e:
#         print(f"[!] Error on page {page_num}: {e}")

# print("[✓] Done downloading first 5 pages!")



# import requests
# from bs4 import BeautifulSoup
# import os

# BASE_URL = "https://thisaccessories.com/reading-base/?cat=159&paged="
# START_PAGE = 1
# END_PAGE = 5

# OUTPUT_DIR = "downloaded_digest_images"
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# print(f"[*] Saving images to: {os.path.abspath(OUTPUT_DIR)}")

# for page_num in range(START_PAGE, END_PAGE + 1):
#     url = f"{BASE_URL}{page_num}"
#     print(f"[+] Fetching page {page_num}: {url}")

#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')

#         img_tags = soup.find_all('img')
#         print(f"[{page_num}] Found {len(img_tags)} image(s)")

#         for i, tag in enumerate(img_tags):
#             img_url = tag.get('src')
#             print(f"  Image {i+1}: {img_url}")

#             if img_url and "wp-content/uploads" in img_url:
#                 # This is likely the correct image
#                 img_data = requests.get(img_url).content
#                 img_filename = os.path.join(OUTPUT_DIR, f"page_{page_num}.jpg")

#                 with open(img_filename, 'wb') as f:
#                     f.write(img_data)

#                 print(f"[✓] Saved image {img_url} as {img_filename}")
#                 break  # Save only first matching image

#     except Exception as e:
#         print(f"[!] Error on page {page_num}: {e}")

# print("[✓] Done downloading!")













# import requests
# from bs4 import BeautifulSoup
# import os

# # URL of the page containing the digest
# url = "https://thisaccessories.com/reading-base/?cat=159&paged=2"

# # Create a directory to save images
# if not os.path.exists("digest_images"):
#     os.makedirs("digest_images")

# # Send a GET request to the webpage
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find all img tags
# images = soup.find_all('img')

# # Download each image
# for index, img in enumerate(images):
#     img_url = img.get('src')
#     if img_url:
#         if not img_url.startswith('http'):
#             img_url = url.rstrip('/') + '/' + img_url
#         try:
#             img_data = requests.get(img_url).content
#             with open(f"digest_images/image_{index}.jpg", 'wb') as handler:
#                 handler.write(img_data)
#             print(f"Downloaded image_{index}.jpg")
#         except Exception as e:
#             print(f"Failed to download {img_url}: {e}")

















# import requests
# from bs4 import BeautifulSoup
# import os

# # URL of the page containing the digest
# url = "https://thisaccessories.com/reading-base/?cat=159&paged=2"

# # Create a directory to save images
# if not os.path.exists("digest_images"):
#     os.makedirs("digest_images")

# # Send a GET request to the webpage
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find all img tags
# images = soup.find_all('img')

# # Download only the first 5 images
# for index, img in enumerate(images[:5]):
#     img_url = img.get('src')
#     if img_url:
#         if not img_url.startswith('http'):
#             img_url = url.rstrip('/') + '/' + img_url
#         try:
#             img_data = requests.get(img_url).content
#             with open(f"digest_images/image_{index}.jpg", 'wb') as handler:
#                 handler.write(img_data)
#             print(f"Downloaded image_{index}.jpg")
#         except Exception as e:
#             print(f"Failed to download {img_url}: {e}")














# import requests
# from bs4 import BeautifulSoup
# import os
# import base64

# # URL of the page containing the digest
# url = "https://thisaccessories.com/reading-base/?cat=159&paged=2"

# # Create a directory to save images
# if not os.path.exists("digest_images"):
#     os.makedirs("digest_images")

# # Send a GET request to the webpage
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find all img tags with base64 data
# images = soup.find_all('img', src=lambda x: x and x.startswith('data:image/jpeg;base64'))

# # Decode and save the first 5 images
# for index, img in enumerate(images[:5]):
#     if img.get('src'):
#         try:
#             # Extract the base64 data (remove the prefix)
#             base64_data = img['src'].split(',')[1]
#             # Decode the base64 data to binary
#             img_data = base64.b64decode(base64_data)
#             # Save the image
#             with open(f"digest_images/image_{index}.jpg", 'wb') as handler:
#                 handler.write(img_data)
#             print(f"Downloaded image_{index}.jpg")
#         except Exception as e:
#             print(f"Failed to download image_{index}: {e}")









import requests
from bs4 import BeautifulSoup
import os
import base64

# URL of the page containing the digest
url = "https://thisaccessories.com/reading-base/?cat=159&paged=4"

# Create a directory to save images
if not os.path.exists("digest_images"):
    os.makedirs("digest_images")

# Send a GET request to the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all img tags with base64 data
images = soup.find_all('img', src=lambda x: x and x.startswith('data:image/jpeg;base64'))

# Decode and save the first 5 images
for index, img in enumerate(images[:5]):
    if img.get('src'):
        try:
            # Extract the base64 data (remove the prefix)
            base64_data = img['src'].split(',')[1]
            # Check if the base64 string is valid
            if base64_data and len(base64.b64decode(base64_data, validate=True)) > 0:
                img_data = base64.b64decode(base64_data)
                with open(f"digest_images/image_{index}.jpg", 'wb') as handler:
                    handler.write(img_data)
                print(f"Downloaded image_{index}.jpg")
            else:
                print(f"Skipped image_{index}: Invalid or empty Base64 data")
        except Exception as e:
            print(f"Failed to download image_{index}: {e}")

            import os
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL of the page containing the digest
url = "https://thisaccessories.com/reading-base/?cat=159&paged=2"

# Create a directory to save images
if not os.path.exists("digest_images"):
    os.makedirs("digest_images")

# Load the page and wait for JavaScript to render
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all img tags with base64 data
images = soup.find_all('img', src=lambda x: x and x.startswith('data:image/jpeg;base64'))

# Decode and save the first 5 images
for index, img in enumerate(images[:5]):
    if img.get('src'):
        try:
            # Extract the base64 data (remove the prefix)
            base64_data = img['src'].split(',')[1]
            # Check if the base64 string is valid
            if base64_data and len(base64.b64decode(base64_data, validate=True)) > 0:
                img_data = base64.b64decode(base64_data)
                with open(f"digest_images/image_{index}.jpg", 'wb') as handler:
                    handler.write(img_data)
                print(f"Downloaded image_{index}.jpg")
            else:
                print(f"Skipped image_{index}: Invalid or empty Base64 data")
        except Exception as e:
            print(f"Failed to download image_{index}: {e}")

# Close the browser
driver.quit()