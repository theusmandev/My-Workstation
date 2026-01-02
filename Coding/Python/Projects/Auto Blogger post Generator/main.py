import pandas as pd
import re

# ===== LOAD EXCEL =====
excel_input_path = r"D:\unb-workstation\writers\deeba tabassum.xlsx"
df = pd.read_excel(excel_input_path)

# Rename columns
df = df.rename(columns={'Titles': 'title', 'Links': 'link'})

# Validate columns
if not {'title', 'link'}.issubset(df.columns):
    raise ValueError("Excel must contain 'Name' and 'URL' columns")

# ===== SEO CLEAN FUNCTION =====
def clean_title(title):
    title = str(title).strip()
    title = re.sub(r'\s+', ' ', title)
    title = title.replace("Pdf", "").replace("PDF", "")
    return title

writer_name = "Deeba Tabassum"

html = []
html.append(f"<h1>{writer_name} Urdu Novels – Complete PDF List</h1>")
html.append(
    f"<p>Read and download all famous Urdu novels by <strong>{writer_name}</strong>. "
    "This post contains complete PDF novels with direct download links.</p>"
)

html.append("<ul class='novel-list'>")

for _, row in df.iterrows():
    title = clean_title(row['title'])
    link = row['link']

    # Ensure writer name in title
    if writer_name.lower() not in title.lower():
        seo_title = f"{title} by {writer_name}"
    else:
        seo_title = title

    html.append(f"""
<li>
  <h2>{seo_title}</h2>
  <p>
    <a href="{link}" rel="nofollow noopener" target="_blank">
      Download {seo_title} PDF
    </a>
  </p>
</li>
""")

html.append("</ul>")

# ===== SAVE TXT =====
output_txt_path = r"C:\Users\PCS\Downloads\New folder\novel_list_seo.txt"
with open(output_txt_path, "w", encoding="utf-8") as f:
    f.write("\n".join(html))

print("✅ SEO Friendly Blogger TXT file generated successfully")
