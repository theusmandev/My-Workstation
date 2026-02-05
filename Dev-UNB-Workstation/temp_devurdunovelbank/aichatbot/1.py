# from flask import Flask, request, jsonify
# import pandas as pd

# app = Flask(__name__)

# # Excel file ka path
# EXCEL_FILE = "urdu_novels.xlsx"

# # Excel file read karna
# def load_data():
#     try:
#         df = pd.read_excel(EXCEL_FILE, dtype=str)  # Ensure strings only
#         df.columns = df.columns.str.strip()  # Extra spaces remove karna
#         return df
#     except Exception as e:
#         print("Error loading file:", e)
#         return None

# # Novel search function
# def search_novels(query):
#     df = load_data()
#     if df is None:
#         return []

#     if "Title" not in df.columns or "Link" not in df.columns:
#         print("Error: Missing required columns!")
#         return []

#     # Case insensitive search
#     results = df[df["Title"].str.contains(query, case=False, na=False)]
#     return results[["Title", "Link"]].to_dict(orient="records")

# @app.route("/search", methods=["GET"])
# def search():
#     query = request.args.get("query", "")
#     if not query:
#         return jsonify({"error": "Query parameter is required"}), 400

#     results = search_novels(query)
#     return jsonify(results)

# if __name__ == "__main__":
#     app.run(debug=True)





# from flask import Flask, request, jsonify
# import pandas as pd

# app = Flask(__name__)

# EXCEL_FILE = "urdu_novels.xlsx"

# def load_data():
#     try:
#         df = pd.read_excel(EXCEL_FILE, dtype=str)  # Ensure all data is string
#         df.columns = df.columns.str.strip().str.lower()  # Remove spaces & lowercase
#         return df
#     except Exception as e:
#         print("Error loading file:", e)
#         return None

# def search_novels(query):
#     df = load_data()
#     if df is None:
#         return []

#     if "title" not in df.columns or "link" not in df.columns:
#         print("Error: Missing required columns! Found columns:", df.columns)
#         return []

#     results = df[df["title"].str.contains(query, case=False, na=False)]
#     return results[["title", "link"]].to_dict(orient="records")

# @app.route("/search", methods=["GET"])
# def search():
#     query = request.args.get("query", "")
#     if not query:
#         return jsonify({"error": "Query parameter is required"}), 400

#     results = search_novels(query)
#     return jsonify(results)

# if __name__ == "__main__":
#     app.run(debug=True)









# from flask import Flask, request, jsonify
# import pandas as pd

# app = Flask(__name__)

# EXCEL_FILE = "urdu_novels.xlsx"

# def load_data():
#     try:
#         df = pd.read_excel(EXCEL_FILE, dtype=str)  # Ensure all data is string
#         df.columns = df.columns.str.strip().str.lower()  # Remove spaces & lowercase

#         # Rename "download links" to "link"
#         df.rename(columns={"download links": "link"}, inplace=True)
#         return df
#     except Exception as e:
#         print("Error loading file:", e)
#         return None

# def search_novels(query):
#     df = load_data()
#     if df is None:
#         return []

#     if "title" not in df.columns or "link" not in df.columns:
#         print("Error: Missing required columns! Found columns:", df.columns)
#         return []

#     results = df[df["title"].str.contains(query, case=False, na=False)]
#     return results[["title", "link"]].to_dict(orient="records")

# @app.route("/search", methods=["GET"])
# def search():
#     query = request.args.get("query", "")
#     if not query:
#         return jsonify({"error": "Query parameter is required"}), 400

#     results = search_novels(query)
#     return jsonify(results)

# if __name__ == "__main__":
#     app.run(debug=True)




# from flask import Flask, request, jsonify
# import pandas as pd

# app = Flask(__name__)

# EXCEL_FILE = "urdu_novels.xlsx"

# def load_data():
#     try:
#         df = pd.read_excel(EXCEL_FILE, dtype=str)  # Ensure all data is string
#         df.columns = df.columns.str.strip().str.lower()  # Normalize column names

#         # Rename columns if needed
#         column_mapping = {"download links": "link", "titles": "title"}
#         df.rename(columns={k: v for k, v in column_mapping.items() if k in df.columns}, inplace=True)

#         # Check if required columns exist
#         if not {"title", "link"}.issubset(df.columns):
#             print("Error: Missing required columns! Found columns:", df.columns)
#             return None
        
#         return df
#     except Exception as e:
#         print("Error loading file:", e)
#         return None

# def search_novels(query):
#     df = load_data()
#     if df is None:
#         return {"error": "Failed to load data"}

#     query = query.strip().lower()  # Normalize query for better search
#     results = df[df["title"].str.lower().str.contains(query, case=False, na=False)]

#     if results.empty:
#         return {"message": "No matching results found"}

#     return results[["title", "link"]].to_dict(orient="records")

# @app.route("/search", methods=["GET"])
# def search():
#     query = request.args.get("query", "").strip()
#     if not query:
#         return jsonify({"error": "Query parameter is required"}), 400

#     results = search_novels(query)
#     return jsonify(results)

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# import pandas as pd

# app = Flask(__name__)

# EXCEL_FILE = "urdu_novels.xlsx"

# def load_data():
#     try:
#         df = pd.read_excel(EXCEL_FILE, dtype=str)  # Ensure all data is string
#         df.columns = df.columns.str.strip().str.lower()  # Normalize column names
        
