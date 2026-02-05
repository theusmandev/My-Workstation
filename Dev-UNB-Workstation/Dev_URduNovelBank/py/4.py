import pandas as pd

# ✅ Apni Excel file ka path replace karein
EXCEL_FILE = r"D:\UNB\Programs\scrapenovels.py\aichatbot\urdu_novels.xlsx"

# ✅ Excel file ko load karein
df = pd.read_excel(EXCEL_FILE, dtype=str, engine="openpyxl")

# ✅ Columns ka naam sahi karein
df.columns = df.columns.str.strip().str.lower()
df.rename(columns={"download links": "link", "titles": "title"}, inplace=True)

# ✅ JSON file generate karein
JSON_FILE = "urdu_novels.json"
df.to_json(JSON_FILE, orient="records", force_ascii=False, indent=4)

print(f"✅ JSON file saved: {JSON_FILE}")
