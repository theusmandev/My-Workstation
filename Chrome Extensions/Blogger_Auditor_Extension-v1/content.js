function initExtension() {
    if (document.getElementById('audit-trigger-btn')) return;

    const btn = document.createElement('button');
    btn.id = 'audit-trigger-btn';
    btn.innerHTML = '🔍 Audit Links';
    btn.style = "position:fixed; bottom:20px; left:20px; z-index:999999; background:#fb8c00; color:white; border:none; padding:12px 25px; border-radius:50px; cursor:pointer; font-weight:bold; box-shadow:0 4px 15px rgba(0,0,0,0.3); border: 2px solid white;";
    document.body.appendChild(btn);

    btn.onclick = runAuditor;
}

function runAuditor() {
    let oldPanel = document.getElementById('link-checker-v8');
    if(oldPanel) oldPanel.remove();

    const panel = document.createElement('div');
    panel.id = 'link-checker-v8';
    panel.style = 'position:fixed; top:15px; right:15px; width:390px; max-height:85vh; background:#ffffff; border:1px solid #e0e0e0; z-index:2147483647; padding:0; overflow:hidden; box-shadow:0 15px 50px rgba(0,0,0,0.3); font-family:sans-serif; border-radius:16px; display:flex; flex-direction:column;';
    
    panel.innerHTML = `
        <div style="background:#1a1a1a; color:white; padding:16px; display:flex; justify-content:space-between; align-items:center;">
            <b style="font-size:14px;">🛠️ Blogger Auditor Extension</b>
            <span id="close-checker" style="cursor:pointer; font-size:24px; line-height:1;">&times;</span>
        </div>
        <div id="summary-bar" style="background:#f4f4f4; padding:10px; font-size:11px; border-bottom:1px solid #ddd; display:flex; justify-content:space-around;">
            <span>Total: <b id="stat-total">0</b></span>
            <span>📁 DL: <b id="stat-drive">0</b></span>
            <span>📄 PV: <b id="stat-pv">0</b></span>
        </div>
        <div id="check-list" style="overflow-y:auto; flex-grow:1; padding:10px; background:#fff; font-size:12px;">Scanning...</div>
    `;
    document.body.appendChild(panel);
    document.getElementById('close-checker').onclick = () => panel.remove();

    // Editor aur uske iframes se content nikalne ka tareeka
    let fullContent = document.body.innerHTML;
    document.querySelectorAll('iframe').forEach(f => {
        try { fullContent += f.contentWindow.document.body.innerHTML + f.outerHTML; } catch(e) { fullContent += f.outerHTML; }
    });

    // Regex Definitions
    const driveRegex = /https:\/\/drive\.google\.com\/uc\?export=download(?:&amp;|&)id=([a-zA-Z0-9_-]+)/g;
    const previewRegex = /https:\/\/drive\.google\.com\/file\/d\/([a-zA-Z0-9_-]+)\/preview/g;
    const igRegex = /https?:\/\/(www\.)?instagram\.com\/([a-zA-Z0-9._-]+)\/?/g;
    const fbRegex = /https?:\/\/(www\.)?facebook\.com\/([a-zA-Z0-9._-]+)\/?/g;

    const dL = [...new Set([...fullContent.matchAll(driveRegex)].map(m => m[1]))];
    const pL = [...new Set([...fullContent.matchAll(previewRegex)].map(m => m[1]))];
    const igL = [...new Set([...fullContent.matchAll(igRegex)].map(m => m[0]))];
    const fbL = [...new Set([...fullContent.matchAll(fbRegex)].map(m => m[0]))];

    const list = document.getElementById('check-list');
    document.getElementById('stat-total').innerText = dL.length + pL.length + igL.length + fbL.length;
    document.getElementById('stat-drive').innerText = dL.length;
    document.getElementById('stat-pv').innerText = pL.length;

    if (dL.length === 0 && pL.length === 0 && igL.length === 0 && fbL.length === 0) {
        list.innerHTML = "<div style='text-align:center; padding:20px; color:#999;'>No links detected. Make sure you are in 'HTML View'.</div>";
        return;
    }
    list.innerHTML = '';

    function addItem(id, label, color) {
        const item = document.createElement('div');
        item.style = `padding:10px; margin-bottom:8px; border-radius:8px; background:#f9f9f9; border-left:5px solid ${color};`;
        item.innerHTML = `<b>${label}</b><br><small style="word-break:break-all;">${id}</small><br><b id="st-${id}" style="color:orange;">Checking...</b>`;
        list.appendChild(item);

        const img = new Image();
        img.src = `https://drive.google.com/thumbnail?id=${id}&sz=w200`;
        img.onload = () => { document.getElementById(`st-${id}`).innerText = "✅ Active"; document.getElementById(`st-${id}`).style.color = "green"; };
        img.onerror = () => { document.getElementById(`st-${id}`).innerText = "❌ Broken / Private"; document.getElementById(`st-${id}`).style.color = "red"; };
    }

    dL.forEach(id => addItem(id, "📥 DOWNLOAD LINK", "#fb8c00"));
    pL.forEach(id => addItem(id, "📄 PDF PREVIEW", "#2980b9"));
    
    // Social links list mein add karein
    igL.forEach(l => {
        const item = document.createElement('div');
        item.style = "padding:10px; margin-bottom:8px; border-radius:8px; background:#f9f9f9; border-left:5px solid #e1306c;";
        item.innerHTML = `<b>📸 INSTAGRAM</b><br><a href="${l}" target="_blank" style="color:#e1306c; text-decoration:none; font-size:11px;">Verify Profile ↗</a>`;
        list.appendChild(item);
    });
}

// Har 2 second baad check karein ke button mojud hai ya nahi
setInterval(initExtension, 2000);