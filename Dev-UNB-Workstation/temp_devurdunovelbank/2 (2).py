import pandas as pd

# Load the comments CSV file
input_csv_file = 'comments_data.csv'

# Attempt to read the CSV file
try:
    comments_df = pd.read_csv(input_csv_file)
    print(f"Loaded data with {len(comments_df)} rows from {input_csv_file}.")
except FileNotFoundError:
    print(f"File {input_csv_file} not found.")
    exit()

# Check if DataFrame is empty
if comments_df.empty:
    print("The input CSV file is empty. No data to process.")
    exit()

# Verify the Username column exists
if 'Username' not in comments_df.columns:
    print("The 'Username' column is missing in the CSV file.")
    exit()

# Count the number of comments per user
user_comment_counts = comments_df['Username'].value_counts().reset_index()
user_comment_counts.columns = ['Username', 'CommentCount']

# Sort by CommentCount in descending order
user_comment_counts = user_comment_counts.sort_values(by='CommentCount', ascending=False)

# Save to an Excel file
output_excel_file = 'sorted_comments_by_user_count.xlsx'
user_comment_counts.to_excel(output_excel_file, index=False)

print(f"User comment counts have been saved to {output_excel_file}")
print(user_comment_counts.head())  # Display the top commenters
