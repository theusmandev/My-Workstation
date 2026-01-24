import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Browser Setup
options = webdriver.ChromeOptions()
# Agar aap chahte hain ke bar bar login na karna pare, to user-data use karein
# options.add_argument("--user-data-dir=./user-data") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com")

print("Dost! Pehle QR Code scan karein aur phir wo Channel open karein jiska data save karna hai.")

# 2. Wait for User to open the channel
input("Jab aap channel open karlein, to yahan 'Enter' dabayein...")

# 3. Scraping Logic
def scrape_channel():
    # WhatsApp ke message bubbles ki common class 'copyable-text' hoti hai
    messages = driver.find_elements(By.CSS_SELECTOR, ".copyable-text")
    
    content_list = []
    for msg in messages:
        text = msg.text.strip()
        if text:
            content_list.append(text)
    
    # 4. Save to TXT file
    with open("channel_posts.txt", "w", encoding="utf-8") as f:
        for line in content_list:
            f.write(line + "\n" + "-"*30 + "\n")
    
    print(f"Mubarak ho! Total {len(content_list)} posts save ho gayi hain.")

scrape_channel()

# driver.quit()