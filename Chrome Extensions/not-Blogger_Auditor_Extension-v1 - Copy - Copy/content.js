// Function to create the button
function injectAuditButton() {
    // Sirf edit page par button dikhana hai
    if (!window.location.href.includes('/post/edit/')) {
        const existingBtn = document.getElementById('audit-trigger-btn');
        if (existingBtn) existingBtn.remove();
        return;
    }

    if (document.getElementById('audit-trigger-btn')) return;

    const btn = document.createElement('button');
    btn.id = 'audit-trigger-btn';
    btn.innerHTML = '🔍 Audit Links';
    btn.style = "position:fixed; bottom:25px; left:25px; z-index:2147483647; background:#fb8c00; color:white; border:none; padding:12px 25px; border-radius:50px; cursor:pointer; font-weight:bold; box-shadow:0 6px 20px rgba(0,0,0,0.3); border: 2px solid #fff; transition: 0.3s;";
    
    // Hover effect
    btn.onmouseover = () => btn.style.transform = "scale(1.05)";
    btn.onmouseout = () => btn.style.transform = "scale(1)";
    
    document.body.appendChild(btn);
    btn.onclick = runAuditor;
}

// Auditor Logic (Same as V8)
function runAuditor() {
    let oldPanel = document.getElementById('link-checker-pro-panel');
    if(oldPanel) oldPanel.remove();

    const panel = document.createElement('div');
    panel.id = 'link-checker-pro-panel';
    panel.style = 'position:fixed; top:15px; right:15px; width:400px; max-height:85vh; background:#ffffff; border:1px solid #ddd; z-index:2147483647; padding:0; overflow:hidden; box-shadow:0 20px 60px rgba(0,0,0,0.4); font-family:sans-serif; border-radius:20px; display:flex; flex-direction:column;';
    
    panel.innerHTML = `
        <div style="background:#1a1a1a; color:white; padding:18px; display:flex; justify-content:space-between; align-items:center;">
            <b style="font-size:15px;">🛠️ Blogger Auditor Pro</b>
            <span id="close-checker" style="cursor:pointer; font-size:28px; line-height:1;">&times;</span>
        </div>
        <div id="summary-bar" style="background:#f8f9fa; padding:12px; font-size:12px; border-bottom:1px solid #eee; display:flex; justify-content:space-around; font-weight:bold;">
            <span>Total: <b id="stat-total">0</b></span>
            <span>📁 DL: <b id="stat-drive">0</b></span>
            <span>📄 PV: <b id="stat-pv">0</b></span>
        </div>
        <div id="check-list" style="overflow-y:auto; flex-grow:1; padding:10px 0; background:#fff;">Scanning...</div>
    `;
    document.body.appendChild(panel);
    document.getElementById('close-checker').onclick = () => panel.remove();

    let fullContent = document.body.innerHTML;
    document.querySelectorAll('iframe').forEach(f => {
        try { if(f.contentWindow.document.body) fullContent += f.contentWindow.document.body.innerHTML; } catch(e){}
        fullContent += f.outerHTML; 
    });

    const driveRegex = /https:\/\/drive\.google\.com\/uc\?export=download(?:&amp;|&)id=([a-zA-Z0-9_-]+)/g;
    const previewRegex = /https:\/\/drive\.google\.com\/file\/d\/([a-zA-Z0-9_-]+)\/preview/g;
    const igRegex = /https?:\/\/(www\.)?instagram\.com\/([a-zA-Z0-9._-]+)\/?/g;
    const fbRegex = /https?:\/\/(www\.)?facebook\.com\/([a-zA-Z0-9._-]+)\/?/g;

    const dM = [...fullContent.matchAll(driveRegex)].map(m => m[1]);
    const pM = [...fullContent.matchAll(previewRegex)].map(m => m[1]);
    const igL = [...new Set([...fullContent.matchAll(igRegex)].map(m => m[0]))];
    const fbL = [...new Set([...fullContent.matchAll(fbRegex)].map(m => m[0]))];

    const list = document.getElementById('check-list');
    document.getElementById('stat-total').innerText = dM.length + pM.length + igL.length + fbL.length;
    document.getElementById('stat-drive').innerText = dM.length;
    document.getElementById('stat-pv').innerText = pM.length;

    if (dM.length + pM.length + igL.length + fbL.length === 0) {
        list.innerHTML = "<div style='text-align:center; padding:30px; color:#999;'>No links found.</div>";
        return;
    }
    list.innerHTML = '';

    function addItem(id, index, label, color, type) {
        const uniqueID = `st-${type}-${index}-${id.substring(0,5)}`;
        const item = document.createElement('div');
        item.style = `padding:14px; margin:10px 15px; border-radius:14px; background:#fbfbfb; border:1px solid #eee; border-left:6px solid ${color}; box-shadow: 0 4px 6px rgba(0,0,0,0.02);`;
        item.innerHTML = `<b>${label} #${index+1}</b><br><small style="word-break:break-all; color:#666;">ID: ${id}</small><br><b id="${uniqueID}" style="color:orange; font-size:13px;">⏳ Verifying...</b>`;
        list.appendChild(item);

        const img = new Image();
        img.src = `https://drive.google.com/thumbnail?id=${id}&sz=w200`;
        img.onload = () => { const el = document.getElementById(uniqueID); if(el) { el.innerText="✅ Active"; el.style.color="green"; } };
        img.onerror = () => { const el = document.getElementById(uniqueID); if(el) { el.innerText="❌ Dead/Private"; el.style.color="red"; } };
    }

    dM.forEach((id, i) => addItem(id, i, "📥 Download", "#fb8c00", "dl"));
    pM.forEach((id, i) => addItem(id, i, "📄 Preview", "#2980b9", "pv"));
    
    // Social links adding logic...
    igL.forEach(l => {
        const item = document.createElement('div');
        item.style = "padding:12px; margin:8px 15px; border-radius:12px; background:#f9f9f9; border-left:5px solid #e1306c;";
        item.innerHTML = `<b>📸 INSTAGRAM</b><br><a href="${l}" target="_blank" style="color:#e1306c; text-decoration:none; font-size:11px; font-weight:bold;">Verify ↗</a>`;
        list.appendChild(item);
    });
}

// INSTANT MONITORING: This watches for any page changes
const observer = new MutationObserver(() => {
    injectAuditButton();
});

// Start observing the page
observer.observe(document.documentElement, { childList: true, subtree: true });

// Initial check
injectAuditButton();