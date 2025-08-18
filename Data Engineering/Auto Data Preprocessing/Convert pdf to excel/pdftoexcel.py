# import tabula
# import os

# # --- Set file paths ---
# input_pdf = r"C:\Users\PCS\Downloads\Merit List _ PM Laptop Scheme 2025.pdf"
# output_excel = r"C:\Users\PCS\Downloads\Merit List _ PM Laptop Scheme 2025.xlsx"

# # --- Check if file exists ---
# if not os.path.exists(input_pdf):
#     print("❌ PDF file not found!")
# else:
#     try:
#         # --- Convert PDF to Excel ---
#         tabula.convert_into(input_pdf, output_excel, output_format="xlsx", pages='all')
#         print(f"✅ Conversion complete. Excel saved to: {output_excel}")
#     except Exception as e:
#         print(f"❌ Error during conversion: {e}")

#without error handling

# import tabula
# import os
# import pandas as pd

# # --- Set file paths ---
# input_pdf = r"C:\Users\PCS\Downloads\Merit List _ PM Laptop Scheme 2025.pdf"
# output_csv = r"C:\Users\PCS\Downloads\Merit List_PMLaptop2025.csv"
# output_excel = r"C:\Users\PCS\Downloads\Merit List_PMLaptop2025.xlsx"

# # --- Convert PDF to CSV (tabula only supports CSV) ---
# try:
#     tabula.convert_into(input_pdf, output_csv, output_format="csv", pages='all')
#     print(f"✅ CSV generated: {output_csv}")

#     # --- Convert CSV to Excel ---
#     df = pd.read_csv(output_csv)
#     df.to_excel(output_excel, index=False)
#     print(f"✅ Excel saved to: {output_excel}")

# except Exception as e:
#     print(f"❌ Error during conversion: {e}")











# with error handling


import tabula
import os
import pandas as pd

# --- Set file paths ---
input_pdf = r"C:\Users\PCS\Downloads\Merit List _ PM Laptop Scheme 2025.pdf"
output_csv = r"C:\Users\PCS\Downloads\Merit List_PMLaptop2025.csv"
output_excel = r"C:\Users\PCS\Downloads\Merit List_PMLaptop2025.xlsx"

# --- Error Handling ---
try:
    # Check if input PDF exists
    if not os.path.exists(input_pdf):
        raise FileNotFoundError(f"Input PDF not found: {input_pdf}")

    # Check if output paths are writable
    output_dir = os.path.dirname(output_csv)
    if output_dir and not os.access(output_dir, os.W_OK):
        raise PermissionError(f"No write permission in directory: {output_dir}")

    # Check if output files already exist
    if os.path.exists(output_csv):
        raise FileExistsError(f"Output CSV already exists: {output_csv}")
    if os.path.exists(output_excel):
        raise FileExistsError(f"Output Excel already exists: {output_excel}")

    # Convert PDF to CSV using tabula
    tabula.convert_into(input_pdf, output_csv, output_format="csv", pages='all')
    print(f"✅ CSV generated: {output_csv}")

    # Convert CSV to Excel using pandas
    df = pd.read_csv(output_csv)
    if df.empty:
        raise ValueError("No data extracted from PDF. The table may be empty or incorrectly formatted.")
    df.to_excel(output_excel, index=False, engine='openpyxl')
    print(f"✅ Excel saved to: {output_excel}")

except FileNotFoundError as e:
    print(f"❌ File Error: {e}")
except PermissionError as e:
    print(f"❌ Permission Error: {e}")
except FileExistsError as e:
    print(f"❌ File Exists Error: {e}")
except tabula.errors.JavaNotFoundError:
    print("❌ Java Error: Java is not installed or not found. Install Java to use tabula-py.")
except pd.errors.EmptyDataError:
    print("❌ CSV Error: The generated CSV is empty or corrupted.")
except pd.errors.ParserError:
    print("❌ CSV Error: Failed to parse the CSV file. The PDF table structure may be invalid.")
except ValueError as e:
    print(f"❌ Data Error: {e}")
except Exception as e:
    print(f"❌ Unexpected Error: {e}. Please check the PDF or dependencies.")













#with improvements (not worked well)

# import tabula
# import os
# import pandas as pd
# import logging
# from tqdm import tqdm

# # --- Setup Logging ---
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logger = logging.getLogger(__name__)

# # --- Set file paths ---
# input_pdf = r"C:\Users\PCS\Downloads\Merit List _ PM Laptop Scheme 2025.pdf"
# output_csv = r"C:\Users\PCS\Downloads\Merit List_PMLaptop2025.csv"
# output_excel = r"C:\Users\PCS\Downloads\Merit List_PMLaptop2025.xlsx"

