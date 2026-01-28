# import pandas as pd

# EXCEL_FILE = r"D:\UNB\Programs\scrapenovels.py\aichatbot\urdu_novels.xlsx"

# df = pd.read_excel(EXCEL_FILE, dtype=str, engine="openpyxl")

# df.columns = df.columns.str.strip().str.lower()
# df.rename(columns={"download links": "link", "titles": "title"}, inplace=True)

# # ✅ Agar "mediafire links" column nahi chahiye, to isko hata dein
# if "mediafire links" in df.columns:
#     df.drop(columns=["mediafire links"], inplace=True)

# # ✅ JSON file sahi format me save karein
# JSON_FILE = "urdu_novels.json"
# df.to_json(JSON_FILE, orient="records", force_ascii=False, indent=4)

# print(f"✅ JSON file saved: {JSON_FILE}")







# import pandas as pd

# # ✅ Excel file ka path
# EXCEL_FILE = r"E:\UNB\oknovels\okkkkkk - Copyokkk.xlsx"

# # ✅ Excel ko pandas DataFrame me load karein
# df = pd.read_excel(EXCEL_FILE, dtype=str, engine="openpyxl")

# df.columns = df.columns.str.strip().str.lower()
# df.rename(columns={"download links": "link", "titles": "title"}, inplace=True)

# # ✅ JSON file ko sahi format me export karein
# JSON_FILE = r"E:\UNB\oknovels\urdu_novels.json"
# df.to_json(JSON_FILE, orient="records", force_ascii=False, indent=4)

# print(f"✅ JSON file saved: {JSON_FILE}")




# import pandas as pd
# import json

# def excel_to_json(excel_file_path, json_file_path):
#     try:
#         # Read the Excel file
#         # Use `sheet_name` to specify a particular sheet if needed, e.g., sheet_name="Sheet1"
#         df = pd.read_excel(excel_file_path)

#         # Ensure the column names are as expected (optional, adjust if needed)
#         # If your Excel has different column names, rename them to match your requirement
#         df = df.rename(columns={
#             'Titles': 'Titles',
#             'Links': 'Links'
#         })

#         # Convert DataFrame to a list of dictionaries
#         data = df.to_dict(orient='records')

#         # Write to JSON file
#         with open(json_file_path, 'w', encoding='utf-8') as json_file:
#             json.dump(data, json_file, ensure_ascii=False, indent=4)

#         print(f"Successfully converted {excel_file_path} to {json_file_path}")

#     except FileNotFoundError:
#         print(f"Error: The file {excel_file_path} was not found.")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# # Example usage
# excel_file = r"E:\UNB\oknovels\okkkkkk - Copyokkk.xlsx"  # Replace with your Excel file path
# json_file = r"E:\UNB\oknovels\okkkkkk"
# excel_to_json(excel_file, json_file)




import pandas as pd
import json

def excel_to_json(excel_file_path, json_file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file_path)

        # Replace NaN with empty strings or null (adjust as needed)
        df = df.fillna('')  # Replace NaN with empty string; use `df.fillna(None)` for null

        # Ensure column names match
        df = df.rename(columns=lambda x: x.strip())  # Remove any whitespace from column names
        if not all(col in df.columns for col in ['Titles', 'Links']):
            raise ValueError("Excel file must contain 'Titles' and 'Links' columns.")

        # Convert to list of dictionaries
        data = df.to_dict(orient='records')

        # Clean up data to ensure valid JSON
        for item in data:
            for key in item:
                if isinstance(item[key], float) and (pd.isna(item[key]) or item[key] != item[key]):  # Check for NaN
                    item[key] = ''
                elif item[key] is None:
                    item[key] = ''
                # Ensure strings are properly encoded
                if isinstance(item[key], str):
                    item[key] = item[key].strip()

        # Write to JSON file
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        print(f"Successfully converted {excel_file_path} to {json_file_path}")

    except FileNotFoundError:
        print(f"Error: The file {excel_file_path} was not found.")
    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
excel_file = r"E:\UNB\oknovels\okkkkkk - Copyokkk.xlsx"  # Replace with your Excel file path
json_file = r"E:\UNB\oknovels\neww"     # Replace with desired JSON output path

excel_to_json(excel_file, json_file)