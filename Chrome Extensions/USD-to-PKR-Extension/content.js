const rate = 280; 

function convertUSDtoPKR() {
    // 1. Pehle observer ko rok den taake infinite loop na bane
    observer.disconnect();

    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    let node;

    while (node = walker.nextNode()) {
        let text = node.nodeValue;
        
        // Check: Agar "$" hai aur "Rs" pehle se maujood NAHI hai
        if (text.includes('$') && !text.includes('Rs')) {
            let newText = text.replace(/\$([\d,]+\.?\d*)/g, (match, p1) => {
                let usd = parseFloat(p1.replace(/,/g, ''));
                if (!isNaN(usd)) {
                    let pkr = (usd * rate).toLocaleString('en-PK', { maximumFractionDigits: 0 });
                    // Thora sa safai se dikhane ke liye format: $10 (Rs 2,800)
                    return `${match} (Rs ${pkr})`;
                }
                return match;
            });
            
            if (newText !== text) {
                node.nodeValue = newText;
            }
        }
    }

    // 2. Kaam khatam hone ke baad observer ko dobara on kar den
    startObserver();
}

const observer = new MutationObserver(() => {
    convertUSDtoPKR();
});

function startObserver() {
    observer.observe(document.body, { childList: true, subtree: true });
}

// First run
convertUSDtoPKR();