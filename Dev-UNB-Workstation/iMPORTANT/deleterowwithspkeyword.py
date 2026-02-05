import pandas as pd

# Excel file ko read karna
file_path = r"D:\workstation\smarturdunovelbankokookokokk.xlsx"  # Apni file ka path yahan daalein
df = pd.read_excel(file_path)

# "Urdu Books" wali rows ko filter out karna
df = df[df['Titles'] != 'Digest Library']

# Nayi file mein save karna
output_path = r"D:\workstation\smarturdunovelbankokookokoitsokitsokkk.xlsx"  # Nayi file ka naam
df.to_excel(output_path, index=False)

print("Urdu Books wali rows delete ho gayi hain aur file save ho gayi hai!")