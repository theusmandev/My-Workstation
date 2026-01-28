import pandas as pd
import os

# Folder path jahan Excel files hain
folder_path = r"D:\workstation\ready"

# Nayi file ka naam aur path (with .xlsx extension)
output_file = r"D:\workstation\readyready.xlsx"

# Saari Excel files ki list banayein
excel_files = [f for f in os.listdir(folder_path) if f.endswith(('.xlsx', '.xls', '.xlsm'))]

# Ek empty DataFrame banayein
merged_data = pd.DataFrame()

# Har Excel file ko read aur merge karein
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    try:
        # Excel file ko read karein
        df = pd.read_excel(file_path, engine='openpyxl')
        merged_data = pd.concat([merged_data, df], ignore_index=True)
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Check if merged_data is empty
if not merged_data.empty:
    # Merged data ko nayi Excel file mein save karein
    merged_data.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Saari Excel files merge ho gayi hain aur {output_file} mein save ho gayi hain!")
else:
    print("No data was merged. Check if the folder contains valid Excel files.")