const rate = 280; // Aap yahan latest rate likh sakte hain

function convertUSDtoPKR() {
    // Sirf un elements ko target karen jin mein $ ho aur PKR pehle se na likha ho
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    let node;

    while (node = walker.nextNode()) {
        let text = node.nodeValue;
        if (text.includes('$') && !text.includes('PKR')) {
            // RegEx use kar rahe hain taake $12.34 jaise numbers dhoond saken
            let newText = text.replace(/\$([\d,]+\.?\dd?)/g, (match, p1) => {
                let usd = parseFloat(p1.replace(/,/g, ''));
                if (!isNaN(usd)) {
                    let pkr = (usd * rate).toLocaleString('en-PK', { maximumFractionDigits: 0 });
                    return `${match} (Rs ${pkr})`;
                }
                return match;
            });
            
            if (newText !== text) {
                node.nodeValue = newText;
            }
        }
    }
}

// 1. Pehli baar chalane ke liye
convertUSDtoPKR();

// 2. Dashboard update hone par khud chalne ke liye (MutationObserver)
const observer = new MutationObserver(() => {
    convertUSDtoPKR();
});

observer.observe(document.body, { childList: true, subtree: true });