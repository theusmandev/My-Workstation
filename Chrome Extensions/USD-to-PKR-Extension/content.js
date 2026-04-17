const rate = 280; 

// CSS Styles
const style = document.createElement('style');
style.innerHTML = `
  .pkr-label {
    display: block !important;
    font-size: 0.55em !important;
    color: rgba(255, 255, 255, 0.85) !important; /* Halka safaid rang */
    font-weight: 400 !important;
    margin-top: 2px !important;
  }
  /* Agat light theme ho to uske liye color fix */
  [data-theme="light"] .pkr-label {
    color: #5f6368 !important;
  }
`;
document.head.appendChild(style);

function convertUSDtoPKR() {
    // 1. Observer ko temporarily rokna
    observer.disconnect();

    // 2. Sirf un elements ko dhoondna jin mein $ ho
    const elements = document.querySelectorAll('span, div, b, h2');

    elements.forEach(el => {
        // Check 1: Kya is mein $ hai?
        // Check 2: Kya hum isay pehle convert kar chuke hain? (Stamp check)
        // Check 3: Kya is ke andar mazeed tags to nahi? (Sirf final value pakarna)
        if (el.innerText.includes('$') && 
            !el.hasAttribute('data-converted') && 
            el.children.length === 0) {

            let originalText = el.innerText;
            let match = originalText.match(/\$([\d,]+\.?\d*)/);

            if (match) {
                let usdValue = parseFloat(match[1].replace(/,/g, ''));
                if (!isNaN(usdValue)) {
                    let pkrValue = (usdValue * rate).toLocaleString('en-PK', { maximumFractionDigits: 0 });
                    
                    // Element ke andar naya HTML set karna
                    el.innerHTML = `${match[0]} <span class="pkr-label">Rs ${pkrValue}</span>`;
                    
                    // STAMP LAGANA: Taake ye dobara convert na ho
                    el.setAttribute('data-converted', 'true');
                }
            }
        }
    });

    // 3. Observer dobara chalu karna
    startObserver();
}

const observer = new MutationObserver(() => {
    convertUSDtoPKR();
});

function startObserver() {
    observer.observe(document.body, { childList: true, subtree: true });
}

// Pehli dafa chalane ke liye
convertUSDtoPKR();