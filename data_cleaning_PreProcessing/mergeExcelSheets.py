import pandas as pd

# Input Excel file path
input_file = r'E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\VirtualUniversityofPakistan_Final_MeritList - Copy.xlsx'

# Output Excel file path (same folder)
output_file = r'E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Combined_Output.xlsx'

# Load the Excel file
xls = pd.ExcelFile(input_file)

# List to hold dataframes from each sheet
df_list = []

# Loop through all sheet names and read each sheet into a dataframe
for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    df_list.append(df)

# Concatenate all dataframes (assuming same headers, it will append rows)
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined dataframe to a new Excel file (in a single sheet)
combined_df.to_excel(output_file, index=False, sheet_name='CombinedSheet')

print(f"Combined data saved to {output_file}")