import pdfplumber
import pandas as pd
import os

def pdf_to_excel(pdf_path, output_excel_path):
    try:
        # Initialize an empty list to store all tables
        all_tables = []
        
        # Open the PDF file
        with pdfplumber.open(pdf_path) as pdf:
            # Iterate through all pages
            for page_num, page in enumerate(pdf.pages, 1):
                # Extract tables from the current page
                tables = page.extract_tables()
                # Add each table to the list
                for table_num, table in enumerate(tables, 1):
                    # Convert table to DataFrame
                    # Use default column names if headers are missing or problematic
                    if table and len(table) > 0:
                        # Check if the first row is a valid header (not empty or None)
                        headers = table[0]
                        if not headers or all(h is None or h == '' for h in headers):
                            # Create default column names
                            headers = [f"Column_{i+1}" for i in range(len(table[1]))]
                        else:
                            # Ensure unique column names by appending index if duplicates exist
                            seen = {}
                            unique_headers = []
                            for i, h in enumerate(headers):
                                h = str(h) if h is not None else f"Column_{i+1}"
                                if h in seen:
                                    seen[h] += 1
                                    unique_headers.append(f"{h}_{seen[h]}")
                                else:
                                    seen[h] = 0
                                    unique_headers.append(h)
                            headers = unique_headers
                        
                        # Create DataFrame with unique headers
                        df = pd.DataFrame(table[1:], columns=headers)
                        all_tables.append(df)
        
        if not all_tables:
            print("No tables found in the PDF.")
            return
        
        # Combine all tables into a single DataFrame
        combined_df = pd.concat(all_tables, ignore_index=True)
        
        # Save the DataFrame to an Excel file
        combined_df.to_excel(output_excel_path, index=False)
        print(f"Excel file saved successfully at: {output_excel_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_pdf = r"C:\Users\PCS\Downloads\Merit List _ PM Laptop Scheme 2025.pdf"  # Replace with your PDF file path
    output_excel = r"C:\Users\PCS\Downloads\Merit List _ PM Laptop Scheme 2025.xlsx"  # Replace with desired output Excel file path
    
    if os.path.exists(input_pdf):
        pdf_to_excel(input_pdf, output_excel)
    else:
        print(f"PDF file not found: {input_pdf}")