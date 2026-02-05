# import pandas as pd

# # Load the filtered Excel file
# excel_input_path = r"D:\workstation\writers\Saira raza_sorted_unique_sorted.xlsx"# Replace with your file path
# try:
#     df = pd.read_excel(excel_input_path)
# except FileNotFoundError:
#     raise FileNotFoundError(f"Excel file not found at: {excel_input_path}")

# # Print columns for debugging
# print("Columns in Excel file:", df.columns.tolist())

# # Rename columns to 'T' ansd 'link' (update 'Name' and 'URL' to match your Excel file)
# df = df.rename(columns={'Name': 'Titles', 'URL': 'Links'})

# # Ensure required columns exist
# if 'Titles' not in df.columns or 'Links' not in df.columns:
#     raise ValueError(f"Excel file must contain 'Titles' and 'Links' columns. Found: {df.columns.tolist()}")

# # Sort DataFrame by title for alphabetical order
# df = df.sort_values(by='Titles', key=lambda x: x.str.lower())

# # Start HTML content (minimal wrapper, as your example is a fragment)
# html_content = ""

# # Add each title and link in the exact provided format with numbering
# for index, row in df.iterrows():
#     Titles = str(row['Titles']).strip() if pd.notna(row['Titles']) else "Untitled"
#     link = str(row['Links']).strip() if pd.notna(row['Links']) else "#"
#     # Handle special note for "Maala"
#     note = " ( still running in episodes )" if Titles.lower() == "maala" else ""
    
#     # Mimic exact HTML structure from your example
#     html_content += f"""<p><i style="color: #1a1a1a; font-family: helvetica; font-size: 13px;"><b>{index + 1}.</b></i></p>
# <div><span face="sans-serif" style="color: #202122;"><span style="font-size: 14px;"><i style="color: #1a1a1a; font-family: helvetica; font-size: 13px;">&nbsp;&nbsp;&nbsp;&nbsp;{Titles}</i></span></span></div>
# <div><span face="sans-serif" style="color: #202122;"><span style="font-size: 14px;"><i style="color: #1a1a1a; font-family: helvetica; font-size: 13px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="{link}" rel="nofollow" target="_blank">👉Download</a>{note}</i></span></span></div>
# """

# # Save the HTML content to a .txt file
# output_txt_path = r"D:\workstation\novel_list.txt"
# try:
#     with open(output_txt_path, 'w', encoding='utf-8') as f:
#         f.write(html_content)
#     print(f"✅ HTML content saved to: {output_txt_path}")
# except Exception as e:
#     print(f"Error writing TXT file: {e}")




import pandas as pd

# Load the filtered Excel file
excel_input_path = r"D:\unb-workstation\writers\digest\khawateen\2025.xlsx"
try:
    df = pd.read_excel(excel_input_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Excel file not found at: {excel_input_path}")

# Print columns for debugging
print("Columns in Excel file:", df.columns.tolist())

# Rename columns to 'Titles' and 'Links' (update 'Name' and 'URL' to match your Excel file)
df = df.rename(columns={'Name': 'Titles', 'URL': 'Links'})

# Ensure required columns exist
if 'Titles' not in df.columns or 'Links' not in df.columns:
    raise ValueError(f"Excel file must contain 'Titles' and 'Links' columns. Found: {df.columns.tolist()}")

# Do not sort the DataFrame to maintain original order
# df = df.sort_values(by='Titles', key=lambda x: x.str.lower())  # Commenting this out

# Start HTML content (minimal wrapper, as your example is a fragment)
html_content = ""

# Add each title and link in the exact provided format with numbering
for index, row in df.iterrows():
    # Extract title and link, handle missing values
    raw_title = str(row['Titles']).strip() if pd.notna(row['Titles']) else "Untitled"
    link = str(row['Links']).strip() if pd.notna(row['Links']) else "#"
    
    # Check if "by" is already in the title
    if " by " in raw_title.lower():
        formatted_title = raw_title.title()  # Use the original title with proper casing
        novel_name = raw_title.split(" by ", 1)[0].strip()  # Extract novel name
    else:
        # Apply title case to the novel name and add "by Nazia Kanwal Nazi" if not present
        novel_name = raw_title.strip()
        formatted_title = f"{novel_name.title()} ."
    
    # Handle special note for "Maala"
    note = " ( still running in episodes )" if novel_name.lower() == "maala" else ""
    
    # Mimic exact HTML structure from your example with proper indentation using  
    html_content += f"""<p><i style="color: #1a1a1a; font-family: helvetica; font-size: 13px;"><b>{index + 1}.</b></i></p>
<div><span face="sans-serif" style="color: #202122;"><span style="font-size: 14px;"><i style="color: #1a1a1a; font-family: helvetica; font-size: 13px;">    {formatted_title}</i></span></span></div>
<div><span face="sans-serif" style="color: #202122;"><span style="font-size: 14px;"><i style="color: #1a1a1a; font-family: helvetica; font-size: 13px;">                <a href="{link}" rel="nofollow" target="_blank">👉Download</a>{note}</i></span></span></div>
"""

# Save the HTML content to a .txt file
output_txt_path = r"D:\unb-workstation\novel_list.txt"
try:
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ HTML content saved to: {output_txt_path}")
except Exception as e:
    print(f"Error writing TXT file: {e}")




