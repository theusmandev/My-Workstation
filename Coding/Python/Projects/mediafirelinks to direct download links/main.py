
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
from concurrent.futures import ThreadPoolExecutor

# --- SETTINGS ---
INPUT_FILE = r"C:\Users\PCS\Downloads\direct download links.xlsx"
OUTPUT_FILE = r"C:\Users\PCS\Downloads\direct download links_ok.xlsx"
MAX_WORKERS = 8  # Speed barhanay ke liye threads ki tadaad
BATCH_SIZE = 10  # Har 10 links ke baad file save hogi

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_link(url):
    """Mediafire page se direct link nikalne ka kaam"""
    if pd.isna(url) or not str(url).startswith('http'):
        return None
    
    try:
        # Request with timeout taake program stuck na ho
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            btn = soup.find('a', {'id': 'downloadButton'})
            if btn:
                return btn.get('href')
    except Exception as e:
        pass # Error handle silently taake threads chaltay rahen
    return None

def main():
    # 1. Resume Logic: Check karein agar purani progress mojud ha
    if os.path.exists(OUTPUT_FILE):
        print("Pichli file mil gayi ha, wahin se resume kar rahay hain...")
        df = pd.read_excel(OUTPUT_FILE)
    else:
        print("Nayi file tayyar ki ja rahi ha...")
        df = pd.read_excel(INPUT_FILE)
        # Naya column banayen agar nahi ha
        if 'Direct Download Links' not in df.columns:
            df['Direct Download Links'] = None

    # 2. Sirf wo links nikalen jo abhi process nahi huay
    pending_mask = df['Direct Download Links'].isna()
    pending_indices = df[pending_mask].index.tolist()

    if not pending_indices:
        print("Mubarak ho! Tamam 600 links pehle hi mukammal hain.")
        return

    print(f"Total Pending Links: {len(pending_indices)}")
    print(f"Using {MAX_WORKERS} threads for high speed...\n")

    # 3. Processing in Batches
    for i in range(0, len(pending_indices), BATCH_SIZE):
        batch = pending_indices[i : i + BATCH_SIZE]
        urls_to_scrape = [df.at[idx, 'Mediafire Links'] for idx in batch]

        # Multi-threading ka istemal
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            results = list(executor.map(scrape_link, urls_to_scrape))

        # Data update karna
        for idx, result in zip(batch, results):
            if result:
                df.at[idx, 'Direct Download Links'] = result
                print(f"Link {idx+1}: Success")
            else:
                print(f"Link {idx+1}: Failed (Retrying in next run)")

        # Save progress to Excel after every batch
        df.to_excel(OUTPUT_FILE, index=False)
        print(f">>> Progress Saved: {i + len(batch)}/{len(pending_indices)} processed.")
        
        # Thora sa saans lenay den server ko
        time.sleep(0.5)

    print("\n--- Kaam Mukammal! ---")
    print(f"Final file saved as: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()












# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# # 1. Excel file load karen
# input_file = r"C:\Users\PCS\Downloads\upload - Copy - Copy.xlsx"  # Aapki purani file ka naam
# df = pd.read_excel(input_file)

# # Direct links store karnay ke liye list
# direct_links_list = []

# # Headers taake Mediafire ko lagay ke browser se request aa rahi ha
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }

# print(f"Total {len(df)} links process ho rahay hain...")

# # 2. Scraping Loop
# for index, row in df.iterrows():
#     page_url = row['Mediafire Links']
#     try:
#         response = requests.get(page_url, headers=headers, timeout=10)
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Download button se href (direct link) nikalna
#         download_button = soup.find('a', {'id': 'downloadButton'})
        
#         if download_button:
#             d_link = download_button.get('href')
#             direct_links_list.append(d_link)
#             print(f"{index+1}: Link nikal liya gaya.")
#         else:
#             direct_links_list.append("Not Found")
#             print(f"{index+1}: Direct link nahi mila.")
            
#     except Exception as e:
#         direct_links_list.append(f"Error: {str(e)}")
#         print(f"{index+1}: Error aya - {page_url}")

#     # Mediafire ki security se bachnay ke liye thora sa break
#     time.sleep(1)

# # 3. Nayi Excel file save karna
# df['Direct Download Links'] = direct_links_list
# output_file = r"C:\Users\PCS\Downloads\upload.xlsx"
# df.to_excel(output_file, index=False)

# print(f"\nKaam mukammal! Tamam links '{output_file}' ma save kar diye gaye hain.")