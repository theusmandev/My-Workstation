const rate = 280; 

// CSS update: Ab hum PKR ko block banayenge taake wo neeche wali line par aaye
const style = document.createElement('style');
style.innerHTML = `
  .pkr-container {
    display: block !important; /* Agli line par shift karne ke liye */
    font-size: 0.5em !important; /* Size mazeed chota kiya */
    color: #e2e8f0 !important;
    font-weight: normal !important;
    line-height: 1.2 !important;
    margin-top: 2px !important;
    opacity: 0.9;
  }
  /* Card ke main numbers ko jagah dene ke liye */
  ins.adsbygoogle, .ads-stats-card {
    overflow: visible !important;
  }
`;
document.head.appendChild(style);

function convertUSDtoPKR() {
    observer.disconnect();

    // Sirf un elements ko target karna jo text dikhate hain
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    let nodes = [];
    let node;
    while (node = walker.nextNode()) nodes.push(node);

    nodes.forEach(textNode => {
        let text = textNode.nodeValue;
        
        // Check: "$" ho aur "Rs" pehle se na ho
        if (text.includes('$') && !text.includes('Rs')) {
            let parent = textNode.parentElement;
            
            // AdSense ke nested elements ko handle karne ke liye replace logic
            let newHTML = text.replace(/\$([\d,]+\.?\d*)/g, (match, p1) => {
                let usd = parseFloat(p1.replace(/,/g, ''));
                if (!isNaN(usd)) {
                    let pkr = (usd * rate).toLocaleString('en-PK', { maximumFractionDigits: 0 });
                    // Bracket hata diye taake mazeed saaf lage
                    return `${match}<span class="pkr-container">Rs ${pkr}</span>`;
                }
                return match;
            });

            if (newHTML !== text) {
                // Text node ko HTML span se replace karna
                let span = document.createElement('span');
                span.innerHTML = newHTML;
                textNode.replaceWith(span);
            }
        }
    });

    startObserver();
}

const observer = new MutationObserver(() => {
    convertUSDtoPKR();
});

function startObserver() {
    observer.observe(document.body, { childList: true, subtree: true });
}

// Initial Run
convertUSDtoPKR();