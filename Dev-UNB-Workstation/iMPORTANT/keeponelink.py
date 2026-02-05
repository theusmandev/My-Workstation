import pandas as pd

# Excel file ka path
file_path = r"C:\Users\PCS\Downloads\itsurdu\mergeitsurdu.xlsx"# Apni file ka path yahan daalein

# Nayi file ka path aur naam
output_file = r"C:\Users\PCS\Downloads\itsurdu\mergeitsurdusingle.xlsx" # Nayi file ka naam

# Excel file ko read karna
df = pd.read_excel(file_path)

# "Links" column mein sirf pehla link rakhna
df['Links'] = df['Links'].apply(lambda x: x.split(',')[0].strip() if isinstance(x, str) and ',' in x else x)

# Modified data ko nayi Excel file mein save karna
df.to_excel(output_file, index=False)

print(f"Links column mein sirf pehla link rakha gaya hai aur file {output_file} mein save ho gayi hai!")