import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# --- CONFIGURATION (Yahan hard-code karein) ---
# Windows ke liye r"..." use karein taake backslashes ka masla na ho
FILE_PATH = r"E:\My-Workstation\Coding\Web Scraping\whatsapp channel/urdu_novel_posts.txt" 
# ----------------------------------------------

# 1. Browser Setup
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com")

print("Dost! Pehle QR Code scan karein aur phir wo Channel open karein.")

# 2. Wait for User
input("Jab Channel open ho jaye, to 'Enter' dabayein...")

# 3. Scraping Logic
def scrape_channel():
    # WhatsApp ke text content ke liye common class
    messages = driver.find_elements(By.CSS_SELECTOR, ".copyable-text")
    
    content_list = []
    for msg in messages:
        text = msg.text.strip()
        if text:
            content_list.append(text)
    
    # 4. Save to Hard-coded Path
    try:
        # Folder agar nahi bana hua to ye ensure karega ke masla na aaye
        folder = os.path.dirname(FILE_PATH)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for line in content_list:
                f.write(line + "\n" + "-"*30 + "\n")
        
        print(f"\nSuccess! Total {len(content_list)} posts save ho gayi hain.")
        print(f"Location: {FILE_PATH}")
        
    except Exception as e:
        print(f"Error: Path galat hai ya access nahi mil raha. Details: {e}")

scrape_channel()
# driver.quit()