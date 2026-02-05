import pandas as pd

# Your hard-coded paths
excel_path = r"D:\unb-workstation\writers\riffat naheed.xlsx"
output_path = r"D:\unb-workstation\writers\riffat_output.txt"

# Read Excel file
df = pd.read_excel(excel_path)

# Normalize and map original columns
cols_map = {c.lower().strip(): c for c in df.columns}

title_col = None
link_col = None

# Auto-detect title column
for c in cols_map:
    if "title" in c:
        title_col = cols_map[c]

# Auto-detect link column
for c in cols_map:
    if "link" in c or "url" in c:
        link_col = cols_map[c]

# If not found
if not title_col or not link_col:
    print("ERROR: Excel file me 'title' aur 'link' columns nahi mile.")
    print("Detected columns:", df.columns.tolist())
    exit()

# Write text file
with open(output_path, "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        title = str(row[title_col]).strip()
        link = str(row[link_col]).strip()

        f.write(f"👉 {title}\n")
        f.write(f"{link}\n\n")

print("Done! Output saved to:", output_path)




# import pandas as pd

# # Your hard-coded paths
# excel_path = r"D:\unb-workstation\writers\riffat naheed.xlsx"
# output_path = r"D:\unb-workstation\writers\riffat_output.txt"

# # Read Excel file
# df = pd.read_excel(excel_path)

# # Normalize and map original columns
# cols_map = {c.lower().strip(): c for c in df.columns}

# title_col = None
# link_col = None

# # Auto-detect title column
# for c in cols_map:
#     if "title" in c:
#         title_col = cols_map[c]

# # Auto-detect link column
# for c in cols_map:
#     if "link" in c or "url" in c:
#         link_col = cols_map[c]

# # If not found, show error
# if not title_col or not link_col:
#     print("ERROR: Excel file me 'title' aur 'link' columns nahi mile.")
#     print("Detected columns:", df.columns.tolist())
#     exit()

# # Write text file
# with open(output_path, "w", encoding="utf-8") as f:
#     for _, row in df.iterrows():
#         f.write(str(row[title_col]).strip() + "\n")
#         f.write(str(row[link_col]).strip() + "\n\n")

# print("Done! Output saved to:", output_path)










# import pandas as pd

# # ---- Hard-code your paths here ----
# excel_path = r"D:\unb-workstation\writers\riffat naheed.xlsx"     # <-- change this
# output_path = r"D:\unb-workstation\writers\riffat_output.txt"       # <-- change this
# # ------------------------------------

# df = pd.read_excel(excel_path)

# # Normalize column names to lowercase
# df.columns = df.columns.str.lower()

# with open(output_path, "w", encoding="utf-8") as f:
#     for _, row in df.iterrows():
#         f.write(str(row["title"]).strip() + "\n")
#         f.write(str(row["link"]).strip() + "\n\n")

# print("Done! Text file created:", output_path)
