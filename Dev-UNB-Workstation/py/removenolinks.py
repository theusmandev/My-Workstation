import pandas as pd

# Read the Excel file
input_file = r"C:\Users\PCS\Downloads\urdunovelbanks\Blogger_Novels.xlsx"
df = pd.read_excel(input_file)

# Print column names to debug
print("Column names in the Excel file:", df.columns.tolist())

# Replace 'Links' with the actual column name from the printed output
# For example, if the column is named 'Link' or 'links', update it below
df_cleaned = df[df['Links'].notna() & (df['Links'] != '')]

# Save the cleaned data to a new Excel file
output_file = r"C:\Users\PCS\Downloads\urdunovelbanks\Blogger_Novelsok.xlsx"
df_cleaned.to_excel(output_file, index=False)

print(f"Rows with empty links removed. New file saved as {output_file}")