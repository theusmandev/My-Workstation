import pandas as pd
import re

# ====== INPUT / OUTPUT FILE ======
INPUT_CSV = r"C:\Users\PCS\Downloads\urdunovelbanks_FULL_2025-12 (1).csv"   # apni csv file ka naam
OUTPUT_CSV = r"C:\Users\PCS\Downloads\urdunook"   # nayi csv file
HTML_COLUMN = "Full HTML Content"  # exact column name
# =================================

# CSV load karo
df = pd.read_csv(INPUT_CSV)

# Blogger image URL regex
pattern = re.compile(
    r'https://blogger\.googleusercontent\.com/img[^"\s]+',
    re.IGNORECASE
)

def extract_blogger_image(html):
    if pd.isna(html):
        return ""
    match = pattern.search(html)
    return match.group(0) if match else ""

# 4th column add karo
df["Image URL"] = df[HTML_COLUMN].apply(extract_blogger_image)

# CSV save karo
df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

print("✅ Done! Blogger image URLs extract ho gaye.")
print(f"📁 Output file: {OUTPUT_CSV}")