# # --- Flag for overwriting output files ---
# force_overwrite = True  # Set to True to allow overwriting; change to False to prevent

# # --- Error Handling ---
# try:
#     # Check if input PDF exists
#     if not os.path.exists(input_pdf):
#         raise FileNotFoundError(f"Input PDF not found: {input_pdf}")

#     # Check if output paths are writable
#     output_dir = os.path.dirname(output_csv)
#     if output_dir and not os.access(output_dir, os.W_OK):
#         raise PermissionError(f"No write permission in directory: {output_dir}")

#     # Check if output files already exist (unless overwriting is allowed)
#     if not force_overwrite:
#         if os.path.exists(output_csv):
#             raise FileExistsError(f"Output CSV already exists: {output_csv}")
#         if os.path.exists(output_excel):
#             raise FileExistsError(f"Output Excel already exists: {output_excel}")

#     # Extract tables from PDF with progress feedback
#     logger.info(f"Extracting tables from {input_pdf}")
#     # Get total pages for progress bar (using a lightweight JSON read)
#     total_pages = len(tabula.read_pdf(input_pdf, pages='all', output_format='json'))
#     dfs = []
#     for page in tqdm(range(1, total_pages + 1), desc="Processing pages"):
#         page_dfs = tabula.read_pdf(input_pdf, pages=str(page), stream=True, multiple_tables=True)
#         dfs.extend(page_dfs if page_dfs else [])
    
#     if not dfs:
#         raise ValueError("No tables found in the PDF.")

#     # Combine tables and clean data
#     df = pd.concat(dfs, ignore_index=True) if len(dfs) > 1 else dfs[0]
#     df = df.dropna(how='all')  # Remove empty rows
#     df.columns = df.columns.str.strip()  # Clean column names
#     df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # Clean string data

#     # Validate data
#     if df.empty:
#         raise ValueError("No data extracted from PDF. The table may be empty or incorrectly formatted.")

#     # Save to CSV
#     df.to_csv(output_csv, index=False)
#     logger.info(f"✅ CSV generated: {output_csv}")

#     # Save to Excel
#     df.to_excel(output_excel, index=False, engine='openpyxl')
#     logger.info(f"✅ Excel saved to: {output_excel}")

# except FileNotFoundError as e:
#     logger.error(f"❌ File Error: {e}")
# except PermissionError as e:
#     logger.error(f"❌ Permission Error: {e}")
# except FileExistsError as e:
#     logger.error(f"❌ File Exists Error: {e}")
# except tabula.errors.JavaNotFoundError:
#     logger.error("❌ Java Error: Java is not installed or not found. Install Java to use tabula-py.")
# except pd.errors.EmptyDataError:
#     logger.error("❌ CSV Error: The generated CSV is empty or corrupted.")
# except pd.errors.ParserError:
#     logger.error("❌ CSV Error: Failed to parse the CSV file. The PDF table structure may be invalid.")
# except ValueError as e:
#     logger.error(f"❌ Data Error: {e}")
# except Exception as e:
#     logger.error(f"❌ Unexpected Error: {e}. Please check the PDF or dependencies.")













# import tabula
# import os
# import pandas as pd
# import logging
# from tqdm import tqdm
# from PyPDF2 import PdfReader

# # --- Setup Logging ---
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logger = logging.getLogger(__name__)

# # --- Set file paths ---
# input_pdf = r"C:\Users\PCS\Downloads\Merit List _ PM Laptop Scheme 2025.pdf"
# output_csv = r"C:\Users\PCS\Downloads\Merit List_PMLaptop2025.csv"
# output_excel = r"C:\Users\PCS\Downloads\Merit List_PMLaptop2025.xlsx"

# # --- Flag for overwriting output files ---
# force_overwrite = True  # Set to True to allow overwriting; change to False to prevent

# # --- Error Handling ---
# try:
#     # Check if input PDF exists
#     if not os.path.exists(input_pdf):
#         raise FileNotFoundError(f"Input PDF not found: {input_pdf}")

#     # Check if output paths are writable
#     output_dir = os.path.dirname(output_csv)
#     if output_dir and not os.access(output_dir, os.W_OK):
#         raise PermissionError(f"No write permission in directory: {output_dir}")

#     # Check if output files already exist (unless overwriting is allowed)
#     if not force_overwrite:
#         if os.path.exists(output_csv):
#             raise FileExistsError(f"Output CSV already exists: {output_csv}")
#         if os.path.exists(output_excel):
#             raise FileExistsError(f"Output Excel already exists: {output_excel}")

