
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

# --- CONFIGURATION ---
FILE_PATH = r"E:\My-Workstation\Coding\Web Scraping\whatsapp channel/urdu_novel_posts.txt" 
SCROLL_COUNT = 10 
SCROLL_PAUSE_TIME = 2.5 
# ---------------------

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com")

print("Dost! QR Code scan karein aur Channel open karein.")
input("Jab Channel open ho jaye, to 'Enter' dabayein...")

def scrape_ordered_channel():
    # Set ki jagah List use karenge taake order save rahe
    ordered_messages = []
    seen_messages = set() # Sirf duplicates check karne ke liye

    try:
        chat_window = driver.find_element(By.TAG_NAME, "body") 
    except:
        print("Chat window nahi mil saki.")
        return

    print("Scraping shuru... Novel ki tarteeb maintain ki ja rahi hai.")

    for i in range(SCROLL_COUNT):
        # Current screen ke messages (Upar se Neechay ki tarteeb mein milte hain)
        current_screen_elements = driver.find_elements(By.CSS_SELECTOR, ".copyable-text")
        
        # Is screen ki messages ko ek temporary list mein dalenge
        temp_list = []
        for msg in current_screen_elements:
            try:
                text = msg.text.strip()
                if text and len(text) > 15:
                    if text not in seen_messages:
                        temp_list.append(text)
                        seen_messages.add(text)
            except StaleElementReferenceException:
                continue

        # Kyunke hum upar scroll kar rahe hain, naye milne wale (purane) messages 
        # list ke shuru (start) mein aane chahiyen
        ordered_messages = temp_list + ordered_messages

        # Scroll Up
        chat_window.send_keys(Keys.PAGE_UP)
        time.sleep(SCROLL_PAUSE_TIME)
        
        print(f"Scroll {i+1}/{SCROLL_COUNT} | Ab tak {len(ordered_messages)} posts tarteeb se jama ho chukin.")

    save_data(ordered_messages)

def save_data(data):
    try:
        folder = os.path.dirname(FILE_PATH)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        with open(FILE_PATH, "w", encoding="utf-8") as f:
            # Ab data pehle se hi chronological order mein hoga
            for post in data:
                f.write(post + "\n" + "-"*30 + "\n")
        
        print(f"\nDone! Novel ki {len(data)} posts sequence mein save ho gayi hain.")
    except Exception as e:
        print(f"File error: {e}")

scrape_ordered_channel()
driver.quit()















#good with scrolling excellent but without tarteeb
# import time
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import StaleElementReferenceException

# # --- CONFIGURATION ---
# FILE_PATH = r"E:\My-Workstation\Coding\Web Scraping\whatsapp channel/urdu_novel_posts.txt" 
# SCROLL_COUNT = 30  
# SCROLL_PAUSE_TIME = 2.5 # Thoda zyada time taake loading stable ho jaye
# # ---------------------

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://web.whatsapp.com")

# print("Dost! QR Code scan karein aur Channel open karein.")
# input("Jab Channel open ho jaye, to 'Enter' dabayein...")

# def scrape_channel_with_scroll():
#     unique_messages = set()
    
#     # Message area find karne ka koshish
#     try:
#         # WhatsApp web ka main scrollable area aksar badalta hai, body par fallback rakhte hain
#         chat_window = driver.find_element(By.TAG_NAME, "body") 
#     except:
#         print("Chat window nahi mil saki.")
#         return

#     print("Scraping shuru... Error handling active hai.")

#     for i in range(SCROLL_COUNT):
#         # Current screen ke messages find karein
#         messages = driver.find_elements(By.CSS_SELECTOR, ".copyable-text")
        
#         for msg in messages:
#             try:
#                 text = msg.text.strip()
#                 if text and len(text) > 15: # Sirf kaam ka content uthane ke liye
#                     unique_messages.add(text)
#             except StaleElementReferenceException:
#                 # Agar element purana ho jaye to usay skip kar dein, agle loop mein cover ho jayega
#                 continue
#             except Exception:
#                 continue

#         # Upar ki taraf scroll karein
#         # Keys.CONTROL + Keys.HOME se behtar hai 'PageUp' use karna multiple times
#         chat_window.send_keys(Keys.PAGE_UP)
#         time.sleep(SCROLL_PAUSE_TIME)
        
#         print(f"Scroll {i+1}/{SCROLL_COUNT} | Unique Posts: {len(unique_messages)}")

#     # Save to File
#     save_data(unique_messages)

# def save_data(data):
#     try:
#         folder = os.path.dirname(FILE_PATH)
#         if folder and not os.path.exists(folder):
#             os.makedirs(folder)

#         with open(FILE_PATH, "w", encoding="utf-8") as f:
#             for post in data:
#                 f.write(post + "\n" + "-"*30 + "\n")
        
#         print(f"\nMubarak ho! {len(data)} posts save ho gayi hain.")
#         print(f"File Path: {FILE_PATH}")
#     except Exception as e:
#         print(f"File save karne mein masla aya: {e}")

# scrape_channel_with_scroll()
# driver.quit()

#good version with scrolling 
# import time
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# # --- CONFIGURATION ---
# FILE_PATH = r"E:\My-Workstation\Coding\Web Scraping\whatsapp channel/urdu_novel_posts.txt" 
# SCROLL_COUNT = 20  # Kitni baar upar scroll karna hai
# SCROLL_PAUSE_TIME = 2  # Scroll ke baad loading ka intezar (seconds)
# # ---------------------

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://web.whatsapp.com")

