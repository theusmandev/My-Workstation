import pandas as pd
import sqlite3
import os
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor
import logging

# -------------------------------
# Configure Logging
# -------------------------------
logging.basicConfig(
    filename=r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\process.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Script started")

# -------------------------------
# File Paths
# -------------------------------
input_file = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\VirtualUniversityofPakistan_Final_MeritList - Copy.xlsx"
excel_output = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Combined_Output.xlsx"
csv_output = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Combined_Output.csv"
sqlite_output = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Combined_Data.db"
duplicate_file = r"E:\My-Workstation\Data Analytics\Data Analytics Projects\PM Laptop Final Merit List\Duplicates_Log.csv"

# -------------------------------
# Error Handling for File Paths
# -------------------------------
if not os.path.exists(input_file):
    logging.error(f"Input file {input_file} does not exist")
    print(f"❌ Error: Input file {input_file} does not exist!")
    exit(1)

# Create output directory if it doesn't exist
output_dir = os.path.dirname(excel_output)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    logging.info(f"Created output directory: {output_dir}")
    print(f"📁 Created output directory: {output_dir}")

# -------------------------------
# Read All Sheets with Parallel Processing
# -------------------------------
def read_sheet(sheet_name):
    try:
        df = pd.read_excel(input_file, sheet_name=sheet_name)
        blank_rows = df.isnull().all(axis=1).sum()
        rows = df.shape[0]
        return df, blank_rows, rows, sheet_name
    except Exception as e:
        logging.error(f"Error reading sheet {sheet_name}: {e}")
        return None, 0, 0, sheet_name

def process_sheets():
    xls = pd.ExcelFile(input_file)
    df_list = []
    total_rows = 0
    blank_rows_total = 0
    empty_sheets = 0

    print("🔄 Reading sheets...\n")
    logging.info("Starting to read sheets")

    try:
        # Attempt parallel processing
        with ProcessPoolExecutor() as executor:
            results = list(tqdm(executor.map(read_sheet, xls.sheet_names), total=len(xls.sheet_names), desc="Reading sheets"))
    except Exception as e:
        # Fallback to sequential processing if parallel fails
        logging.warning(f"Parallel processing failed: {e}. Falling back to sequential processing.")
        print(f"⚠️ Parallel processing failed: {e}. Falling back to sequential processing.")
        results = [read_sheet(sheet) for sheet in tqdm(xls.sheet_names, desc="Reading sheets sequentially")]

    for df, sheet_blank_rows, rows, sheet_name in results:
        if df is not None and not df.empty:
            print(f"📄 Reading sheet: {sheet_name}")
            print(f"   ✅ {rows} rows loaded ({sheet_blank_rows} completely blank rows)")
            df_list.append(df)
            total_rows += rows
            blank_rows_total += sheet_blank_rows
        else:
            empty_sheets += 1
            print(f"⚠️ Skipping empty sheet: {sheet_name}")
            logging.warning(f"Skipped empty or invalid sheet: {sheet_name}")

    print("\n📊 Summary Before Combining")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📌 Total sheets read        : {len(xls.sheet_names)}")
    print(f"📌 Empty sheets skipped     : {empty_sheets}")
    print(f"📌 Total rows (before drop) : {total_rows}")
    print(f"📌 Total blank rows         : {blank_rows_total}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    logging.info(f"Total sheets read: {len(xls.sheet_names)}, Empty sheets: {empty_sheets}, Total rows: {total_rows}, Blank rows: {blank_rows_total}")

    # -------------------------------
    # Combine All Sheets
    # -------------------------------
    print("🔗 Combining all sheets...")
    logging.info("Combining all sheets")
    combined_df = pd.concat(df_list, ignore_index=True)

    # Count and log duplicate rows
    duplicate_rows = combined_df.duplicated().sum()
    if duplicate_rows > 0:
        duplicates = combined_df[combined_df.duplicated(keep=False)]
        duplicates.to_csv(duplicate_file, index=False)
        print(f"📜 Duplicates logged to: {duplicate_file}")
        logging.info(f"Duplicates logged to: {duplicate_file}")

    # Remove duplicates
    combined_df.drop_duplicates(inplace=True)

    print(f"✅ Combined data created!")
    print(f"🔍 Duplicate rows found  : {duplicate_rows}")
    print(f"📌 Final rows after drop : {combined_df.shape[0]}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    logging.info(f"Duplicate rows found: {duplicate_rows}, Final rows after drop: {combined_df.shape[0]}")

  
    # Smart Output Decision
   
    EXCEL_ROW_LIMIT = 1_048_576
    CSV_ROW_LIMIT = 2_000_000

    print("💾 Saving final data...")
    logging.info("Saving final data")

    if combined_df.shape[0] <= EXCEL_ROW_LIMIT:
        combined_df.to_excel(excel_output, index=False, sheet_name="CombinedSheet")
        print(f"📂 Data saved to Excel: {excel_output}")
        logging.info(f"Data saved to Excel: {excel_output}")
    elif combined_df.shape[0] <= CSV_ROW_LIMIT:
        combined_df.to_csv(csv_output, index=False)
        print(f"📂 Data saved to CSV: {csv_output}")
        logging.info(f"Data saved to CSV: {csv_output}")
    else:
        conn = sqlite3.connect(sqlite_output)
        combined_df.to_sql("CombinedData", conn, if_exists="replace", index=False)
        conn.close()
        print(f"🗄️ Data saved to SQLite DB: {sqlite_output}")
        logging.info(f"Data saved to SQLite DB: {sqlite_output}")

    print("\n🎉 Process completed successfully!")
    logging.info("Script completed successfully")

if __name__ == '__main__':
    from multiprocessing import freeze_support
    freeze_support()
    process_sheets()