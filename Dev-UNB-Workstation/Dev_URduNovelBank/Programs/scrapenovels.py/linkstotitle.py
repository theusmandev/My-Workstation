# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

# # Google Drive links list (Replace with your actual links)
# drive_links = [
#    "https://drive.google.com/file/d/1vjnrr3oEejO0aWmAU-MF34wv1rJ_kkq8/view?usp=drivesdk" 
# ]

# def get_drive_title(url):
#     """Fetch the title of a Google Drive link"""
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             title_tag = soup.find("title")
#             return title_tag.text if title_tag else "Title not found"
#         else:
#             return f"Failed ({response.status_code})"
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Extract titles
# data = [{"Google Drive Link": link, "Title": get_drive_title(link)} for link in drive_links]

# # Convert to DataFrame
# df = pd.DataFrame(data)

# # Save to Excel
# output_file = "google_drive_titles.xlsx"
# df.to_excel(output_file, index=False)

# print(f"Titles saved successfully in {output_file}")









# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# from concurrent.futures import ThreadPoolExecutor
# import time
# from urllib.parse import urlparse
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Configuration
# INPUT_FILE = r"C:\Users\Latitude\Downloads\DigestLibrarydotcom"
# OUTPUT_FILE = r"C:\Users\Latitude\Downloads\DigestLibrarydotcom\google_drive_titles.xlsx"
# TIMEOUT = 10  # seconds
# MAX_WORKERS = 5  # number of concurrent requests

# def is_valid_drive_url(url):
#     """Validate if URL is a Google Drive link"""
#     try:
#         parsed = urlparse(url)
#         return parsed.netloc in ['drive.google.com', 'docs.google.com'] and parsed.scheme in ['http', 'https']
#     except:
#         return False

# def get_drive_title(url):
#     """Fetch the title of a Google Drive link with improved error handling"""
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
    
#     try:
#         # Validate URL first
#         if not is_valid_drive_url(url):
#             return "Invalid Google Drive URL"

#         # Add timeout and headers to request
#         response = requests.get(url, headers=headers, timeout=TIMEOUT)
#         response.raise_for_status()  # Raise exception for bad status codes
        
#         soup = BeautifulSoup(response.text, 'html.parser')
#         title_tag = soup.find("title")
        
#         if title_tag and title_tag.text.strip():
#             return title_tag.text.strip()
#         return "Title not found"
        
#     except requests.Timeout:
#         return "Error: Request timed out"
#     except requests.RequestException as e:
#         return f"Error: HTTP {str(e)}"
#     except Exception as e:
#         return f"Error: {str(e)}"

# def process_links():
#     """Main function to process Excel file and fetch titles"""
#     try:
#         # Start timing
#         start_time = time.time()
        
#         # Load Excel file
#         logging.info(f"Loading input file: {INPUT_FILE}")
#         df = pd.read_excel(INPUT_FILE)
        
#         # Validate column
#         if "Links" not in df.columns:
#             raise ValueError("Excel file must have a column named 'Links'")
        
#         # Clean and validate URLs
#         df['Links'] = df['Links'].astype(str).str.strip()
        
#         # Use ThreadPoolExecutor for parallel processing
#         logging.info(f"Fetching titles for {len(df)} links...")
#         with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
#             df["Title"] = list(executor.map(get_drive_title, df["Links"]))
        
#         # Add timestamp column
#         df["Processed_Date"] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        
#         # Save results
#         df.to_excel(OUTPUT_FILE, index=False)
        
#         # Log completion
#         execution_time = time.time() - start_time
#         logging.info(f"Titles saved successfully in {OUTPUT_FILE}")
#         logging.info(f"Processed {len(df)} links in {execution_time:.2f} seconds")
        
#         return True
        
#     except FileNotFoundError:
#         logging.error(f"Input file not found: {INPUT_FILE}")
#         return False
#     except Exception as e:
#         logging.error(f"Processing failed: {str(e)}")
#         return False

# if __name__ == "__main__":
#     success = process_links()
#     if not success:
#         print("Processing failed. Check logs for details.")








# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# from concurrent.futures import ThreadPoolExecutor
# import time
# from urllib.parse import urlparse
# import logging
# import os

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Configuration
# INPUT_FILE = r"E:\UNB\Programs\scrapenovels.py\Novels excel files\DigestLibrarydotcom_ok\merged_output.xlsx"
# OUTPUT_FILE = r"E:\UNB\Programs\scrapenovels.py\Novels excel files\DigestLibrarydotcom_ok\merged_outphhhhhhut.xlsx"
# TIMEOUT = 10
# MAX_WORKERS = 5

# # Create output directory if it doesn't exist
# output_dir = os.path.dirname(OUTPUT_FILE)
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir, exist_ok=True)

# def is_valid_drive_url(url):
#     """Validate if URL is a Google Drive link"""
#     try:
#         parsed = urlparse(url)
#         return parsed.netloc in ['drive.google.com', 'docs.google.com'] and parsed.scheme in ['http', 'https']
#     except:
#         return False

# def get_drive_title(url):
#     """Fetch the title of a Google Drive link"""
#     headers = {'User-Agent': 'Mozilla/5.0'}
#     try:
#         if not is_valid_drive_url(url):
#             return "Invalid Google Drive URL"
#         response = requests.get(url, headers=headers, timeout=TIMEOUT)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, 'html.parser')
#         title_tag = soup.find("title")
#         return title_tag.text.strip() if title_tag and title_tag.text.strip() else "Title not found"
#     except requests.Timeout:
#         return "Error: Request timed out"
#     except requests.RequestException as e:
#         return f"Error: HTTP {str(e)}"
#     except Exception as e:
#         return f"Error: {str(e)}"

# def process_links():
#     """Main function to process Excel file and fetch titles"""
#     try:
#         start_time = time.time()
        
#         if not os.path.isfile(INPUT_FILE):
#             raise FileNotFoundError(f"Input file does not exist: {INPUT_FILE}")
            
#         logging.info(f"Loading input file: {INPUT_FILE}")
#         df = pd.read_excel(INPUT_FILE)
        
#         if "Links" not in df.columns:
#             raise ValueError("Excel file must have a column named 'Links'")
        
#         df['Links'] = df['Links'].astype(str).str.strip()
        
#         logging.info(f"Fetching titles for {len(df)} links...")
#         with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
#             df["Title"] = list(executor.map(get_drive_title, df["Links"]))
        
#         df["Processed_Date"] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
#         df.to_excel(OUTPUT_FILE, index=False)
        
#         execution_time = time.time() - start_time
#         logging.info(f"Titles saved successfully in {OUTPUT_FILE}")
#         logging.info(f"Processed {len(df)} links in {execution_time:.2f} seconds")
#         return True
        
#     except Exception as e:
#         logging.error(f"Processing failed: {str(e)}")
#         return False

# if __name__ == "__main__":
#     success = process_links()
#     if not success:
#         print("Processing failed. Check logs for details.")











# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# from concurrent.futures import ThreadPoolExecutor
# import time
# from urllib.parse import urlparse
# import logging
# import os

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Configuration
# INPUT_FILE = r"E:\UNB\Programs\scrapenovels.py\Novels excel files\DigestLibrarydotcom_ok\merged_output.xlsx"
# OUTPUT_FILE = r"E:\UNB\Programs\scrapenovels.py\Novels excel files\DigestLibrarydotcom_ok\merged_outphhhhhhut.xlsx"
# TIMEOUT = 10
# MAX_WORKERS = 20  # Increased for better performance
# BATCH_SIZE = 1000  # Process in batches of 1000

# # Create output directory if it doesn't exist
# output_dir = os.path.dirname(OUTPUT_FILE)
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir, exist_ok=True)

# def is_valid_drive_url(url):
#     """Validate if URL is a Google Drive link"""
#     try:
#         parsed = urlparse(url)
#         return parsed.netloc in ['drive.google.com', 'docs.google.com'] and parsed.scheme in ['http', 'https']
#     except:
#         return False

# def get_drive_title(url, index=None):
#     """Fetch the title of a Google Drive link"""
#     headers = {'User-Agent': 'Mozilla/5.0'}
#     try:
#         if index and index % 100 == 0:
#             logging.info(f"Processed {index} links")
            
#         if not is_valid_drive_url(url):
#             return "Invalid Google Drive URL"
        
