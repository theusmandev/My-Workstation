import pandas as pd

# Load the Excel file
input_file = r"D:\workstation\smarturdunovelbank.xlsx" # Replace with your Excel file name
output_file = r"D:\workstation\smarturdunovelbanmediafire.xlsx"  # Name of the new Excel file

# Read the Excel file
df = pd.read_excel(input_file)

# Filter rows where the 'Link' column contains 'mediafire.com'
mediafire_df = df[df['Link'].str.contains("mediafire.com", case=False, na=False)]

# Save the filtered rows to a new Excel file
mediafire_df.to_excel(output_file, index=False)

print(f"Filtered rows saved to {output_file}")