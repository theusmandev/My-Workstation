"""
Mini Search Engine - Flask single-file app
Run: pip install flask requests beautifulsoup4 scikit-learn
Then: python mini_search_engine_flask.py
Open: http://127.0.0.1:5000

Features:
- Crawl a single domain (start URL) up to max_pages
- Store pages in SQLite
- Build TF-IDF index using scikit-learn for ranking
- Browser UI: Crawl form, Search box, Results with relevance scores
- Simple rate limiting and robots.txt respect

Note: This is a synchronous crawler. For large crawls, consider using asynchronous workers or Scrapy.
"""
from flask import Flask, request, redirect, url_for, render_template_string, g
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag, urlparse
import sqlite3
import time
import urllib.robotparser
from sklearn.feature_extraction.text import TfidfVectorizer
import threading

DB_PATH = 'mini_search.db'
USER_AGENT = 'MiniGoogleBot/1.0 (+youremail@example.com)'

app = Flask(__name__)

# -------------------- Database helpers --------------------
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    db = sqlite3.connect(DB_PATH)
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS pages (
                    url TEXT PRIMARY KEY,
                    title TEXT,
                    content TEXT
                )''')
    db.commit()
    db.close()

# -------------------- Crawler --------------------

def normalize(url):
    url, _ = urldefrag(url)
    return url


def crawl_domain(start_url, max_pages=50, delay=1.0):
    parsed_start = urlparse(start_url)
    allowed_domain = parsed_start.netloc

    # robots
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urljoin(start_url, '/robots.txt'))
    try:
        rp.read()
    except:
        # if robots not reachable, proceed but be conservative
        pass

    def is_allowed(url):
        try:
            return rp.can_fetch('*', url)
        except:
            return True

    seen = set()
    queue = [start_url]

    db = sqlite3.connect(DB_PATH)
    cur = db.cursor()

    headers = {'User-Agent': USER_AGENT}

    while queue and len(seen) < max_pages:
        url = normalize(queue.pop(0))
        if url in seen:
            continue
        if urlparse(url).netloc != allowed_domain:
            continue
        if not is_allowed(url):
            print('Blocked by robots:', url)
            continue

        try:
            resp = requests.get(url, timeout=10, headers=headers)
            if resp.status_code != 200:
                print('Non-200:', resp.status_code, url)
                continue

            soup = BeautifulSoup(resp.text, 'html.parser')
            title = soup.title.string.strip() if soup.title and soup.title.string else ''
            text = ' '.join(soup.get_text(separator=' ', strip=True').split())

            cur.execute('INSERT OR REPLACE INTO pages (url, title, content) VALUES (?, ?, ?)',
                        (url, title, text))
            db.commit()
            print('Crawled:', url)

            seen.add(url)

            # extract links
            for a in soup.find_all('a', href=True):
                new = normalize(urljoin(url, a['href']))
                if new not in seen and urlparse(new).netloc == allowed_domain:
                    queue.append(new)

        except Exception as e:
            print('Error:', e, 'for', url)

        time.sleep(delay)

    db.close()
    print('Crawl finished. Pages crawled:', len(seen))

# -------------------- Search / Index --------------------

def load_pages():
    db = sqlite3.connect(DB_PATH)
    cur = db.cursor()
    cur.execute('SELECT url, title, content FROM pages')
    rows = cur.fetchall()
    db.close()
    pages = [{'url': r[0], 'title': r[1], 'content': r[2]} for r in rows]
    return pages


def rank_results(query, pages, top_k=20):
    # Use TF-IDF to rank pages by relevance to the query
    docs = [p['content'] or '' for p in pages]
    if not docs:
        return []
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(docs)
    q_vec = vectorizer.transform([query])
    # cosine similarity
    import numpy as np
    scores = (X @ q_vec.T).toarray().ravel()
    ranked_idx = np.argsort(-scores)
    results = []
    for idx in ranked_idx[:top_k]:
        if scores[idx] > 0:
            p = pages[idx].copy()
            p['score'] = float(scores[idx])
            results.append(p)
    return results

# -------------------- Flask routes --------------------

BASE_HTML = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mini Search Engine</title>
  <style>
    body{font-family:Inter, system-ui, -apple-system, Segoe UI, Roboto, 'Helvetica Neue', Arial; margin:0; padding:0; background:#f7fafc}
    header{background:#0b5ed7;color:white;padding:18px 28px}
    .container{max-width:960px;margin:28px auto;padding:18px;background:white;border-radius:12px;box-shadow:0 6px 24px rgba(12,18,32,0.06)}
    input[type=text]{width:100%;padding:12px 14px;border:1px solid #e2e8f0;border-radius:8px}
    .row{display:flex;gap:12px}
    .btn{background:#0b5ed7;color:white;padding:10px 14px;border:none;border-radius:8px;cursor:pointer}
    .meta{color:#6b7280;font-size:13px}
    a.result{display:block;padding:10px 0;border-bottom:1px solid #eef2f7}
  </style>
</head>
<body>
  <header>
    <h1 style="margin:0;font-size:20px">Mini Search Engine</h1>
  </header>
  <div class="container">
    {% block body %}{% endblock %}
  </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(BASE_HTML + '''
    {% block body %}
      <h2>Search</h2>
      <form action="/search" method="get">
        <input name="q" type="text" placeholder="Type keywords..." required>
        <div style="margin-top:12px"><button class="btn">Search</button></div>
      </form>

      <hr style="margin:20px 0">
      <h2>Crawl a site</h2>
      <form action="/crawl" method="post">
        <input name="start_url" type="text" placeholder="https://example.com" required>
        <div style="margin-top:8px">
          <label>Max pages: <input name="max_pages" type="number" value="30" min="1" style="width:80px"></label>
          <label style="margin-left:12px">Delay(s): <input name="delay" type="number" value="1" step="0.2" style="width:80px"></label>
        </div>
        <div style="margin-top:12px"><button class="btn">Start Crawl</button></div>
      </form>

    {% endblock %}
    ''')

@app.route('/crawl', methods=['POST'])
def crawl_route():
    start_url = request.form.get('start_url')
    max_pages = int(request.form.get('max_pages') or 30)
    delay = float(request.form.get('delay') or 1.0)

    # Run crawl in a separate thread so the web UI returns immediately
    thread = threading.Thread(target=crawl_domain, args=(start_url, max_pages, delay))
    thread.start()

    return render_template_string(BASE_HTML + '''
    {% block body %}
      <h2>Crawl started</h2>
      <p class="meta">Crawling <strong>{{start_url}}</strong> (max {{max_pages}} pages, delay {{delay}}s). The crawler runs in background. Refresh the page after a while and then search.</p>
      <p><a href="/">Back to home</a></p>
    {% endblock %}
    ''', start_url=start_url, max_pages=max_pages, delay=delay)

@app.route('/search')
def search_route():
    q = request.args.get('q','').strip()
    if not q:
        return redirect(url_for('index'))
    pages = load_pages()
    results = rank_results(q, pages)
    return render_template_string(BASE_HTML + '''
    {% block body %}
      <h2>Results for "{{q}}"</h2>
      <p class="meta">{{results|length}} results (showing top {{results|length}})</p>
      <div style="margin-top:12px">
        {% for r in results %}
          <a class="result" href="{{r.url}}" target="_blank">
            <strong>{{r.title or r.url}}</strong>
            <div class="meta">{{r.url}} &nbsp; — &nbsp; score: {{"{:.3f}".format(r.score)}}</div>
          </a>
        {% endfor %}
        {% if not results %}
          <p>No matches found.</p>
        {% endif %}
      </div>
      <p style="margin-top:18px"><a href="/">Back</a></p>
    {% endblock %}
    ''', q=q, results=results)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
