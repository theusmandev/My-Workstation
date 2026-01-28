import pandas as pd

# Load the filtered Excel file
excel_input_path = r"D:\unb-workstation\writers\Munam Malik.xlsx"       # Replace with your file path
try:
    df = pd.read_excel(excel_input_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Excel file not found at: {excel_input_path}")

# Print columns for debugging
print("Columns in Excel file:", df.columns.tolist())

# Rename 'Name' column to 'Titles' (update 'Name' to match your Excel file if needed)
df = df.rename(columns={'Name': 'Titles'})

# Ensure 'Titles' column exists
if 'Titles' not in df.columns:
    raise ValueError(f"Excel file must contain 'Titles' column. Found: {df.columns.tolist()}")

# Start text content
text_content = ""

# Add each title with numbering
for index, row in df.iterrows():
    # Extract title, handle missing values
    raw_title = str(row['Titles']).strip() if pd.notna(row['Titles']) else "Untitled"
    
    # Check if "by" is already in the title
    if " by " in raw_title.lower():
        formatted_title = raw_title.title()  # Use the original title with proper casing
    else:
        # Apply title case and add "by Nabeela Aziz" if not present
        formatted_title = f"{raw_title.title()} by Nabeela Aziz"
    
    # Handle special note for "Maala"
    note = " ( still running in episodes )" if raw_title.lower() == "maala" else ""
    
    # Add numbered title to text content
    text_content += f"{index + 1}. {formatted_title}{note}\n"

# Save the text content to a .txt file
output_txt_path = r"D:\unb-workstation\novel_list.txt"
try:
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(text_content)
    print(f"✅ Text content saved to: {output_txt_path}")
except Exception as e:
    print(f"Error writing TXT file: {e}")