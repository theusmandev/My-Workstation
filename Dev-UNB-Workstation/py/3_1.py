# from flask import Flask, request, jsonify, render_template
# import pandas as pd
# import re
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from flask_cors import CORS
# from nltk.corpus import wordnet

# app = Flask(__name__, template_folder="templates")
# CORS(app)  # ✅ Enable CORS

# EXCEL_FILE = r"D:\UNB\Programs\scrapenovels.py\aichatbot\urdu_novels.xlsx"

# # ✅ Load Data
# df = pd.read_excel(EXCEL_FILE, dtype=str, engine="openpyxl")
# df.columns = df.columns.str.strip().str.lower()
# df.rename(columns={"download links": "link", "titles": "title", "summary": "summary", "image": "image"}, inplace=True)

# def normalize_text(text):
#     """ Normalize text (remove special characters, lowercase) """
#     if not isinstance(text, str):
#         return ""
#     text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
#     return re.sub(r"\s+", " ", text).strip().lower()

# df["normalized_title"] = df["title"].apply(normalize_text)

# # ✅ Train TF-IDF model
# vectorizer = TfidfVectorizer()
# tfidf_matrix = vectorizer.fit_transform(df["normalized_title"])

# def get_synonyms(word):
#     """ Fetch synonyms from WordNet """
#     synonyms = set()
#     for syn in wordnet.synsets(word):
#         for lemma in syn.lemmas():
#             synonyms.add(lemma.name().lower().replace("_", " "))
#     return synonyms

# def search_novels(query):
#     """ Search novels using TF-IDF ranking + synonyms """
#     query = normalize_text(query)
#     words = query.split()
    
#     all_variations = set(words)
#     for word in words:
#         all_variations.update(get_synonyms(word))  # ✅ Add synonyms

#     query_vec = vectorizer.transform([" ".join(all_variations)])
#     cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
#     df["score"] = cosine_similarities
#     results = df[df["score"] > 0.1].sort_values(by="score", ascending=False)[:10]  # ✅ Top 10 results

#     return results[["title", "link", "summary", "image"]].to_dict(orient="records")

# @app.route("/")
# def index():
#     """ Serve the frontend HTML """
#     return render_template("index1.html")

# @app.route("/search", methods=["GET"])
# def search():
#     """ API endpoint for searching novels """
#     query = request.args.get("query", "").strip()
#     if not query:
#         return jsonify({"error": "Query parameter is required"}), 400

#     results = search_novels(query)
#     return jsonify(results)

# @app.route("/autocomplete", methods=["GET"])
# def autocomplete():
#     """ API endpoint for autocomplete suggestions """
#     query = request.args.get("query", "").strip().lower()
#     if not query:
#         return jsonify([])

#     matches = df[df["normalized_title"].str.startswith(query)]["title"].tolist()[:10]  # ✅ First 10 matches
#     return jsonify(matches)

# if __name__ == "__main__":
#     app.run(debug=True)









from flask import Flask, request, jsonify, render_template
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")
CORS(app)  # ✅ Enable CORS

EXCEL_FILE = r"D:\UNB\Programs\scrapenovels.py\aichatbot\urdu_novels.xlsx"

# ✅ Load Data
df = pd.read_excel(EXCEL_FILE, dtype=str, engine="openpyxl")
df.columns = df.columns.str.strip().str.lower()
df.rename(columns={"download links": "link", "titles": "title"}, inplace=True)

def normalize_text(text):
    """ Normalize text (remove special characters, lowercase) """
    if not isinstance(text, str):
        return ""
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()

df["normalized_title"] = df["title"].apply(normalize_text)

# ✅ Train TF-IDF model
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["normalized_title"])

def search_novels(query):
    """ Search novels using TF-IDF ranking """
    query = normalize_text(query)
    query_vec = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    df["score"] = cosine_similarities
    results = df[df["score"] > 0.1].sort_values(by="score", ascending=False)[:10]  # ✅ Top 10 results

    return results[["title", "link"]].to_dict(orient="records")

@app.route("/")
def index():
    """ Serve the frontend HTML """
    return render_template("index1.html")

@app.route("/search", methods=["GET"])
def search():
    """ API endpoint for searching novels """
    query = request.args.get("query", "").strip()
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    results = search_novels(query)
    return jsonify(results)

@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    """ API endpoint for autocomplete suggestions """
    query = request.args.get("query", "").strip().lower()
    if not query:
        return jsonify([])

    matches = df[df["normalized_title"].str.startswith(query)]["title"].tolist()[:10]  # ✅ First 10 matches
    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)
