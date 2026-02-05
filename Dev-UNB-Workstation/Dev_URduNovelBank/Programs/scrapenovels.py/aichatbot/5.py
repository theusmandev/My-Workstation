from flask import Flask, request, jsonify, render_template
import pandas as pd
import re
import pickle
from bisect import bisect_left
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")
CORS(app)

EXCEL_FILE = r"D:\\UNB\\Programs\\scrapenovels.py\\aichatbot\\urdu_novels.xlsx"

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

def train_tfidf():
    """ Train and save TF-IDF model """
    vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=5000)  # ✅ Optimized
    tfidf_matrix = vectorizer.fit_transform(df["normalized_title"])
    
    # ✅ Save model for future use
    with open("tfidf_vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    with open("tfidf_matrix.pkl", "wb") as f:
        pickle.dump(tfidf_matrix, f)
    return vectorizer, tfidf_matrix

# ✅ Load or train model
try:
    with open("tfidf_vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    with open("tfidf_matrix.pkl", "rb") as f:
        tfidf_matrix = pickle.load(f)
except FileNotFoundError:
    vectorizer, tfidf_matrix = train_tfidf()

def search_novels(query):
    """ Search novels using optimized TF-IDF ranking """
    query = normalize_text(query)
    query_vec = vectorizer.transform([query])
    cosine_similarities = linear_kernel(query_vec, tfidf_matrix).flatten()
    
    df["score"] = cosine_similarities
    results = df[df["score"] > 0.1].sort_values(by="score", ascending=False)[:10]
    return results[["title", "link"]].to_dict(orient="records")

def autocomplete(query):
    """ Fast autocomplete using binary search """
    query = query.lower()
    titles = sorted(df["normalized_title"].tolist())  # ✅ Sorted for binary search
    index = bisect_left(titles, query)
    return [titles[i] for i in range(index, min(index + 10, len(titles)))]

@app.route("/")
def index():
    """ Serve the frontend HTML """
    return render_template("index3.html")

@app.route("/search", methods=["GET"])
def search():
    """ API endpoint for searching novels """
    query = request.args.get("query", "").strip()
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    results = search_novels(query)
    return jsonify(results)

@app.route("/autocomplete", methods=["GET"])
def autocomplete_api():
    """ API endpoint for autocomplete suggestions """
    query = request.args.get("query", "").strip().lower()
    if not query:
        return jsonify([])
    return jsonify(autocomplete(query))

if __name__ == "__main__":
    app.run(debug=True)