#     # Get total pages efficiently using PyPDF2
#     logger.info(f"Determining total pages in {input_pdf}")
#     pdf_reader = PdfReader(input_pdf)
#     total_pages = len(pdf_reader.pages)
#     logger.info(f"Total pages: {total_pages}")

#     # Extract tables from PDF in batches with progress feedback and encoding fix
#     logger.info(f"Extracting tables from {input_pdf}")
#     dfs = []
#     batch_size = 50  # Process 50 pages at a time to manage memory
#     for start_page in tqdm(range(1, total_pages + 1, batch_size), desc="Processing page batches", unit="batch"):
#         end_page = min(start_page + batch_size - 1, total_pages)
#         try:
#             # Use latin1 encoding to handle non-UTF-8 characters
#             page_dfs = tabula.read_pdf(
#                 input_pdf,
#                 pages=f"{start_page}-{end_page}",
#                 stream=True,
#                 multiple_tables=True,
#                 guess=False,
#                 encoding="latin1"
#             )
#             if page_dfs:
#                 for i, df_page in enumerate(page_dfs):
#                     logger.info(f"Batch {start_page}-{end_page}, Table {i+1}: {df_page.shape}, Columns: {list(df_page.columns)}")
#                 dfs.extend(page_dfs)
#             else:
#                 logger.warning(f"No tables found in page range {start_page}-{end_page}")
#         except Exception as e:
#             logger.warning(f"Failed to process page range {start_page}-{end_page}: {str(e)}")

#     if not dfs:
#         raise ValueError("No tables found in the PDF. Consider using lattice=True or OCR for scanned PDFs.")

#     # Combine tables and clean data
#     logger.info("Combining and cleaning extracted tables")
#     if len(dfs) > 1:
#         # Find the table with the most columns as the reference
#         max_columns = max(len(df.columns) for df in dfs)
#         reference_df = max(dfs, key=lambda df: len(df.columns))
#         common_columns = reference_df.columns
#         filtered_dfs = []
#         for i, df_page in enumerate(dfs):
#             if len(df_page.columns) == max_columns:
#                 filtered_dfs.append(df_page)
#             else:
#                 logger.warning(f"Skipping table {i+1} with {len(df_page.columns)} columns (expected {max_columns})")
#         if not filtered_dfs:
#             raise ValueError("No tables with consistent column count found.")
#         df = pd.concat(filtered_dfs, ignore_index=True)
#     else:
#         df = dfs[0]

#     # Clean data
#     df = df.dropna(how='all')  # Remove empty rows
#     df.columns = df.columns.str.strip()  # Clean column names
#     df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # Clean string data

#     # Validate data
#     if df.empty:
#         raise ValueError("No data extracted from PDF. The table may be empty or incorrectly formatted.")
    
#     # Log table shape and sample data for debugging
#     logger.info(f"Extracted table shape: {df.shape}")
#     logger.info(f"Columns: {list(df.columns)}")
#     if not df.empty:
#         logger.info(f"Sample data (first row): \n{df.head(1)}")

#     # Check for expected columns (adjust based on your PDF's structure)
#     expected_columns = ["Name", "Roll No", "Merit Position"]  # Example; modify as needed
#     missing_columns = [col for col in expected_columns if col not in df.columns]
#     if missing_columns:
#         logger.warning(f"Missing expected columns: {missing_columns}")

#     # Save to CSV
#     df.to_csv(output_csv, index=False, encoding="utf-8")
#     logger.info(f"✅ CSV generated: {output_csv}")

#     # Save to Excel
#     df.to_excel(output_excel, index=False, engine='openpyxl')
#     logger.info(f"✅ Excel saved to: {output_excel}")

# except FileNotFoundError as e:
#     logger.error(f"❌ File Error: {e}")
# except PermissionError as e:
#     logger.error(f"❌ Permission Error: {e}")
# except FileExistsError as e:
#     logger.error(f"❌ File Exists Error: {e}")
# except tabula.errors.JavaNotFoundError:
#     logger.error("❌ Java Error: Java is not installed or not found. Install Java to use tabula-py.")
# except pd.errors.EmptyDataError:
#     logger.error("❌ CSV Error: The generated CSV is empty or corrupted.")
# except pd.errors.ParserError:
#     logger.error("❌ CSV Error: Failed to parse the CSV file. The PDF table structure may be invalid.")
# except ValueError as e:
#     logger.error(f"❌ Data Error: {e}")
# except Exception as e:
#     logger.error(f"❌ Unexpected Error: {e}. Please check the PDF or dependencies.")