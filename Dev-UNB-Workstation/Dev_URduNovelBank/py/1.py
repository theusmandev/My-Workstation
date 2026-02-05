import pandas as pd

# Load the comments CSV file
input_csv_file = 'comments_data.csv'

# Attempt to read the CSV file
try:
    comments_df = pd.read_csv(input_csv_file)
    print(f"Loaded data with {len(comments_df)} rows from {input_csv_file}.")
    print("Sample data loaded:\n", comments_df.head())
except FileNotFoundError:
    print(f"File {input_csv_file} not found.")
    exit()

# Check if DataFrame is empty
if comments_df.empty:
    print("The input CSV file is empty. No data to process.")
    exit()

# Display column names to verify the correct names are present
print("Columns found in the CSV file:", comments_df.columns)

# Verify the Username column exists
if 'Username' not in comments_df.columns:
    print("The 'Username' column is missing in the CSV file.")
    exit()
else:
    print("Username column found.")

# Sort the DataFrame alphabetically by Username
comments_df = comments_df.sort_values(by='Username')

# Create a new Excel writer
output_excel_file = 'sorted_comments_by_user.xlsx'
with pd.ExcelWriter(output_excel_file) as writer:
    # Group by Username and save each group as a separate sheet
    for username, group in comments_df.groupby('Username'):
        if group.empty:
            print(f"No data found for user: {username}")
            continue
        
        # Replace invalid characters in the sheet name with underscores
        sanitized_username = "".join([c if c.isalnum() else "_" for c in username])
        
        # Write each user's comments to a separate sheet
        try:
            group.to_excel(writer, sheet_name=sanitized_username[:31], index=False)  # Excel sheet names max at 31 characters
            print(f"Added sheet for user: {username} with {len(group)} comments")
        except Exception as e:
            print(f"Error saving sheet for user {username}: {e}")

print(f"Data has been separated by user and saved in {output_excel_file}")

# Check if the file was created
import os
if os.path.exists(output_excel_file):
    print(f"File '{output_excel_file}' saved successfully.")
else:
    print(f"Failed to save file '{output_excel_file}'.")
