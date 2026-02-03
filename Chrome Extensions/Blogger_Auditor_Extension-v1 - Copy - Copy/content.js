function initExtension() {
    if (document.getElementById('audit-trigger-btn')) return;
    const btn = document.createElement('button');
    btn.id = 'audit-trigger-btn';
    btn.innerHTML = '🔍 Audit Links';
    btn.style = "position:fixed; bottom:25px; left:25px; z-index:999999; background:#fb8c00; color:white; border:none; padding:12px 25px; border-radius:50px; cursor:pointer; font-weight:bold; box-shadow:0 6px 20px rgba(0,0,0,0.3); border: 2px solid #fff; transition: 0.3s;";
    document.body.appendChild(btn);
    btn.onclick = runAuditor;
}

function runAuditor() {
    let oldPanel = document.getElementById('link-checker-pro-panel');
    if(oldPanel) oldPanel.remove();

    const panel = document.createElement('div');
    panel.id = 'link-checker-pro-panel';
    panel.style = 'position:fixed; top:15px; right:15px; width:400px; max-height:85vh; background:#ffffff; border:1px solid #ddd; z-index:2147483647; padding:0; overflow:hidden; box-shadow:0 20px 60px rgba(0,0,0,0.4); font-family:sans-serif; border-radius:20px; display:flex; flex-direction:column; animation: slideIn 0.3s ease;';
    
    panel.innerHTML = `
        <div style="background:#1a1a1a; color:white; padding:18px; display:flex; justify-content:space-between; align-items:center;">
            <b style="font-size:15px; letter-spacing:0.5px;">🛠️ Blogger Auditor Pro</b>
            <span id="close-checker" style="cursor:pointer; font-size:28px; line-height:1;">&times;</span>
        </div>
        <div id="summary-bar" style="background:#f8f9fa; padding:12px; font-size:12px; border-bottom:1px solid #eee; display:flex; justify-content:space-around; font-weight:bold;">
            <span>Total: <b id="stat-total" style="color:#333;">0</b></span>
            <span>📁 DL: <b id="stat-drive" style="color:#fb8c00;">0</b></span>
            <span>📄 PV: <b id="stat-pv" style="color:#2980b9;">0</b></span>
        </div>
        <div id="check-list" style="overflow-y:auto; flex-grow:1; padding:10px 0; background:#fff;">Scanning editor...</div>
    `;
    document.body.appendChild(panel);
    document.getElementById('close-checker').onclick = () => panel.remove();

    // Editor content extraction (including all iframes)
    let fullContent = document.body.innerHTML;
    document.querySelectorAll('iframe').forEach(f => {
        try { 
            if (f.contentWindow && f.contentWindow.document.body) {
                fullContent += f.contentWindow.document.body.innerHTML; 
            }
        } catch(e) { /* Handle Cross-Origin */ }
        fullContent += f.outerHTML; 
    });

    // Regex for all link types
    const driveRegex = /https:\/\/drive\.google\.com\/uc\?export=download(?:&amp;|&)id=([a-zA-Z0-9_-]+)/g;
    const previewRegex = /https:\/\/drive\.google\.com\/file\/d\/([a-zA-Z0-9_-]+)\/preview/g;
    const igRegex = /https?:\/\/(www\.)?instagram\.com\/([a-zA-Z0-9._-]+)\/?/g;
    const fbRegex = /https?:\/\/(www\.)?facebook\.com\/([a-zA-Z0-9._-]+)\/?/g;

    // Get all matches (allowing duplicates for correct counting)
    const dMatches = [...fullContent.matchAll(driveRegex)].map(m => m[1]);
    const pMatches = [...fullContent.matchAll(previewRegex)].map(m => m[1]);
    const igLinks = [...new Set([...fullContent.matchAll(igRegex)].map(m => m[0]))];
    const fbLinks = [...new Set([...fullContent.matchAll(fbRegex)].map(m => m[0]))];

    const list = document.getElementById('check-list');
    document.getElementById('stat-total').innerText = dMatches.length + pMatches.length + igLinks.length + fbLinks.length;
    document.getElementById('stat-drive').innerText = dMatches.length;
    document.getElementById('stat-pv').innerText = pMatches.length;

    if (dMatches.length + pMatches.length + igLinks.length + fbLinks.length === 0) {
        list.innerHTML = "<div style='text-align:center; padding:30px; color:#999;'>No links found. Switch to HTML View if needed.</div>";
        return;
    }
    list.innerHTML = '';

    function addItem(id, index, label, color, type) {
        const uniqueID = `st-${type}-${index}-${id.substring(0,5)}`;
        const item = document.createElement('div');
        item.style = `padding:14px; margin:10px 15px; border-radius:14px; background:#fbfbfb; border:1px solid #eee; border-left:6px solid ${color}; box-shadow: 0 4px 6px rgba(0,0,0,0.02);`;
        item.innerHTML = `
            <div style="font-size:10px; color:#888; font-weight:bold; text-transform:uppercase; margin-bottom:5px;">${label} #${index+1}</div>
            <div style="font-size:12px; margin-bottom:8px; word-break:break-all; color:#444;">ID: <code>${id}</code></div>
            <div id="${uniqueID}" style="font-weight:bold; font-size:13px; color:#f39c12;">⏳ Verifying...</div>
        `;
        list.appendChild(item);

        const img = new Image();
        img.src = `https://drive.google.com/thumbnail?id=${id}&sz=w200`;
        img.onload = () => { 
            const el = document.getElementById(uniqueID);
            if(el) { el.innerText = "✅ Active"; el.style.color = "green"; }
        };
        img.onerror = () => { 
            const el = document.getElementById(uniqueID);
            if(el) { el.innerText = "❌ Dead / Private / Error"; el.style.color = "red"; }
        };
    }

    // Add items to list
    dMatches.forEach((id, i) => addItem(id, i, "📥 Download Link", "#fb8c00", "dl"));
    pMatches.forEach((id, i) => addItem(id, i, "📄 PDF Preview", "#2980b9", "pv"));
    
    igLinks.forEach((l, i) => {
        const u = l.split('instagram.com/')[1].replace('/','');
        const item = document.createElement('div');
        item.style = "padding:14px; margin:10px 15px; border-radius:14px; background:#fbfbfb; border-left:6px solid #e1306c;";
        item.innerHTML = `<b>📸 INSTAGRAM</b><br><span style="font-size:13px;">@${u}</span><br><a href="${l}" target="_blank" style="color:#e1306c; text-decoration:none; font-size:11px; font-weight:bold; display:inline-block; margin-top:5px;">Verify Profile ↗</a>`;
        list.appendChild(item);
    });

    fbLinks.forEach((l, i) => {
        const u = l.split('facebook.com/')[1].replace('/','');
        const item = document.createElement('div');
        item.style = "padding:14px; margin:10px 15px; border-radius:14px; background:#fbfbfb; border-left:6px solid #0766ff;";
        item.innerHTML = `<b>👤 FACEBOOK</b><br><span style="font-size:13px;">${u}</span><br><a href="${l}" target="_blank" style="color:#0766ff; text-decoration:none; font-size:11px; font-weight:bold; display:inline-block; margin-top:5px;">Verify Page ↗</a>`;
        list.appendChild(item);
    });
}

// Global CSS for animation
const style = document.createElement('style');
style.innerHTML = `@keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }`;
document.head.appendChild(style);

setInterval(initExtension, 2000);