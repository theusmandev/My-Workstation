import pandas as pd
import json
import os
import re

# --- 1. INPUT FILE PATH ---
input_csv_path = r"C:\Users\PCS\Downloads\urdunovelbanks_image_urls.csv"

# --- 2. OUTPUT FILE PATH ---
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
output_file_path = os.path.join(downloads_path, "blogger_optimized_code.txt")

print(f"Reading CSV from: {input_csv_path} ...")

# --- 3. LOAD CSV ---
try:
    df = pd.read_csv(input_csv_path, encoding='cp1252')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(input_csv_path, encoding='latin1')
    except:
        print("Error: Encoding issue. CSV check karein.")
        exit()
except FileNotFoundError:
    print("Error: File nahi mili.")
    exit()

# --- 4. IMAGE OPTIMIZER FUNCTION (Critical for LCP/Lightweight) ---
def optimize_google_url(url):
    if not isinstance(url, str): return ""
    url = url.strip()
    
    # Agar ye Google/Blogger ki image hai to isay WebP aur Fixed Size ma convert kro
    # Pattern: /s1600/, /s320/, =s1600 etc ko replace karega
    if 'blogger.googleusercontent.com' in url or 'bp.blogspot.com' in url:
        # Check if URL has standard slash pattern like /s1600/
        if re.search(r'\/s\d+.*\/', url):
            return re.sub(r'\/s\d+.*\/', '/w300-h450-c-rw/', url) # -rw means WebP (Super Fast)
        # Check if URL has equals pattern like =s1600
        elif re.search(r'=s\d+', url):
            return re.sub(r'=s\d+.*', '=w300-h450-c-rw', url)
            
    return url

# --- 5. PREPARE DATA ---
novels_list = []
for index, row in df.iterrows():
    try:
        original_img = str(row['Image URL'])
        optimized_img = optimize_google_url(original_img)
        
        novel = {
            "title": str(row['Title']).strip(),
            "link": str(row['Post URL']).strip(),
            "img": optimized_img
        }
        novels_list.append(novel)
    except KeyError:
        continue

# JSON Data for JS
json_data = json.dumps(novels_list, ensure_ascii=False)

# --- 6. OPTIMIZED HTML TEMPLATE ---
html_template = r"""<style>
/* --- CONTAINER --- */
.novels-box { 
    margin-top: 20px; border-top: 1px solid #eee; padding-top: 20px; 
    contain: content; /* Helps browser render faster */
}
.novels-head { font-size: 18px; font-weight: bold; color: #333; margin-bottom: 15px; border-left: 4px solid #e74c3c; padding-left: 10px; text-transform: uppercase; }

/* --- GRID --- */
.novels-grid {
    display: grid; 
    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); 
    gap: 10px;
    min-height: 300px;
    content-visibility: auto; /* Advanced Optimization */
}

/* --- CARD --- */
.novel-card { 
    background: #fff; border: 1px solid #ddd; border-radius: 5px; overflow: hidden; 
    text-decoration: none; display: flex; flex-direction: column; 
    position: relative; 
    contain-intrinsic-size: 100px 180px; /* Fix for CLS */
    transition: transform 0.2s ease;
}
.novel-card:hover { transform: translateY(-3px); box-shadow: 0 4px 8px rgba(0,0,0,0.1); }

/* --- IMAGE (CLS FIX) --- */
.novel-card img {
    width: 100%; 
    height: auto;
    aspect-ratio: 2 / 3; /* Browser knows space beforehand */
    object-fit: cover; 
    display: block; 
    background: #f0f0f0;
}

/* --- TITLE --- */
.novel-title { 
    padding: 6px 4px; font-size: 11px; font-weight: 700; color: #333; 
    text-align: center; line-height: 1.3;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
    height: 30px; 
}

/* --- BUTTONS --- */
.load-more-area { text-align: center; margin-top: 20px; width: 100%; display: none; }
.load-btn {
    background: #e74c3c; color: white; border: none; padding: 12px 40px;
    font-size: 14px; font-weight: bold; cursor: pointer; border-radius: 50px;
}
.end-msg {
    text-align: center; margin-top: 20px; padding: 10px; font-weight: bold; 
    font-size: 13px; color: #e74c3c; display: none;
}
</style>

<div class="novels-box">
  <div class="novels-head">Writers Novels Library</div>
  
  <div class="novels-grid" id="libGrid">
    </div>

  <div class="load-more-area" id="libBtnArea">
    <button class="load-btn" onclick="renderNextBatch()">Load More Novels</button>
  </div>
  <div class="end-msg" id="libEndMsg">All novels loaded. Keep in touch!</div>
</div>

<script>
// --- STATIC DATA ---
var staticNovels = __DATA_HERE__;

var renderedCount = 0;
var batchSize = 30; 
var grid = document.getElementById("libGrid");

// Initialize immediately
(function initLibrary() {
    // Sort A-Z
    staticNovels.sort(function(a, b) {
        return a.title.localeCompare(b.title);
    });
    renderNextBatch();
})();

function renderNextBatch() {
    var fragment = document.createDocumentFragment(); // Faster DOM insertion
    
    var limit = renderedCount + batchSize;
    if (limit > staticNovels.length) limit = staticNovels.length;

    for (var i = renderedCount; i < limit; i++) {
        var post = staticNovels[i];
        
        // --- LCP OPTIMIZATION ---
        // First 4 images get High Priority + Eager Loading
        // Remaining get Lazy Loading + Async Decoding
        var isLCP = (i < 4);
        var loadAttr = isLCP ? 'loading="eager" fetchpriority="high"' : 'loading="lazy" decoding="async"';
        
        var safeTitle = post.title.replace(/"/g, '&quot;');

        var linkEl = document.createElement('a');
        linkEl.className = 'novel-card';
        linkEl.href = post.link;
        linkEl.title = safeTitle;

        // Using standard HTML string for inner content is faster here
        linkEl.innerHTML = `
            <img src="${post.img}" ${loadAttr} alt="${safeTitle}" width="300" height="450">
            <div class="novel-title">${post.title}</div>
        `;
        
        fragment.appendChild(linkEl);
    }

    grid.appendChild(fragment);
    renderedCount = limit;
    
    // UI Update
    var btn = document.getElementById("libBtnArea");
    var msg = document.getElementById("libEndMsg");
    
    if (renderedCount >= staticNovels.length) {
        if(btn) btn.style.display = 'none';
        if(msg) msg.style.display = 'block';
    } else {
        if(btn) btn.style.display = 'block';
        if(msg) msg.style.display = 'none';
    }
}
</script>
"""

# --- 7. MERGE & SAVE ---
final_html = html_template.replace('__DATA_HERE__', json_data)

with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("--------------------------------------------------")
print("OPTIMIZED CODE GENERATED SUCCESSFULLY!")
print(f"File Location: {output_file_path}")
print("Features: CLS Fixed (Size Attributes), LCP Optimized (WebP + FetchPriority)")
print("--------------------------------------------------")