// script.js
// Initialize AOS
AOS.init({
    duration: 1000,
    once: true
});

// Dark/Light Mode Toggle
const modeSwitch = document.getElementById('mode-switch');
const body = document.body;

// Load saved mode from localStorage
if (localStorage.getItem('darkMode') === 'enabled') {
    body.classList.add('dark');
    modeSwitch.checked = true;
}

modeSwitch.addEventListener('change', () => {
    if (modeSwitch.checked) {
        body.classList.add('dark');
        localStorage.setItem('darkMode', 'enabled');
    } else {
        body.classList.remove('dark');
        localStorage.setItem('darkMode', 'disabled');
    }
});

// Active Nav Link Highlight
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
const navLinks = document.querySelectorAll('.nav-links a');
navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPage) {
        link.classList.add('active');
    }
});

// Contact Form Validation (Frontend Only)
const contactForm = document.getElementById('contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const message = document.getElementById('message').value.trim();

        if (!name || !email || !message) {
            alert('Please fill in all fields.');
            return;
        }

        if (!/\S+@\S+\.\S+/.test(email)) {
            alert('Please enter a valid email.');
            return;
        }

        // Simulate send (since no backend)
        alert('Message sent successfully! (Simulation)');
        contactForm.reset();
    });
}