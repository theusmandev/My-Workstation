import pandas as pd

# Load both Excel files
file1 = r"D:\workstation\writers\Nabila aziz.xlsx"
file2 = r"D:\workstation\writers\Nabeela aziz.xlsx"

# Read the Excel files into DataFrames
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Merge (append) the DataFrames
merged_df = pd.concat([df1, df2], ignore_index=True)

# Save the merged DataFrame to a new Excel file
merged_df.to_excel('merged_file.xlsx', index=False)

print("Files merged successfully into 'merged_file.xlsx'")
