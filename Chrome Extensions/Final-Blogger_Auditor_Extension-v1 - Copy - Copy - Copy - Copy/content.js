// 1. Extension Initialization
function initExtension() {
    const isEditor = window.location.href.includes('/blog/post/edit/');
    const existingBtn = document.getElementById('audit-trigger-btn');

    if (isEditor && !existingBtn) {
        const btn = document.createElement('button');
        btn.id = 'audit-trigger-btn';
        btn.innerHTML = '🔍 Audit Current Post';
        btn.style = "position:fixed; bottom:20px; left:20px; z-index:999999; background:#fb8c00; color:white; border:none; padding:12px 25px; border-radius:50px; cursor:pointer; font-weight:bold; box-shadow:0 4px 15px rgba(0,0,0,0.3); border: 2px solid white;";
        
        document.body.appendChild(btn);
        btn.onclick = runAuditor;
    } 
    else if (!isEditor && existingBtn) {
        existingBtn.remove();
        const panel = document.getElementById('link-checker-pro-panel');
        if(panel) panel.remove();
    }
}

// 2. Main Auditor Logic
function runAuditor() {
    // Purana panel agar koi hai to foran khatam karein
    const oldPanel = document.getElementById('link-checker-pro-panel');
    if(oldPanel) oldPanel.remove();

    // Data containers ko empty reset karein
    let dL = [], pL = [], igL = [], fbL = [];
    let editorContent = "";

    // --- CRITICAL FIX: SIRF ACTIVE EDITOR KO TARGET KARNA ---
    // Blogger ke editor ka content hamesha aik specific iframe mein hota hai
    const iframes = document.querySelectorAll('iframe.editable');
    
    iframes.forEach(iframe => {
        try {
            // Sirf wahi iframe scan karein jo screen par nazar aa raha hai (Visible)
            if (iframe.offsetWidth > 0 && iframe.offsetHeight > 0) {
                editorContent += iframe.contentWindow.document.body.innerHTML;
            }
        } catch(e) {
            console.warn("Iframe scan skipped due to security/loading: ", e);
        }
    });

    // Agar iframe na mile (kabhi kabhi Blogger HTML view mein hota hai)
    if (!editorContent) {
        const aceEditor = document.querySelector('.ace_content'); // HTML View editor
        if (aceEditor) {
            editorContent = aceEditor.innerText;
        }
    }

    // 3. UI Panel Create Karein
    const panel = document.createElement('div');
    panel.id = 'link-checker-pro-panel';
    panel.style = 'position:fixed; top:15px; right:15px; width:390px; max-height:85vh; background:#ffffff; border:1px solid #e0e0e0; z-index:2147483647; padding:0; overflow:hidden; box-shadow:0 15px 50px rgba(0,0,0,0.3); font-family:sans-serif; border-radius:16px; display:flex; flex-direction:column;';
    
    panel.innerHTML = `
        <div style="background:#1a1a1a; color:white; padding:16px; display:flex; justify-content:space-between; align-items:center;">
            <b style="font-size:14px;">🛠️ Blogger Auditor Pro</b>
            <span id="close-checker" style="cursor:pointer; font-size:24px; line-height:1;">&times;</span>
        </div>
        <div id="summary-bar" style="background:#f4f4f4; padding:10px; font-size:11px; border-bottom:1px solid #ddd; display:flex; justify-content:space-around;">
            <span>Total: <b id="stat-total">0</b></span>
            <span>📁 DL: <b id="stat-drive">0</b></span>
            <span>📄 PV: <b id="stat-pv">0</b></span>
        </div>
        <div id="check-list" style="overflow-y:auto; flex-grow:1; padding:10px 0; background:#fff;">Scanning...</div>
    `;
    document.body.appendChild(panel);
    document.getElementById('close-checker').onclick = () => panel.remove();

    // 4. Regex Scanning (Sirf Editor Content Par)
    const driveRegex = /https:\/\/drive\.google\.com\/uc\?export=download(?:&amp;|&)id=([a-zA-Z0-9_-]+)/g;
    const previewRegex = /https:\/\/drive\.google\.com\/file\/d\/([a-zA-Z0-9_-]+)\/preview/g;
    const igRegex = /https?:\/\/(www\.)?instagram\.com\/([a-zA-Z0-9._-]+)\/?/g;
    const fbRegex = /https?:\/\/(www\.)?facebook\.com\/([a-zA-Z0-9._-]+)\/?/g;

    dL = [...new Set([...editorContent.matchAll(driveRegex)].map(m => m[1]))];
    pL = [...new Set([...editorContent.matchAll(previewRegex)].map(m => m[1]))];
    igL = [...new Set([...editorContent.matchAll(igRegex)].map(m => m[0]))];
    fbL = [...new Set([...editorContent.matchAll(fbRegex)].map(m => m[0]))];

    const list = document.getElementById('check-list');
    document.getElementById('stat-total').innerText = dL.length + pL.length + igL.length + fbL.length;
    document.getElementById('stat-drive').innerText = dL.length;
    document.getElementById('stat-pv').innerText = pL.length;

    if (dL.length + pL.length + igL.length + fbL.length === 0) {
        list.innerHTML = "<div style='text-align:center; padding:20px; color:#999;'>No links found in current post.</div>";
        return;
    }
    list.innerHTML = '';

    // 5. Result Display
    function addItem(id, type, label, color) {
        const uniqueKey = type + '-' + id.replace(/[^a-z0-9]/gi, '');
        const item = document.createElement('div');
        item.style = `padding:12px; margin:8px 12px; border-radius:12px; background:#f9f9f9; border-left:5px solid ${color}; box-shadow: 0 2px 5px rgba(0,0,0,0.05);`;
        item.innerHTML = `<b>${label}</b><br><small style="word-break:break-all; color:#666;">${id}</small><br><b id="st-${uniqueKey}" style="color:orange; font-size:13px;">Checking...</b>`;
        list.appendChild(item);

        const img = new Image();
        img.src = `https://drive.google.com/thumbnail?id=${id}&sz=w200`;
        img.onload = () => { 
            const el = document.getElementById(`st-${uniqueKey}`);
            if(el) { el.innerText = "✅ Active"; el.style.color = "green"; }
        };
        img.onerror = () => { 
            const el = document.getElementById(`st-${uniqueKey}`);
            if(el) { el.innerText = "❌ Dead / Private"; el.style.color = "red"; }
        };
    }

    dL.forEach(id => addItem(id, "dl", "📥 DOWNLOAD LINK", "#fb8c00"));
    pL.forEach(id => addItem(id, "pv", "📄 PDF PREVIEW", "#2980b9"));
    igL.forEach(l => {
        const u = l.split('instagram.com/')[1].replace('/','');
        const item = document.createElement('div');
        item.style = "padding:12px; margin:8px 12px; border-radius:12px; background:#f9f9f9; border-left:5px solid #e1306c;";
        item.innerHTML = `<b>📸 INSTAGRAM</b><br>@${u}<br><a href="${l}" target="_blank" style="color:#e1306c; text-decoration:none; font-size:11px; font-weight:bold;">Verify Profile ↗</a>`;
        list.appendChild(item);
    });
    fbL.forEach(l => {
        const u = l.split('facebook.com/')[1].replace('/','');
        const item = document.createElement('div');
        item.style = "padding:12px; margin:8px 12px; border-radius:12px; background:#f9f9f9; border-left:5px solid #0766ff;";
        item.innerHTML = `<b>👤 FACEBOOK</b><br>${u}<br><a href="${l}" target="_blank" style="color:#0766ff; text-decoration:none; font-size:11px; font-weight:bold;">Verify Page ↗</a>`;
        list.appendChild(item);
    });
}

// 6. Observer for SPA Navigation
setInterval(initExtension, 1000);