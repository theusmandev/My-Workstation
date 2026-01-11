import pandas as pd
import json
import os

# --- 1. INPUT FILE PATH ---
# آپ کا دیا ہوا ایڈریس (Raw string 'r' کے ساتھ)
input_csv_path = r"C:\Users\PCS\Downloads\urdunovelbanks_image_urls.csv"

# --- 2. OUTPUT FILE PATH ---
# یہ کوڈ خودکار طریقے سے آپ کے Downloads فولڈر میں فائل محفوظ کرے گا
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
output_txt_path = os.path.join(downloads_folder, "blogger_final_code.txt")

print(f"Reading file from: {input_csv_path}")

# --- 3. READING CSV (Fixed Encoding) ---
try:
    # 'cp1252' ونڈوز کی فائلوں کے لیے بہتر ہے
    df = pd.read_csv(input_csv_path, encoding='cp1252')
except UnicodeDecodeError:
    # اگر وہ بھی نہ چلے تو 'latin1' ٹرائی کریں
    df = pd.read_csv(input_csv_path, encoding='latin1')
except FileNotFoundError:
    print("Error: File not found. Please check the path.")
    exit()

# --- 4. PREPARING DATA ---
novels_list = []
for index, row in df.iterrows():
    novel = {
        "title": str(row['Title']).strip(),
        "link": str(row['Post URL']).strip(),
        "img": str(row['Image URL']).strip()
    }
    novels_list.append(novel)

json_data = json.dumps(novels_list, ensure_ascii=False, indent=2)

# --- 5. HTML TEMPLATE (Fixed Syntax Warning using r"") ---
html_template = r"""<style>
/* --- CONTAINER --- */
.novels-box { 
    margin-top: 20px; border-top: 1px solid #eee; padding-top: 20px; 
    contain: content; 
}
.novels-head { font-size: 18px; font-weight: bold; color: #333; margin-bottom: 15px; border-left: 4px solid #e74c3c; padding-left: 10px; text-transform: uppercase; }

/* --- GRID --- */
.novels-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); gap: 10px;
    min-height: 300px;
}

/* --- CARD --- */
.novel-card { 
    background: #fff; border: 1px solid #ddd; border-radius: 5px; overflow: hidden; 
    text-decoration: none; display: flex; flex-direction: column; 
    position: relative; content-visibility: auto; contain-intrinsic-size: 100px 180px;
    transition: transform 0.2s ease;
}
.novel-card:hover { transform: translateY(-3px); box-shadow: 0 4px 8px rgba(0,0,0,0.1); }

/* --- IMAGE --- */
.novel-card img {
    width: 100%; aspect-ratio: 2 / 3; object-fit: cover; display: block; background: #f0f0f0;
}

/* --- TITLE --- */
.novel-title { 
    padding: 6px 4px; font-size: 11px; font-weight: 700; color: #333; 
    text-align: center; line-height: 1.3;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
    height: 30px; 
}

/* --- BUTTONS & STATUS --- */
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
    <div class="novel-card"><div class="skeleton"></div></div>
    <div class="novel-card"><div class="skeleton"></div></div>
    <div class="novel-card"><div class="skeleton"></div></div>
  </div>

  <div class="load-more-area" id="libBtnArea">
    <button class="load-btn" onclick="renderNextBatch()">Load More Novels</button>
  </div>
  <div class="end-msg" id="libEndMsg">All novels loaded. Keep in touch!</div>
</div>

<script>
// STATIC DATA
var staticNovels = __DATA_HERE__;

var renderedCount = 0;
var batchSize = 30; 

function initStaticLibrary() {
    var grid = document.getElementById("libGrid");
    grid.innerHTML = "";
    
    // Sort A-Z
    staticNovels.sort(function(a, b) {
        var x = a.title.toLowerCase();
        var y = b.title.toLowerCase();
        return x < y ? -1 : x > y ? 1 : 0;
    });

    renderNextBatch();
}

function renderNextBatch() {
    var grid = document.getElementById("libGrid");
    var html = "";
    
    var limit = renderedCount + batchSize;
    if (limit > staticNovels.length) limit = staticNovels.length;

    for (var i = renderedCount; i < limit; i++) {
        var post = staticNovels[i];
        
        var imgUrl = post.img;
        if(imgUrl.includes('/s1600/') || imgUrl.includes('/s1200/') || imgUrl.includes('/s1000/')) {
             imgUrl = imgUrl.replace(/\/s[0-9]+.*?\//, "/w300-h450-c/");
        } else if (imgUrl.includes('=s')) {
             imgUrl = imgUrl.replace(/=s[0-9]+/, "=w300-h450-c");
        }

        var loadAttr = (i < 6) ? 'loading="eager"' : 'loading="lazy"';
        var safeTitle = post.title.replace(/"/g, '&quot;');

        html += '<a href="' + post.link + '" class="novel-card" title="' + safeTitle + '">';
        html += '<img src="' + imgUrl + '" ' + loadAttr + ' alt="' + safeTitle + '" width="300" height="450">';
        html += '<div class="novel-title">' + post.title + '</div>';
        html += '</a>';
    }

    var div = document.createElement('div');
    div.innerHTML = html;
    while (div.firstChild) {
        grid.appendChild(div.firstChild);
    }

    renderedCount = limit;
    
    var btn = document.getElementById("libBtnArea");
    var msg = document.getElementById("libEndMsg");
    
    if (renderedCount >= staticNovels.length) {
        btn.style.display = 'none';
        msg.style.display = 'block';
    } else {
        btn.style.display = 'block';
        msg.style.display = 'none';
    }
}

initStaticLibrary();
</script>
"""

# --- 6. MERGING AND SAVING ---
final_html = html_template.replace('__DATA_HERE__', json_data)

with open(output_txt_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Success! Output saved to: {output_txt_path}")