# import pandas as pd

# # Input Excel file path
# input_file = r'E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\VirtualUniversityofPakistan_Final_MeritList - Copy.xlsx'

# # Output Excel file path (same folder)
# output_file = r'E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Combined_Output.xlsx'

# # Load the Excel file
# xls = pd.ExcelFile(input_file)

# # List to hold dataframes from each sheet
# df_list = []

# # Loop through all sheet names and read each sheet into a dataframe
# for sheet in xls.sheet_names:
#     df = pd.read_excel(xls, sheet_name=sheet)
#     df_list.append(df)

# # Concatenate all dataframes (assuming same headers, it will append rows)
# combined_df = pd.concat(df_list, ignore_index=True)

# # Save the combined dataframe to a new Excel file (in a single sheet)
# combined_df.to_excel(output_file, index=False, sheet_name='CombinedSheet')

# print(f"Combined data saved to {output_file}")





import pandas as pd
import sqlite3
import os

# -------------------------------
# File Paths
# -------------------------------
input_file = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\VirtualUniversityofPakistan_Final_MeritList - Copy.xlsx"
excel_output = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Combined_Output.xlsx"
csv_output = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Combined_Output.csv"
sqlite_output = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Combined_Data.db"


# Read All Sheets in Chunks

xls = pd.ExcelFile(input_file)
df_list = []
total_rows = 0

print("🔄 Reading sheets...")

for sheet in xls.sheet_names:
    print(f"📄 Reading sheet: {sheet}")
    
    # Read sheet in chunks to save memory
    try:
        df = pd.read_excel(input_file, sheet_name=sheet)
    except Exception as e:
        print(f"⚠️ Skipping {sheet} due to error: {e}")
        continue

    # Skip empty sheets
    if df.empty:
        print(f"⚠️ Skipping empty sheet: {sheet}")
        continue

    rows = df.shape[0]
    total_rows += rows
    print(f"   ✅ {rows} rows loaded from {sheet}")
    df_list.append(df)

print(f"\n📊 Total combined rows: {total_rows}")

# -------------------------------
# Combine All Sheets
# -------------------------------
print("🔗 Combining all sheets...")
combined_df = pd.concat(df_list, ignore_index=True)

# Remove duplicates
combined_df.drop_duplicates(inplace=True)

print(f"✅ Final rows after removing duplicates: {combined_df.shape[0]}")

# -------------------------------
# Smart Output Decision
# -------------------------------
EXCEL_ROW_LIMIT = 1_048_576
CSV_ROW_LIMIT = 2_000_000

if combined_df.shape[0] <= EXCEL_ROW_LIMIT:
    # Save to Excel
    combined_df.to_excel(excel_output, index=False, sheet_name="CombinedSheet")
    print(f"📂 Data saved to Excel: {excel_output}")

elif combined_df.shape[0] <= CSV_ROW_LIMIT:
    # Save to CSV (faster than Excel)
    combined_df.to_csv(csv_output, index=False)
    print(f"📂 Data saved to CSV: {csv_output}")

else:
    # Save to SQLite database for very large datasets
    conn = sqlite3.connect(sqlite_output)
    combined_df.to_sql("CombinedData", conn, if_exists="replace", index=False)
    conn.close()
    print(f"🗄️ Data saved to SQLite DB: {sqlite_output}")

print("\n🎉 Process completed successfully!")
