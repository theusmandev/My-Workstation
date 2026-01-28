# from flask import Flask, request, jsonify, render_template
# import pandas as pd
# import re
# from fuzzywuzzy import process
# from flask_cors import CORS  # Enable CORS

# app = Flask(__name__, template_folder="templates")  # Serve HTML files from "templates" folder
# CORS(app)  # Allow frontend to communicate with backend

# EXCEL_FILE = r"D:\UNB\Programs\scrapenovels.py\aichatbot\urdu_novels.xlsx"

# def normalize_text(text):
#     """ Remove special characters & extra spaces, and convert to lowercase. """
#     if not isinstance(text, str):
#         return ""
#     text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
#     return re.sub(r"\s+", " ", text).strip().lower()  # Normalize spaces & lowercase

# def load_data():
#     """ Load the Excel file and normalize column names. """
#     try:
#         df = pd.read_excel(EXCEL_FILE, dtype=str, engine="openpyxl")  # Ensure correct engine
#         df.columns = df.columns.str.strip().str.lower()  # Normalize column names

#         print("✅ Columns in Excel file:", df.columns)  # Debugging

#         column_mapping = {"download links": "link", "titles": "title"}
#         df.rename(columns={k: v for k, v in column_mapping.items() if k in df.columns}, inplace=True)

#         if not {"title", "link"}.issubset(df.columns):
#             print("❌ Error: Missing required columns! Found:", df.columns)
#             return None

#         # Normalize title column for better searching
#         df["normalized_title"] = df["title"].apply(normalize_text)

#         print(f"📊 Data Loaded Successfully. Rows: {len(df)}")
#         return df
#     except Exception as e:
#         print("❌ Error loading file:", e)
#         return None

# def search_novels(query):
#     """ Search novels using fuzzy matching and return best matches. """
#     df = load_data()
#     if df is None:
#         return {"error": "Failed to load data"}

#     query = normalize_text(query)  # Normalize search query
#     print(f"🔍 Searching for: {query}")  # Debugging

#     # Use fuzzy matching to find closest matches
#     choices = df["normalized_title"].tolist()
#     best_matches = process.extract(query, choices, limit=10, scorer=process.fuzz.partial_ratio)

#     # Extract matched titles where score > 60
#     matched_titles = [match for (match, score) in best_matches if score > 60]

#     if not matched_titles:
#         print("⚠️ No matching results found!")
#         return {"message": "No matching results found"}

#     # Filter dataframe for matched titles
#     results = df[df["normalized_title"].isin(matched_titles)][["title", "link"]]

#     print("📌 Matched Titles:", results["title"].tolist())

#     return results.to_dict(orient="records")

# @app.route("/")
# def index():
#     """ Serve the HTML frontend """
#     return render_template("index.html")

# @app.route("/search", methods=["GET"])
# def search():
#     """ API endpoint for searching novels. """
#     query = request.args.get("query", "").strip()
#     if not query:
#         return jsonify({"error": "Query parameter is required"}), 400

#     results = search_novels(query)
#     return jsonify(results)

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, request, jsonify, render_template
# import pandas as pd
# import re
# from fuzzywuzzy import process
# from flask_cors import CORS  # Import CORS

# app = Flask(__name__, template_folder="templates")

# # ✅ Enable CORS for all routes
# CORS(app)

# EXCEL_FILE = r"D:\UNB\Programs\scrapenovels.py\aichatbot\urdu_novels.xlsx"

# def normalize_text(text):
#     """ Remove special characters & extra spaces, and convert to lowercase. """
#     if not isinstance(text, str):
#         return ""
#     text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
#     return re.sub(r"\s+", " ", text).strip().lower()  # Normalize spaces & lowercase

# def load_data():
#     """ Load the Excel file and normalize column names. """
#     try:
#         df = pd.read_excel(EXCEL_FILE, dtype=str, engine="openpyxl")  # Ensure correct engine
#         df.columns = df.columns.str.strip().str.lower()  # Normalize column names

