



import pandas as pd
import os

# Input file path
input_file = r"E:\unb-workstation\Writers All Novels\Uploadings\General thelibrarypk Workstation\Excel files\Asia mirza.xlsx"
df = pd.read_excel(input_file)

# Sort the DataFrame by the 'Titles' column
df_sorted = df.sort_values(by='Titles', ascending=True)

# Get input file name without extension
file_name = os.path.splitext(os.path.basename(input_file))[0]

# Create output file path with '_sorted' added to file name
output_file = os.path.join(os.path.dirname(input_file), f"{file_name}_sorted.xlsx")

# Save the sorted DataFrame to the new file
df_sorted.to_excel(output_file, index=False)

print(f"Sorted Excel file saved as {output_file}")
