import pandas as pd

# Correct path with .json extension
json_file_path = r"D:\workstation\smarturdunovelbank.json"

# Read the JSON file
df = pd.read_json(json_file_path)

# Correct path with .xlsx extension
excel_file_path = r"D:\workstation\smarturdunovelbankokok.xlsx"

# Convert to Excel using openpyxl engine
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f"Converted '{json_file_path}' to '{excel_file_path}' successfully.")
