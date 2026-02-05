# import pandas as pd
# import requests
# from requests.exceptions import RequestException
# import time

# # Excel file ka path
# excel_file = r"C:\Users\PCS\Desktop\Book2.xlsx"
# sheet_name = 'Sheet1'

# # Dataframe mein Excel file load karo
# df = pd.read_excel(excel_file, sheet_name=sheet_name)

# # Link ka column naam
# link_column = 'Links'

# # Naya column banayein broken/working status ke liye
# df['Status'] = ''

# # Har link ko check karne ka function
# def check_link(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
#     try:
#         response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
#         # Debug: Print final URL and first 200 chars of response
#         print(f"URL: {response.url}")
#         print(f"Response (first 200 chars): {response.text[:200]}")
#         # Check for CAPTCHA/security page
#         if 'Just a moment' in response.text:
#             return 'Blocked by CAPTCHA (Manual Check Needed)'
#         # Check for broken link indicators
#         if 'error.php' in response.url or 'Something appears to be missing' in response.text:
#             return 'Broken'
#         # Check for working link (valid MediaFire page with download hint)
#         if response.status_code == 200 and 'mediafire.com' in response.url and 'download' in response.text.lower():
#             return 'Working'
#         else:
#             return 'Broken'
#     except RequestException:
#         return 'Error Connecting'

# # Har link ko check karein
# for index, row in df.iterrows():
#     url = row[link_column]
#     if 'mediafire.com' in url.lower():
#         status = check_link(url)
#         df.at[index, 'Status'] = status
#         time.sleep(2)  # Small delay to avoid rate limiting
#     else:
#         df.at[index, 'Status'] = 'Not a MediaFire Link'

# # Updated data ko nai Excel file mein save karein
# output_file = r"C:\Users\PCS\Downloads\checklinks.xlsx"
# df.to_excel(output_file, index=False)
# print(f"Results saved to {output_file}")









# import pandas as pd
# import requests
# from requests.exceptions import RequestException
# import time

# # Excel file ka path
# excel_file = r"D:\workstation\smarturdunovelbanmediafire.xlsx"
# sheet_name = 'Sheet1'

# # Dataframe mein Excel file load karo
# df = pd.read_excel(excel_file, sheet_name=sheet_name)

# # Link ka column naam
# link_column = 'Links'

# # Naya column banayein broken/working status ke liye
# df['Status'] = ''

# # Har link ko check karne ka function
# def check_link(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
#     try:
#         response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
#         # Debug: Print final URL and first 200 chars of response
#         print(f"URL: {response.url}")
#         print(f"Response (first 200 chars): {response.text[:200]}")
#         # Check for CAPTCHA/security page
#         if 'Just a moment' in response.text:
#             print("Note: This link requires manual CAPTCHA verification in a browser.")
#             return 'Blocked by CAPTCHA (Manual Check Needed)'
#         # Check for broken link indicators
#         if 'error.php' in response.url:
#             return 'Broken'
#         # Check for working link (valid MediaFire page with download hint)
#         if response.status_code == 200 and 'mediafire.com' in response.url and 'download' in response.text.lower():
#             return 'Working'
#         else:
#             return 'Broken'
#     except RequestException:
#         return 'Error Connecting'

# # Har link ko check karein
# for index, row in df.iterrows():
#     url = row[link_column]
#     if 'mediafire.com' in url.lower():
#         status = check_link(url)
#         df.at[index, 'Status'] = status
#         time.sleep(2)  # Small delay to avoid rate limiting
#     else:
#         df.at[index, 'Status'] = 'Not a MediaFire Link'

# # Updated data ko nai Excel file mein save karein
# output_file = r"C:\Users\PCS\Downloads\checklinks.xlsx"
# df.to_excel(output_file, index=False)
# print(f"Results saved to {output_file}")









import pandas as pd
import requests
from requests.exceptions import RequestException
import time

# Excel file ka path
excel_file = r"D:\workstation\smarturdunovelbanmediafire.xlsx"
sheet_name = 'Sheet1'

# Dataframe mein Excel file load karo
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Link ka column naam
link_column = 'Links'

# Naya column banayein broken/working status ke liye
df['Status'] = ''

# Output file ka path
output_file = r"C:\Users\PCS\Downloads\checklinks.xlsx"

# Har link ko check karne ka function
def check_link(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        # Debug: Print final URL and first 200 chars of response
        print(f"URL: {response.url}")
        print(f"Response (first 200 chars): {response.text[:200]}")
        # Check for CAPTCHA/security page
        if 'Just a moment' in response.text:
            print("Note: This link requires manual CAPTCHA verification in a browser.")
            return 'Blocked by CAPTCHA (Manual Check Needed)'
        # Check for broken link indicators
        if 'error.php' in response.url:
            return 'Broken'
        # Check for working link (valid MediaFire page with download hint)
        if response.status_code == 200 and 'mediafire.com' in response.url and 'download' in response.text.lower():
            return 'Working'
        else:
            return 'Broken'
    except RequestException:
        return 'Error Connecting'

# Counter to track processed links
counter = 0

# Har link ko check karein
for index, row in df.iterrows():
    url = row[link_column]
    if 'mediafire.com' in url.lower():
        status = check_link(url)
        df.at[index, 'Status'] = status
        time.sleep(2)  # Small delay to avoid rate limiting
    else:
        df.at[index, 'Status'] = 'Not a MediaFire Link'
    
    counter += 1
    # Har 50 links ke baad status save karo
    if counter % 50 == 0:
        df.to_excel(output_file, index=False)
        print(f"Saved status for {counter} links to {output_file}")

# Final save to ensure all data is written
df.to_excel(output_file, index=False)
print(f"Final results saved to {output_file}")