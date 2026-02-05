import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_mediafire_title(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.find("title")
        return title_tag.text if title_tag else "No Title Found"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Load Excel file
input_file = r"D:\UNB\Programs\scrapenovels.py\Novels excel files\allurdunovelszone\Blogger_Novels (1).xlsx"  # Replace with your file name
output_file = r"D:\UNB\Programs\scrapenovels.py\Novels excel files\allurdunovelszone\Blogger_Novels (2).xlsx"

df = pd.read_excel(input_file)

# Assuming links are in the first column
df["Title"] = df.iloc[:, 0].apply(get_mediafire_title)

# Save the new Excel file
df.to_excel(output_file, index=False)

print("Extraction completed. Check mediafire_titles.xlsx")