# print("Dost! Pehle QR Code scan karein aur phir wo Channel open karein.")
# input("Jab Channel open ho jaye aur messages load ho jayein, to 'Enter' dabayein...")

# def scrape_channel_with_scroll():
#     # Duplicates se bachne ke liye Set use karenge
#     unique_messages = set()
    
#     # WhatsApp ka main message container dhundna
#     # Ye aksar badalta rehta hai, lekin 'main' area ko target karna behtar hai
#     try:
#         # Pura message area select karna
#         chat_window = driver.find_element(By.XPATH, "//div[@role='application']//div[@id='main']//div[contains(@class, '_5-9m')]")
#     except:
#         # Agar specific class na mile to body par scroll try karein
#         chat_window = driver.find_element(By.TAG_NAME, "body")

#     print("Scraping aur Scrolling shuru ho rahi hai...")

#     for i in range(SCROLL_COUNT):
#         # 1. Current screen ke messages nikaalna
#         messages = driver.find_elements(By.CSS_SELECTOR, ".copyable-text")
#         for msg in messages:
#             text = msg.text.strip()
#             if text and len(text) > 10: # Choti moti info (like time) filter karne ke liye
#                 unique_messages.add(text)

#         # 2. Upar ki taraf scroll karna
#         # Hum 'Home' key ya JS scroll use kar sakte hain
#         driver.execute_script("arguments[0].scrollTop = 0", chat_window) 
#         # Ya phir ye method:
#         chat_window.send_keys(Keys.CONTROL + Keys.HOME)
        
#         print(f"Scroll {i+1}/{SCROLL_COUNT} mukammal... Ab tak {len(unique_messages)} unique posts mili.")
#         time.sleep(SCROLL_PAUSE_TIME)

#     # 4. Save to File
#     try:
#         folder = os.path.dirname(FILE_PATH)
#         if folder and not os.path.exists(folder):
#             os.makedirs(folder)

#         with open(FILE_PATH, "w", encoding="utf-8") as f:
#             for post in unique_messages:
#                 f.write(post + "\n" + "-"*30 + "\n")
        
#         print(f"\nSuccess! Total {len(unique_messages)} unique posts save ho gayi hain.")
#         print(f"Location: {FILE_PATH}")
        
#     except Exception as e:
#         print(f"Error saving file: {e}")

# scrape_channel_with_scroll()
# driver.quit()










# import time
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# # --- CONFIGURATION (Aapka Path) ---
# FILE_PATH = r"E:\My-Workstation\Coding\Web Scraping\whatsapp channel\urdu_novel_posts.txt" 
# # ----------------------------------

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://web.whatsapp.com")

# print("Dost! Pehle QR Code scan karein aur Channel open karein.")
# input("Jab Channel open ho jaye, to 'Enter' dabayein...")

# def scrape_channel():
#     # Wapis wahi purana selector jo aapke paas kaam kar raha tha
#     messages = driver.find_elements(By.CSS_SELECTOR, ".copyable-text")
    
#     content_list = []
#     seen_texts = set() # Ye duplicate posts ko rokne ke liye hai

#     for msg in messages:
#         text = msg.text.strip()
        
#         # Check: Agar text khali nahi hai aur pehle list mein nahi aaya
#         if text and text not in seen_texts:
#             content_list.append(text)
#             seen_texts.add(text) # Is text ko yaad rakho
    
#     # File Save Logic
#     try:
#         folder = os.path.dirname(FILE_PATH)
#         if folder and not os.path.exists(folder):
#             os.makedirs(folder)

#         # "w" se har baar nayi file banegi, "a" se purani mein add hoga
#         with open(FILE_PATH, "w", encoding="utf-8") as f:
#             for line in content_list:
#                 f.write(line + "\n" + "-"*30 + "\n")
        
#         print(f"\nDone! Total {len(content_list)} posts save ho gayi hain.")
#         print(f"File Path: {FILE_PATH}")
        
#     except Exception as e:
#         print(f"Error: {e}")

# scrape_channel()











# import time
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# # --- CONFIGURATION (Aapka hard-coded path) ---
# FILE_PATH = r"E:\My-Workstation\Coding\Web Scraping\whatsapp channel\urdu_novel_posts.txt" 
# # ----------------------------------------------

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://web.whatsapp.com")

# print("Dost! Pehle QR Code scan karein aur Channel open karein.")
# input("Jab Channel open ho jaye, to 'Enter' dabayein...")

# def scrape_channel():
#     # Behtar Selector: Sirf message text ko target karne ke liye
#     messages = driver.find_elements(By.CSS_SELECTOR, "span.selectable-text.copyable-text")
    
#     content_list = []
#     seen_texts = set() # Duplicates ko filter karne ke liye

#     for msg in messages:
#         text = msg.text.strip()
        
#         # Check: Duplicate filter logic
#         if text and text not in seen_texts:
#             content_list.append(text)
#             seen_texts.add(text)
    
#     # File Save Logic
#     try:
#         # Path check: Agar folders nahi bane hue to create karega
#         folder = os.path.dirname(FILE_PATH)
#         if folder and not os.path.exists(folder):
#             os.makedirs(folder)

#         with open(FILE_PATH, "w", encoding="utf-8") as f:
#             for line in content_list:
#                 f.write(line + "\n" + "-"*30 + "\n")
        
#         print(f"\nBehtareen! Total {len(content_list)} unique posts save ho gayi hain.")
#         print(f"File Path: {FILE_PATH}")
        
#     except Exception as e:
#         print(f"Error: Path access karne mein masla aa raha hai. Details: {e}")

# scrape_channel()
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
# driver.quit()

