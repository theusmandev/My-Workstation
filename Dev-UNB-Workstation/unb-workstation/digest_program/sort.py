# import pandas as pd
# from datetime import datetime

# # Define input and output paths
# input_path = r"D:\workstation\writers\digest\Khawateen.xlsx"
# output_path = r"D:\workstation\writers\digest\sorted_Khawateen.xlsx"

# # Read the Excel file
# df = pd.read_excel(input_path)

# # Function to extract year and month from the title
# def extract_date(title):
#     # Split the title and get the last two parts (month and year)
#     parts = title.split()
#     month = parts[-2]  # Second-to-last part is the month
#     year = parts[-1]   # Last part is the year
#     # Convert month name to month number for sorting
#     return datetime.strptime(f"{month} {year}", "%B %Y")

# # Add a new column for sorting by date
# df['SortDate'] = df['Titles'].apply(extract_date)

# # Sort the dataframe by the SortDate column
# df_sorted = df.sort_values(by='SortDate')

# # Drop the temporary SortDate column
# df_sorted = df_sorted.drop(columns=['SortDate'])

# # Save the sorted dataframe to the output path
# df_sorted.to_excel(output_path, index=False)

# print(f"Data has been sorted and saved to '{output_path}'")






#he error occurs because the month "February" is misspelled as "Feburay" in one of the titles (e.g., "Khawateen Digest Feburay 2012"), causing datetime.strptime to fail when trying to parse it with the format %B %Y (which expects the full month name, like "February"). To handle this, we can modify the script to correct common misspellings







# import pandas as pd
# from datetime import datetime

# # Define input and output paths
# input_path = r"D:\workstation\writers\digest\Khawateen.xlsx"
# output_path = r"D:\workstation\writers\digest\sorted_Khawateen.xlsx"

# # Read the Excel file
# df = pd.read_excel(input_path)

# # Function to correct common month misspellings
# def correct_month(month):
#     corrections = {
#         'Feburay': 'February',
#         'Januray': 'January',  # Add more corrections if needed
#         'Februray': 'February',
#         'Feburary': 'February'
#     }
#     return corrections.get(month, month)  # Return corrected month or original if no correction needed

# # Function to extract year and month from the title
# def extract_date(title):
#     # Split the title and get the last two parts (month and year)
#     parts = title.split()
#     month = parts[-2]  # Second-to-last part is the month
#     year = parts[-1]   # Last part is the year
#     # Correct any misspelled month
#     month = correct_month(month)
#     # Convert month name to month number for sorting
#     return datetime.strptime(f"{month} {year}", "%B %Y")

# # Add a new column for sorting by date
# df['SortDate'] = df['Titles'].apply(extract_date)

# # Sort the dataframe by the SortDate column
# df_sorted = df.sort_values(by='SortDate')

# # Drop the temporary SortDate column
# df_sorted = df_sorted.drop(columns=['SortDate'])

# # Save the sorted dataframe to the output path
# df_sorted.to_excel(output_path, index=False)

# print(f"Data has been sorted and saved to '{output_path}'")
















#The error indicates that one of the titles in your Excel file, specifically "Khawateen Digest September," is missing the year, causing the datetime.strptime function to fail when trying to parse it with the format "%B %Y". To fix this, we need to handle cases where the year is missing or the title format is inconsistent. Below is an updated Python script that:


import pandas as pd
from datetime import datetime

# Define input and output paths
input_path = r"D:\unb-workstation\writers\digest\kiran.xlsx"
output_path = r"D:\unb-workstation\writers\digest\kiran_sorted by time.xlsx"

# Read the Excel file
df = pd.read_excel(input_path)

# Function to correct common month misspellings
def correct_month(month):
    corrections = {
        'Feburay': 'February',
        'Januray': 'January',
        'Februray': 'February',
        'Feburary': 'February'
    }
    return corrections.get(month, month)  # Return corrected month or original if no correction needed

# Function to extract year and month from the title
def extract_date(title):
    try:
        # Split the title and get the last parts
        parts = title.split()
        if len(parts) < 3:  # Check if title is too short (e.g., missing year)
            print(f"Warning: Invalid title format '{title}' - missing year. Skipping for sorting.")
            return None  # Return None for invalid titles
        month = parts[-2]  # Second-to-last part is the month
        year = parts[-1]   # Last part is the year
        # Correct any misspelled month
        month = correct_month(month)
        # Ensure year is numeric
        if not year.isdigit():
            print(f"Warning: Invalid year in '{title}'. Skipping for sorting.")
            return None
        # Convert month name to month number for sorting
        return datetime.strptime(f"{month} {year}", "%B %Y")
    except ValueError as e:
        print(f"Error parsing title '{title}': {e}. Skipping for sorting.")
        return None

# Add a new column for sorting by date
df['SortDate'] = df['Titles'].apply(extract_date)

# Log titles that couldn't be parsed
invalid_titles = df[df['SortDate'].isna()]
if not invalid_titles.empty:
    print("\nThe following titles could not be parsed and will be placed at the end:")
    print(invalid_titles[['Titles', 'Links']])

# Sort the dataframe by SortDate, placing None values (invalid dates) at the end
df_sorted = df.sort_values(by='SortDate', na_position='last')

# Drop the temporary SortDate column
df_sorted = df_sorted.drop(columns=['SortDate'])

# Save the sorted dataframe to the output path
df_sorted.to_excel(output_path, index=False)

print(f"\nData has been sorted and saved to '{output_path}'")