#         time.sleep(0.5)  # Add delay to avoid rate limiting
#         response = requests.get(url, headers=headers, timeout=TIMEOUT)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, 'html.parser')
#         title_tag = soup.find("title")
#         return title_tag.text.strip() if title_tag and title_tag.text.strip() else "Title not found"
#     except requests.Timeout:
#         return "Error: Request timed out"
#     except requests.RequestException as e:
#         return f"Error: HTTP {str(e)}"
#     except Exception as e:
#         return f"Error: {str(e)}"

# def process_links():
#     """Main function to process Excel file and fetch titles"""
#     try:
#         overall_start = time.time()
        
#         if not os.path.isfile(INPUT_FILE):
#             raise FileNotFoundError(f"Input file does not exist: {INPUT_FILE}")
            
#         logging.info(f"Loading input file: {INPUT_FILE}")
#         df = pd.read_excel(INPUT_FILE)
        
#         if "Links" not in df.columns:
#             raise ValueError("Excel file must have a column named 'Links'")
        
#         df['Links'] = df['Links'].astype(str).str.strip()
#         total_links = len(df)
#         total_batches = (total_links + BATCH_SIZE - 1) // BATCH_SIZE
        
#         for batch in range(total_batches):
#             batch_start = time.time()
#             start_idx = batch * BATCH_SIZE
#             end_idx = min((batch + 1) * BATCH_SIZE, total_links)
#             batch_df = df.iloc[start_idx:end_idx].copy()
            
#             logging.info(f"Processing batch {batch + 1}/{total_batches} ({end_idx-start_idx} links)...")
            
#             with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
#                 batch_df["Title"] = list(executor.map(
#                     lambda x: get_drive_title(x[1], x[0] + start_idx), 
#                     enumerate(batch_df["Links"])
#                 ))
            
#             # Save intermediate results
#             batch_df.to_excel(f"{OUTPUT_FILE[:-5]}_batch{batch}.xlsx", index=False)
            
#             # Calculate and log time remaining
#             batch_time = time.time() - batch_start
#             remaining_batches = total_batches - (batch + 1)
#             est_time_remaining = batch_time * remaining_batches
#             logging.info(f"Batch {batch + 1} completed in {batch_time:.2f}s. "
#                         f"Estimated time remaining: {est_time_remaining/60:.2f} minutes")
        
#         # Combine all batches
#         logging.info("Combining batches...")
#         final_df = pd.concat([pd.read_excel(f"{OUTPUT_FILE[:-5]}_batch{i}.xlsx") 
#                             for i in range(total_batches)])
#         final_df["Processed_Date"] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
#         final_df.to_excel(OUTPUT_FILE, index=False)
        
#         # Clean up temporary files
#         for i in range(total_batches):
#             os.remove(f"{OUTPUT_FILE[:-5]}_batch{i}.xlsx")
            
#         total_time = time.time() - overall_start
#         logging.info(f"Processed {total_links} links in {total_time/60:.2f} minutes")
#         return True
        
#     except Exception as e:
#         logging.error(f"Processing failed: {str(e)}")
#         return False

# if __name__ == "__main__":
#     success = process_links()
#     if not success:
#         print("Processing failed. Check logs for details.")

import requests
import pandas as pd
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time
from urllib.parse import urlparse
import logging
import os
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration
INPUT_FILE = r"E:\UNB\Programs\scrapenovels.py\Novels excel files\DigestLibrarydotcom_ok\Blogger_Novels.xlsx"
OUTPUT_FILE = r"E:\UNB\Programs\scrapenovels.py\Novels excel files\DigestLibrarydotcom_ok\Blogger_Novelsok.xlsx"
TIMEOUT = 20  # Increased timeout to 20 seconds
MAX_WORKERS = 5  # Reduced to avoid rate limiting
BATCH_SIZE = 500
INITIAL_DELAY = 2  # Increased delay to 2 seconds
MAX_RETRIES = 3
PAUSE_ON_RATE_LIMIT = 60  # Pause for 60 seconds if rate limit is detected

# Create output directory if it doesn't exist
output_dir = os.path.dirname(OUTPUT_FILE)
if not os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)