#         print("✅ Columns in Excel file:", df.columns)  # Debugging

#         # Rename columns if needed
#         column_mapping = {"download links": "link", "titles": "title"}
#         df.rename(columns={k: v for k, v in column_mapping.items() if k in df.columns}, inplace=True)

#         # Check if required columns exist
#         if not {"title", "link"}.issubset(df.columns):
#             print("❌ Error: Missing required columns! Found:", df.columns)
#             return None
        
#         print(f"📊 Data Loaded Successfully. Rows: {len(df)}")
#         return df
#     except Exception as e:
#         print("❌ Error loading file:", e)
#         return None

# def search_novels(query):
#     df = load_data()
#     if df is None:
#         return {"error": "Failed to load data"}

#     query = query.strip().lower()  # Normalize query
#     print(f"🔍 Searching for: {query}")  # Debugging

#     # Check for partial match
#     results = df[df["title"].str.lower().str.contains(query, na=False)]

#     if results.empty:
#         print("⚠️ No matching results found!")
#         return {"message": "No matching results found"}

#     print(f"📌 Found {len(results)} results")  # Debugging
#     return results[["title", "link"]].to_dict(orient="records")

# @app.route("/search", methods=["GET"])
# def search():
#     query = request.args.get("query", "").strip()
#     if not query:
#         return jsonify({"error": "Query parameter is required"}), 400

#     results = search_novels(query)
#     return jsonify(results)

# if __name__ == "__main__":
#     app.run(debug=True)








# from flask import Flask, request, jsonify
# import pandas as pd
# import re

# app = Flask(__name__)

# EXCEL_FILE = r"D:\UNB\Programs\scrapenovels.py\aichatbot\urdu_novels.xlsx"


# def normalize_text(text):
#     """ Remove special characters & extra spaces, and convert to lowercase. """
#     if not isinstance(text, str):
#         return ""
#     text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
#     return re.sub(r"\s+", " ", text).strip().lower()  # Normalize spaces & lowercase

# def load_data():
#     try:
#         df = pd.read_excel(EXCEL_FILE, dtype=str, engine="openpyxl")  # Ensure correct engine
#         df.columns = df.columns.str.strip().str.lower()  

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
#     df = load_data()
#     if df is None:
#         return {"error": "Failed to load data"}

#     query = normalize_text(query)  # Normalize search query
#     print(f"🔍 Searching for: {query}")  # Debugging

#     results = df[df["normalized_title"].str.contains(query, case=False, na=False)]

#     if results.empty:
#         print("⚠️ No matching results found!")
#         return {"message": "No matching results found"}

#     # Show found titles for debugging
#     print("📌 Matched Titles:", results["title"].tolist())  

#     return results[["title", "link"]].to_dict(orient="records")

# @app.route("/search", methods=["GET"])
# def search():
#     query = request.args.get("query", "").strip()
#     if not query:
#         return jsonify({"error": "Query parameter is required"}), 400

#     results = search_novels(query)
#     return jsonify(results)

# if __name__ == "__main__":
#     app.run(debug=True)






from flask import Flask, request, jsonify
import pandas as pd
import re
from fuzzywuzzy import process

app = Flask(__name__)

EXCEL_FILE = r"D:\UNB\Programs\scrapenovels.py\aichatbot\urdu_novels.xlsx"

def normalize_text(text):
    """ Remove special characters & extra spaces, and convert to lowercase. """
    if not isinstance(text, str):
        return ""
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    return re.sub(r"\s+", " ", text).strip().lower()  # Normalize spaces & lowercase

def load_data():
    """ Load the Excel file and normalize column names. """
    try:
        df = pd.read_excel(EXCEL_FILE, dtype=str, engine="openpyxl")  # Ensure correct engine
        df.columns = df.columns.str.strip().str.lower()  # Normalize column names

        print("✅ Columns in Excel file:", df.columns)  # Debugging

        column_mapping = {"download links": "link", "titles": "title"}
        df.rename(columns={k: v for k, v in column_mapping.items() if k in df.columns}, inplace=True)

        if not {"title", "link"}.issubset(df.columns):
            print("❌ Error: Missing required columns! Found:", df.columns)
            return None

        # Normalize title column for better searching
        df["normalized_title"] = df["title"].apply(normalize_text)

        print(f"📊 Data Loaded Successfully. Rows: {len(df)}")
        return df
    except Exception as e:
        print("❌ Error loading file:", e)
        return None

def search_novels(query):
    """ Search novels using fuzzy matching and return best matches. """
    df = load_data()
    if df is None:
        return {"error": "Failed to load data"}

    query = normalize_text(query)  # Normalize search query
    print(f"🔍 Searching for: {query}")  # Debugging

    # Use fuzzy matching to find closest matches
    choices = df["normalized_title"].tolist()
    best_matches = process.extract(query, choices, limit=10, scorer=process.fuzz.partial_ratio)

    # Extract matched titles where score > 60
    matched_titles = [match for (match, score) in best_matches if score > 90]

    if not matched_titles:
        print("⚠️ No matching results found!")
        return {"message": "No matching results found"}

    # Filter dataframe for matched titles
    results = df[df["normalized_title"].isin(matched_titles)][["title", "link"]]

    print("📌 Matched Titles:", results["title"].tolist())

    return results.to_dict(orient="records")

@app.route("/search", methods=["GET"])
def search():
    """ API endpoint for searching novels. """
    query = request.args.get("query", "").strip()
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    results = search_novels(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
