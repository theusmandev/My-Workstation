


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# 1. Excel Load Karen
df = pd.read_excel('Mediafire_Direct_Links_Updated.xlsx')
fresh_links = []

# 2. Browser Setup
chrome_options = Options()
# chrome_options.add_argument("--headless") # Shuru mein isay off rakhen taake aap captcha dekh saken
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

print("Browser khul raha hai... Agar Captcha aaye to manually solve karen.")

for index, row in df.iterrows():
    url = row['Mediafire Links'] # Column ka sahi naam check kar len
    try:
        driver.get(url)
        
        # Thora intezar taake page load ho jaye
        time.sleep(3) 
        
        # Download button dhoondna
        download_button = driver.find_element(By.ID, 'downloadButton')
        direct_link = download_button.get_attribute('href')
        
        if direct_link:
            print(f"Link {index+1} Refreshed: {direct_link}")
            fresh_links.append(direct_link)
        else:
            fresh_links.append("Failed")
            
    except Exception as e:
        print(f"Link {index+1} par masla aaya. Shayad Captcha hai.")
        input("Captcha solve karke Enter dabayen...") # Script yahan ruk jaye gi taake aap captcha hal karen
        # Dubara koshish
        download_button = driver.find_element(By.ID, 'downloadButton')
        fresh_links.append(download_button.get_attribute('href'))

# 3. Nayi Excel Save Karen
df['Fresh_Direct_Links'] = fresh_links
df.to_excel('Refreshed_Links_Final.xlsx', index=False)
driver.quit()
print("Tamam links refresh ho gaye hain!")








# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import os
# import time

# # 1. Excel file load karen
# input_file = 'Mediafire_Direct_Links_Updated.xlsx'
# df = pd.read_excel(input_file)

# # Download folder
# download_path = "Novels_Refreshed"
# if not os.path.exists(download_path):
#     os.makedirs(download_path)

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
# }

# def get_fresh_link(page_url):
#     try:
#         response = requests.get(page_url, headers=headers, timeout=15)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         btn = soup.find('a', {'id': 'downloadButton'})
#         if btn:
#             return btn.get('href')
#     except:
#         return None

# # 2. Loop through links
# for index, row in df.iterrows():
#     # Original link (jo mediafire.com/file/... wala tha)
#     original_url = row['Mediafire Links'] 
    
#     print(f"Refreshing Link {index+1}...")
#     fresh_link = get_fresh_link(original_url)

#     if fresh_link and "download_repair" not in fresh_link:
#         try:
#             file_name = fresh_link.split('/')[-1].split('?')[0]
#             print(f"Downloading: {file_name}")
            
#             # File download karna
#             r = requests.get(fresh_link, stream=True, headers=headers)
#             with open(os.path.join(download_path, file_name), 'wb') as f:
#                 for chunk in r.iter_content(chunk_size=1024*1024):
#                     f.write(chunk)
#             print("Done!")
            
#         except Exception as e:
#             print(f"Download Error: {e}")
#     else:
#         print(f"Link {index+1} still blocked or not found. Needs manual Captcha.")
    
#     # Gap dena bohat zaroori ha taake block na hon
#     time.sleep(5)