function initExtension() {
    const isEditor = window.location.href.includes('/blog/post/edit/');
    const existingBtn = document.getElementById('audit-trigger-btn');

    if (isEditor && !existingBtn) {
        const btn = document.createElement('button');
        btn.id = 'audit-trigger-btn';
        btn.innerHTML = '🔍 Audit Links Order';
        btn.style = "position:fixed; bottom:20px; left:20px; z-index:999999; background:#fb8c00; color:white; border:none; padding:12px 25px; border-radius:50px; cursor:pointer; font-weight:bold; box-shadow:0 4px 15px rgba(0,0,0,0.3); border: 2px solid white;";
        
        document.body.appendChild(btn);
        btn.onclick = runAuditor;
    } 
    else if (!isEditor && existingBtn) {
        existingBtn.remove();
        cleanupOldResults();
    }
}

function cleanupOldResults() {
    const panel = document.getElementById('link-checker-pro-panel');
    if (panel) panel.remove();
}

function runAuditor() {
    cleanupOldResults();

    // 1. Editor ka content uthayen (Sirf active wala)
    let editorHTML = "";
    const iframes = document.querySelectorAll('iframe.editable');
    iframes.forEach(iframe => {
        if (iframe.offsetWidth > 0 && iframe.offsetHeight > 0) {
            try { editorHTML = iframe.contentWindow.document.body.innerHTML; } catch(e) {}
        }
    });

    // Agar iframe na mile to main body scan karein (exclude panel)
    if (!editorHTML) {
        editorHTML = document.body.innerHTML.split('id="audit-trigger-btn"')[0];
    }

    // 2. Regex Patterns
    const patterns = [
        { type: 'dl', label: '📥 DOWNLOAD', color: '#fb8c00', regex: /https:\/\/drive\.google\.com\/uc\?export=download(?:&amp;|&)id=([a-zA-Z0-9_-]+)/g },
        { type: 'pv', label: '📄 PREVIEW', color: '#2980b9', regex: /https:\/\/drive\.google\.com\/file\/d\/([a-zA-Z0-9_-]+)\/preview/g },
        { type: 'ig', label: '📸 INSTAGRAM', color: '#e1306c', regex: /https?:\/\/(www\.)?instagram\.com\/([a-zA-Z0-9._-]+)\/?/g },
        { type: 'fb', label: '👤 FACEBOOK', color: '#0766ff', regex: /https?:\/\/(www\.)?facebook\.com\/([a-zA-Z0-9._-]+)\/?/g }
    ];

    let allMatches = [];

    // 3. Saare links dhoondein aur unki "Position" (index) yaad rakhein
    patterns.forEach(p => {
        let match;
        while ((match = p.regex.exec(editorHTML)) !== null) {
            allMatches.push({
                type: p.type,
                label: p.label,
                color: p.color,
                id: p.type === 'ig' || p.type === 'fb' ? match[0] : match[1],
                index: match.index // Page mein kahan par hai
            });
        }
    });

    // 4. Sort by Index (Top to Bottom)
    allMatches.sort((a, b) => a.index - b.index);

    // 5. UI Create Karein
    const panel = document.createElement('div');
    panel.id = 'link-checker-pro-panel';
    panel.style = 'position:fixed; top:15px; right:15px; width:390px; max-height:85vh; background:#ffffff; border:1px solid #e0e0e0; z-index:2147483647; padding:0; overflow:hidden; box-shadow:0 15px 50px rgba(0,0,0,0.3); font-family:sans-serif; border-radius:16px; display:flex; flex-direction:column;';
    
    panel.innerHTML = `
        <div style="background:#1a1a1a; color:white; padding:16px; display:flex; justify-content:space-between; align-items:center;">
            <b style="font-size:14px;">🛠️ Blogger Auditor Pro</b>
            <span id="close-checker" style="cursor:pointer; font-size:24px; line-height:1;">&times;</span>
        </div>
        <div id="summary-bar" style="background:#f4f4f4; padding:10px; font-size:11px; border-bottom:1px solid #ddd; text-align:center;">
            <b>Found ${allMatches.length} Links (In Order)</b>
        </div>
        <div id="check-list" style="overflow-y:auto; flex-grow:1; padding:10px 0; background:#fff;"></div>
    `;
    document.body.appendChild(panel);
    document.getElementById('close-checker').onclick = () => panel.remove();

    const list = document.getElementById('check-list');

    if (allMatches.length === 0) {
        list.innerHTML = "<div style='text-align:center; padding:20px; color:#999;'>No links found. Make sure links are correct.</div>";
        return;
    }

    allMatches.forEach((m, i) => {
        const pos = i + 1;
        const item = document.createElement('div');
        item.style = `padding:12px; margin:8px 12px; border-radius:12px; background:#f9f9f9; border-left:5px solid ${m.color}; position:relative; box-shadow: 0 2px 5px rgba(0,0,0,0.05);`;
        item.innerHTML = `
            <span style="position:absolute; top:10px; right:10px; background:#eee; padding:2px 8px; border-radius:10px; font-size:10px; font-weight:bold;">#${pos}</span>
            <b>${m.label}</b><br>
            <small style="word-break:break-all; color:#666; font-size:10px;">${m.id}</small><br>
            <b id="status-${pos}" style="color:orange; font-size:12px;">Checking...</b>
        `;
        list.appendChild(item);

        if (m.type === 'dl' || m.type === 'pv') {
            const img = new Image();
            img.src = `https://drive.google.com/thumbnail?id=${m.id}&sz=w200`;
            img.onload = () => { document.getElementById(`status-${pos}`).innerHTML = "✅ Active"; document.getElementById(`status-${pos}`).style.color = "green"; };
            img.onerror = () => { document.getElementById(`status-${pos}`).innerHTML = "❌ Dead / Private"; document.getElementById(`status-${pos}`).style.color = "red"; };
        } else {
            document.getElementById(`status-${pos}`).innerHTML = `<a href="${m.id}" target="_blank" style="color:${m.color}; text-decoration:none;">Verify Manually ↗</a>`;
        }
    });
}

setInterval(initExtension, 1000);