#         column_mapping = {"download links": "link", "titles": "title"}
#         df.rename(columns={k: v for k, v in column_mapping.items() if k in df.columns}, inplace=True)

#         if not {"title", "link"}.issubset(df.columns):
#             print("❌ Error: Missing required columns! Found:", df.columns)
#             return None

#         df["normalized_title"] = df["title"].apply(normalize_text)
#         return df
#     except Exception as e:
#         print("❌ Error loading file:", e)
#         return None

# def search_novels(query):
#     """ Search novels using fuzzy matching and return best matches. """
#     df = load_data()
#     if df is None:
#         return {"error": "Failed to load data"}

#     query = normalize_text(query)  # Normalize search query
#     choices = df["normalized_title"].tolist()
#     best_matches = process.extract(query, choices, limit=50, scorer=process.fuzz.partial_ratio)

#     matched_titles = [match for (match, score) in best_matches if score > 98]

#     if not matched_titles:
#         return {"message": "No matching results found"}

#     results = df[df["normalized_title"].isin(matched_titles)][["title", "link"]]

#     return results.to_dict(orient="records")

# @app.route("/")
# def index():
#     """ Serve the HTML frontend """
#     return render_template("index.html")

# @app.route("/search", methods=["GET"])
# def search():
#     """ API endpoint for searching novels. """
#     query = request.args.get("query", "").strip()
#     if not query:
#         return jsonify({"error": "Query parameter is required"}), 400

#     results = search_novels(query)
#     return jsonify(results)

# if __name__ == "__main__":
#     app.run(debug=True)







from flask import Flask, request, jsonify, render_template
import pandas as pd
import re
from fuzzywuzzy import process, fuzz
from flask_cors import CORS
import logging

app = Flask(__name__, template_folder="templates")
CORS(app)  # Apply CORS globally

EXCEL_FILE = r"D:\UNB\Programs\scrapenovels.py\aichatbot\urdu_novels.xlsx"

# ✅ Configure logging
logging.basicConfig(level=logging.INFO)

def normalize_text(text):
    """ Remove special characters & extra spaces, and convert to lowercase. """
    if not isinstance(text, str):
        return ""
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    return re.sub(r"\s+", " ", text).strip().lower()  # Normalize spaces & lowercase

def load_data():
    """ Load Excel data once & normalize it. """
    try:
        df = pd.read_excel(EXCEL_FILE, dtype=str, engine="openpyxl")
        df.columns = df.columns.str.strip().str.lower()

        column_mapping = {"download links": "link", "titles": "title"}
        df.rename(columns={k: v for k, v in column_mapping.items() if k in df.columns}, inplace=True)

        if not {"title", "link"}.issubset(df.columns):
            logging.error(f"❌ Missing required columns! Found: {df.columns}")
            return None

        df["normalized_title"] = df["title"].apply(normalize_text)
        return df
    except Exception as e:
        logging.error(f"❌ Error loading file: {e}")
        return None

# ✅ Load data once when the app starts
novels_df = load_data()

def search_novels(query):
    """ Search novels using fuzzy matching. """
    if novels_df is None:
        return {"error": "Failed to load data"}

    query = normalize_text(query)
    choices = novels_df["normalized_title"].tolist()
    best_matches = process.extractBests(query, choices, limit=50, scorer=fuzz.partial_ratio)

    matched_titles = [match for match, score in best_matches if score > 95]  # Adjusted threshold

    if not matched_titles:
        return {"message": "No matching results found"}

    results = novels_df[novels_df["normalized_title"].isin(matched_titles)][["title", "link"]]

    return results.to_dict(orient="records")

@app.route("/")
def index():
    """ Serve the frontend """
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    """ API for searching novels. """
    query = request.args.get("query", "").strip()
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    results = search_novels(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
