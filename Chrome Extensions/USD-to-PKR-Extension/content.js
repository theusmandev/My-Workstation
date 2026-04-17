

const rate = 278; 

// 1. Choti aur saaf styling
const style = document.createElement('style');
style.innerHTML = `
  .pkr-label {
    font-size: 0.6em !important;
    color: #B7C7DA !important; /* Gold color taake blue background par saaf dikhe */
    font-weight: normal !important;
    margin-left: 5px !important;
    display: inline-block !important;
  }
`;
document.head.appendChild(style);

function convertUSDtoPKR() {
    observer.disconnect();

    // TreeWalker sirf text ko dhoondta hai, HTML tags ko nahi cherta
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    let node;
    const nodesToReplace = [];

    while (node = walker.nextNode()) {
        let text = node.nodeValue;
        // Check: Agar $ hai, PKR pehle se nahi hai, aur parent element pehle se converted nahi hai
        if (text.includes('$') && !text.includes('Rs') && !node.parentElement.hasAttribute('data-converted')) {
            nodesToReplace.push(node);
        }
    }

    nodesToReplace.forEach(textNode => {
        let text = textNode.nodeValue;
        let parent = textNode.parentElement;

        let newHTML = text.replace(/\$([\d,]+\.?\d*)/g, (match, p1) => {
            let usd = parseFloat(p1.replace(/,/g, ''));
            if (!isNaN(usd)) {
                let pkr = (usd * rate).toLocaleString('en-PK', { maximumFractionDigits: 0 });
                return `${match} <span class="pkr-label">Rs ${pkr}</span>`;
            }
            return match;
        });

        if (newHTML !== text) {
            // Naya element banayen taake asli layout na tootay
            let span = document.createElement('span');
            span.innerHTML = newHTML;
            span.setAttribute('data-converted', 'true');
            
            // Text node ko replace karen
            if (textNode.parentNode) {
                textNode.replaceWith(span);
            }
        }
    });

    startObserver();
}

const observer = new MutationObserver((mutations) => {
    // Sirf tab chalana jab waqayi koi naya content aaye
    convertUSDtoPKR();
});

function startObserver() {
    observer.observe(document.body, { childList: true, subtree: true });
}

// Start
convertUSDtoPKR();