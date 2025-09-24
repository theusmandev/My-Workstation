import pandas as pd
import sqlite3
import os


# File Paths
# -------------------------------
input_file = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\VirtualUniversityofPakistan_Final_MeritList - Copy.xlsx"
excel_output = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Combined_Output.xlsx"
csv_output = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Combined_Output.csv"
sqlite_output = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Combined_Data.db"


# Read All Sheets
# -------------------------------
xls = pd.ExcelFile(input_file)
df_list = []
total_rows = 0
blank_rows_total = 0
empty_sheets = 0

print("🔄 Reading sheets...\n")

for sheet in xls.sheet_names:
    print(f"📄 Reading sheet: {sheet}")
    
    # Try reading the sheet
    try:
        df = pd.read_excel(input_file, sheet_name=sheet)
    except Exception as e:
        print(f"⚠️ Skipping {sheet} due to error: {e}")
        continue

    # Count blank rows in the sheet
    sheet_blank_rows = df.isnull().all(axis=1).sum()
    blank_rows_total += sheet_blank_rows

    # Skip empty sheets
    if df.empty:
        empty_sheets += 1
        print(f"⚠️ Skipping empty sheet: {sheet}")
        continue

    rows = df.shape[0]
    total_rows += rows
    print(f"   ✅ {rows} rows loaded ({sheet_blank_rows} completely blank rows)")

    df_list.append(df)

print("\n📊 Summary Before Combining")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"📌 Total sheets read        : {len(xls.sheet_names)}")
print(f"📌 Empty sheets skipped     : {empty_sheets}")
print(f"📌 Total rows (before drop) : {total_rows}")
print(f"📌 Total blank rows         : {blank_rows_total}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

# -------------------------------
# Combine All Sheets
# -------------------------------
print("🔗 Combining all sheets...")
combined_df = pd.concat(df_list, ignore_index=True)

# Count duplicate rows before removing them
duplicate_rows = combined_df.duplicated().sum()

# Remove duplicates
combined_df.drop_duplicates(inplace=True)

print(f"✅ Combined data created!")
print(f"🔍 Duplicate rows found  : {duplicate_rows}")
print(f"📌 Final rows after drop : {combined_df.shape[0]}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

# -------------------------------
# Smart Output Decision
# -------------------------------
EXCEL_ROW_LIMIT = 1_048_576
CSV_ROW_LIMIT = 2_000_000

print("💾 Saving final data...")

if combined_df.shape[0] <= EXCEL_ROW_LIMIT:
    combined_df.to_excel(excel_output, index=False, sheet_name="CombinedSheet")
    print(f"📂 Data saved to Excel: {excel_output}")

elif combined_df.shape[0] <= CSV_ROW_LIMIT:
    combined_df.to_csv(csv_output, index=False)
    print(f"📂 Data saved to CSV: {csv_output}")

else:
    conn = sqlite3.connect(sqlite_output)
    combined_df.to_sql("CombinedData", conn, if_exists="replace", index=False)
    conn.close()
    print(f"🗄️ Data saved to SQLite DB: {sqlite_output}")

print("\n🎉 Process completed successfully!")
