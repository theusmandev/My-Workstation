# Code to clean digest excel removing unwanted words and also sort 

import pandas as pd
import os
import re

# Input file path
input_file = r"D:\unb-workstation\writers\digest\Shua.xlsx"

# Read Excel
df = pd.read_excel(input_file)

# List of unwanted keywords (case-insensitive)
unwanted_keywords = [
    "complete", "download", "pdf", "free", "read", "onine", "online"
]

def clean_title(title):
    title = str(title).lower()
    
    # remove anything inside brackets e.g. ( ... )
    title = re.sub(r"\(.*?\)", "", title)
    
    # remove unwanted keywords
    for word in unwanted_keywords:
        title = re.sub(rf"\b{word}\b", "", title, flags=re.IGNORECASE)
    
    # remove extra spaces
    title = re.sub(r"\s+", " ", title).strip()
    
    # match pattern: Shua digest + Month + Year
    match = re.search(r"(shua digest)\s+([a-zA-Z]+)\s+(\d{4})", title, re.IGNORECASE)
    if match:
        return f"{match.group(1).title()} {match.group(2).capitalize()} {match.group(3)}"
    
    return title.strip().title()

# Apply cleaning on Titles column
df['Titles'] = df['Titles'].apply(clean_title)

# Sort by Titles alphabetically
df_sorted = df.sort_values(by='Titles', ascending=True)

# Save cleaned and sorted file
file_name = os.path.splitext(os.path.basename(input_file))[0]
output_file = os.path.join(os.path.dirname(input_file), f"{file_name}_cleaned_sorted.xlsx")
df_sorted.to_excel(output_file, index=False)

print(f"✅ Cleaned (keywords + brackets removed) and sorted file saved as {output_file}")



