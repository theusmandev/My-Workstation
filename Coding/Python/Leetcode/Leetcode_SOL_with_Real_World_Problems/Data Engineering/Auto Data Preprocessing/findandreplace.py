import pandas as pd
import os
import re

def find_replace_excel(input_file, find_text, replace_text):
    try:
        # Validate input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")
        
        # Get the directory of the input file
        input_dir = os.path.dirname(input_file) or '.'
        
        # Define output file path (same directory as input)
        output_file = os.path.join(input_dir, 'modified_' + os.path.basename(input_file))
        
        # Load the Excel file
        df = pd.read_excel(input_file, engine='openpyxl')
        
        # Perform case-insensitive replacement across the entire dataframe
        df = df.apply(lambda x: x.str.replace(f'(?i){re.escape(find_text)}', replace_text, regex=True) if x.dtype == "object" else x)
        
        # Save to the output Excel file
        df.to_excel(output_file, index=False, engine='openpyxl')
        print(f"Successfully saved modified file to '{output_file}'")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except pd.errors.EmptyDataError:
        print(f"Error: The input file '{input_file}' is empty or not a valid Excel file.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_file}' or writing to '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_file = r"D:\workstation\writers\Nabeela_aziz.xlsx"# Replace with your input file path
    find_text = 'Nabila aziz'       # Text to find (case-insensitive)
    replace_text = 'Nabeela Aziz'    # Replacement text
    find_replace_excel(input_file, find_text, replace_text)