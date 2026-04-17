const rate = 280; 

// 1. PKR ke liye choti si CSS style add karna
const style = document.createElement('style');
style.innerHTML = `
  .pkr-small {
    font-size: 0.65em !important; /* Asli price se 35% chota */
    font-weight: normal !important;
    color: #e0e0e0; /* Thora halka rang (Greyish white) */
    margin-left: 4px;
    display: inline-block;
    vertical-align: middle;
  }
`;
document.head.appendChild(style);

function convertUSDtoPKR() {
    observer.disconnect();

    // AdSense ke un elements ko pakarna jahan prices hoti hain
    const elements = document.querySelectorAll('div, span, p');

    elements.forEach(el => {
        // Sirf un elements ko cherna jin mein $ ho aur PKR pehle se na ho
        // Aur ye bhi check karna ke element ke andar mazeed tags na hon (taake design na tootay)
        if (el.innerText.includes('$') && !el.innerHTML.includes('pkr-small') && el.children.length === 0) {
            
            let originalText = el.innerText;
            let newHTML = originalText.replace(/\$([\d,]+\.?\d*)/g, (match, p1) => {
                let usd = parseFloat(p1.replace(/,/g, ''));
                if (!isNaN(usd)) {
                    let pkr = (usd * rate).toLocaleString('en-PK', { maximumFractionDigits: 0 });
                    // Styled span return karna
                    return `${match} <span class="pkr-small">(Rs ${pkr})</span>`;
                }
                return match;
            });

            if (newHTML !== originalText) {
                el.innerHTML = newHTML;
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

// Initial run
convertUSDtoPKR();