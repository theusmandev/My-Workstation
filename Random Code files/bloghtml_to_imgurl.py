import pandas as pd
import re
import os

# ===== INPUT / OUTPUT PATHS =====
INPUT_CSV = r"C:\Users\PCS\Downloads\urdunovelbanks_FULL_2025-12 (1).csv"
DOWNLOADS_DIR = r"C:\Users\PCS\Downloads"
OUTPUT_CSV = os.path.join(DOWNLOADS_DIR, "urdunovelbanks_image_urls.csv")

HTML_COLUMN = "Full HTML Content"
# =================================

# CSV read (Excel / Windows safe encoding)
df = pd.read_csv(INPUT_CSV, encoding="cp1252")

# Blogger image URL regex
pattern = re.compile(
    r'https://blogger\.googleusercontent\.com/img[^"\s]+',
    re.IGNORECASE
)

def extract_blogger_image(html):
    if pd.isna(html):
        return ""
    match = pattern.search(str(html))
    return match.group(0) if match else ""

# 4th column add karo
df["Image URL"] = df[HTML_COLUMN].apply(extract_blogger_image)

# CSV save in Downloads folder
df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

print("✅ DONE!")
print(f"📁 Output saved at:\n{OUTPUT_CSV}")
