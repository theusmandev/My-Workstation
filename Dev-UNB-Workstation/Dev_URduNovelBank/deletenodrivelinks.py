import pandas as pd

# Excel file ka path
file_path =r"C:\Users\PCS\Downloads\itsurdu\mergeitsurdusingle.xlsx" # Apni file ka path yahan daalein

# Nayi file ka path aur naam
output_file = r"C:\Users\PCS\Downloads\itsurdu\ready.xlsx"  # Nayi file ka naam

# Excel file ko read karna
df = pd.read_excel(file_path)

# "Links" column mein "No Google Drive Link" wali rows ko delete karna
df = df[df['Links'] != 'No Mediafire Link']

# Modified data ko nayi Excel file mein save karna
df.to_excel(output_file, index=False)

print(f"'No Google Drive Link' wali rows delete ho gayi hain aur file {output_file} mein save ho gayi hai!")