# Set up requests session with retry mechanism
session = requests.Session()
retries = Retry(total=MAX_RETRIES, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

def is_valid_drive_url(url):
    """Validate if URL is a Google Drive link"""
    try:
        parsed = urlparse(url)
        return parsed.netloc in ['drive.google.com', 'docs.google.com'] and parsed.scheme in ['http', 'https']
    except:
        return False

def get_drive_title(url, index=None):
    """Fetch the title of a Google Drive link with retry mechanism"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        if index and index % 100 == 0:
            logging.info(f"Processed {index} links")
            
        if not is_valid_drive_url(url):
            return "Invalid Google Drive URL"
        
        # Random delay to avoid rate limiting
        time.sleep(INITIAL_DELAY + random.uniform(0, 1))
        
        response = session.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()

        # Check for Google's "sorry" page (indicating rate limiting or CAPTCHA)
        if "sorry/index" in response.url:
            logging.warning(f"Rate limit or CAPTCHA detected for {url}. Pausing for {PAUSE_ON_RATE_LIMIT} seconds...")
            time.sleep(PAUSE_ON_RATE_LIMIT)
            return "Error: Rate limit or CAPTCHA detected"

        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find("title")
        return title_tag.text.strip() if title_tag and title_tag.text.strip() else "Title not found"
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            logging.warning(f"Rate limit hit for {url}. Pausing for {PAUSE_ON_RATE_LIMIT} seconds...")
            time.sleep(PAUSE_ON_RATE_LIMIT)
            return "Error: HTTP 429 - Too Many Requests"
        return f"Error: HTTP {str(e)}"
    except requests.Timeout:
        logging.warning(f"Timeout occurred for {url}. Retrying after a pause...")
        time.sleep(PAUSE_ON_RATE_LIMIT // 2)  # Pause for 30 seconds before retrying
        return "Error: Request timed out"
    except requests.RequestException as e:
        return f"Error: HTTP {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def process_links():
    """Main function to process Excel file and fetch titles"""
    try:
        overall_start = time.time()
        
        if not os.path.isfile(INPUT_FILE):
            raise FileNotFoundError(f"Input file does not exist: {INPUT_FILE}")
            
        logging.info(f"Loading input file: {INPUT_FILE}")
        df = pd.read_excel(INPUT_FILE)
        
        if "Links" not in df.columns:
            raise ValueError("Excel file must have a column named 'Links'")
        
        df['Links'] = df['Links'].astype(str).str.strip()
        total_links = len(df)
        total_batches = (total_links + BATCH_SIZE - 1) // BATCH_SIZE
        
        for batch in range(total_batches):
            batch_start = time.time()
            start_idx = batch * BATCH_SIZE
            end_idx = min((batch + 1) * BATCH_SIZE, total_links)
            batch_df = df.iloc[start_idx:end_idx].copy()
            
            logging.info(f"Processing batch {batch + 1}/{total_batches} ({end_idx-start_idx} links)...")
            
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                batch_df["Title"] = list(executor.map(
                    lambda x: get_drive_title(x[1], x[0] + start_idx), 
                    enumerate(batch_df["Links"])
                ))
            
            # Save intermediate results
            batch_df.to_excel(f"{OUTPUT_FILE[:-5]}_batch{batch}.xlsx", index=False)
            
            # Calculate and log time remaining
            batch_time = time.time() - batch_start
            remaining_batches = total_batches - (batch + 1)
            est_time_remaining = batch_time * remaining_batches
            logging.info(f"Batch {batch + 1} completed in {batch_time:.2f}s. "
                        f"Estimated time remaining: {est_time_remaining/60:.2f} minutes")
        
        # Combine all batches
        logging.info("Combining batches...")
        final_df = pd.concat([pd.read_excel(f"{OUTPUT_FILE[:-5]}_batch{i}.xlsx") 
                            for i in range(total_batches)])
        final_df["Processed_Date"] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        final_df.to_excel(OUTPUT_FILE, index=False)
        
        # Clean up temporary files
        for i in range(total_batches):
            os.remove(f"{OUTPUT_FILE[:-5]}_batch{i}.xlsx")
            
        total_time = time.time() - overall_start
        logging.info(f"Processed {total_links} links in {total_time/60:.2f} minutes")
        return True
        
    except Exception as e:
        logging.error(f"Processing failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = process_links()
    if not success:
        print("Processing failed. Check logs for details.")