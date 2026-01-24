import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# --- CONFIGURATION (Aapka hard-coded path) ---
FILE_PATH = r"E:\My-Workstation\Coding\Web Scraping\whatsapp channel\urdu_novel_posts.txt" 
# ----------------------------------------------

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com")

print("Dost! Pehle QR Code scan karein aur Channel open karein.")
input("Jab Channel open ho jaye, to 'Enter' dabayein...")

def scrape_channel():
    # Behtar Selector: Sirf message text ko target karne ke liye
    messages = driver.find_elements(By.CSS_SELECTOR, "span.selectable-text.copyable-text")
    
    content_list = []
    seen_texts = set() # Duplicates ko filter karne ke liye

    for msg in messages:
        text = msg.text.strip()
        
        # Check: Duplicate filter logic
        if text and text not in seen_texts:
            content_list.append(text)
            seen_texts.add(text)
    
    # File Save Logic
    try:
        # Path check: Agar folders nahi bane hue to create karega
        folder = os.path.dirname(FILE_PATH)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for line in content_list:
                f.write(line + "\n" + "-"*30 + "\n")
        
        print(f"\nBehtareen! Total {len(content_list)} unique posts save ho gayi hain.")
        print(f"File Path: {FILE_PATH}")
        
    except Exception as e:
        print(f"Error: Path access karne mein masla aa raha hai. Details: {e}")

scrape_channel()
# driver.quit()






# import time
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# # --- CONFIGURATION (Yahan hard-code karein) ---
# # Windows ke liye r"..." use karein taake backslashes ka masla na ho
# FILE_PATH = r"E:\My-Workstation\Coding\Web Scraping\whatsapp channel/urdu_novel_posts.txt" 
# # ----------------------------------------------

# # 1. Browser Setup
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://web.whatsapp.com")

# print("Dost! Pehle QR Code scan karein aur phir wo Channel open karein.")

# # 2. Wait for User
# input("Jab Channel open ho jaye, to 'Enter' dabayein...")

# # 3. Scraping Logic
# def scrape_channel():
#     # WhatsApp ke text content ke liye common class
#     messages = driver.find_elements(By.CSS_SELECTOR, ".copyable-text")
    
#     content_list = []
#     for msg in messages:
#         text = msg.text.strip()
#         if text:
#             content_list.append(text)
    
#     # 4. Save to Hard-coded Path
#     try:
#         # Folder agar nahi bana hua to ye ensure karega ke masla na aaye
#         folder = os.path.dirname(FILE_PATH)
#         if folder and not os.path.exists(folder):
#             os.makedirs(folder)

#         with open(FILE_PATH, "w", encoding="utf-8") as f:
#             for line in content_list:
#                 f.write(line + "\n" + "-"*30 + "\n")
        
#         print(f"\nSuccess! Total {len(content_list)} posts save ho gayi hain.")
#         print(f"Location: {FILE_PATH}")
        
#     except Exception as e:
#         print(f"Error: Path galat hai ya access nahi mil raha. Details: {e}")

# scrape_channel()
# # driver.quit()