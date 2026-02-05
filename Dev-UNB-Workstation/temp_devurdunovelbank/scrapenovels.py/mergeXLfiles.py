import pandas as pd
import os

# 🔹 Folder path jahan Excel aur CSV files hain
folder_path = r"E:\UNB\oknovels" # 📂 Apna folder path yahan set karein

# 🔹 List all supported files (.xlsx, .xls, .csv)
all_files = [file for file in os.listdir(folder_path) if file.endswith(('.xlsx', '.xls', '.csv'))]

# 🔹 Check agar files mojood hain 
if not all_files:
    print("⚠️ No Excel or CSV files found in the folder. Exiting.")
else:
    dfs = []  # 🔹 Sab DataFrames store karne ke liye list

    # 🔹 Har file ko read karna
    for file in all_files:
        file_path = os.path.join(folder_path, file)
        try:
            if file.endswith('.csv'):
                df = pd.read_csv(file_path, encoding='utf-8')  # CSV files read karega
            else:
                df = pd.read_excel(file_path, engine='openpyxl' if file.endswith('.xlsx') else None)  # Excel files read karega
            
            dfs.append(df)
        except Exception as e:
            print(f"❌ Error reading '{file}': {e}")

    # 🔹 Agar koi valid files hain toh merge karein
    if dfs:
        try:
            merged_df = pd.concat(dfs, ignore_index=True, sort=False)

            # 🔹 Output file ko save karna
            output_file_path = os.path.join(folder_path, "merged_output.xlsx")
            merged_df.to_excel(output_file_path, index=False, engine='openpyxl')

            print(f"✅ Merging completed! File saved as '{output_file_path}'")
        except Exception as e:
            print(f"❌ Error while merging files: {e}")
    else:
        print("⚠️ No valid files to merge.")
