document.addEventListener('DOMContentLoaded', () => {
    const loginButtons = document.querySelectorAll('.login, .logins');
    const registerButton = document.getElementById('register');
    const loginPopup = document.getElementById('loginPopup');
    const registerPopup = document.getElementById('registerPopup');
    const closeButtons = document.querySelectorAll('.close');
    const navbar = document.getElementById('navbar');
    const hamburgerIcon = document.getElementById('hamburger-icon');

    loginButtons.forEach(button => {
        button.addEventListener('click', () => {
            loginPopup.classList.add('visible');
        });
    });

    registerButton.addEventListener('click', () => {
        registerPopup.classList.add('visible');
    });

    closeButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            event.target.closest('.popup').classList.remove('visible');
        });
    });

    // Toggle the navbar on hamburger click
    hamburgerIcon.addEventListener('click', () => {
        navbar.classList.toggle('active');
    });

    // Close the popup when clicking outside of it
    window.addEventListener('click', (event) => {
        if (event.target === loginPopup) {
            loginPopup.classList.remove('visible');
        }
        if (event.target === registerPopup) {
            registerPopup.classList.remove('visible');
        }
    });
});


function generateRandomIP() {
    // Generate four random numbers between 0 and 255
    let ip = [];
    for (let i = 0; i < 4; i++) {
        ip.push(Math.floor(Math.random() * 256));
    }
    // Join the numbers with dots to mimic an IP address
    return ip.join('.');
}

// Display the generated random IP address
document.getElementById("user-ip").textContent = generateRandomIP();

function generateRandomIP() {
    // Generate four random numbers between 0 and 255
    let ip = [];
    for (let i = 0; i < 4; i++) {
        ip.push(Math.floor(Math.random() * 256));
    }
    // Join the numbers with dots to mimic an IP address
    return ip.join('.');
}

// Display the generated random IP address
document.getElementById("user-ip-cast").textContent = generateRandomIP();

function updateTime() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    const timeString = `${hours}:${minutes}:${seconds}`;
    document.getElementById("time").textContent = timeString;
}

// Update the clock every second
setInterval(updateTime, 1000);
// Initialize the clock immediately
updateTime();

const text = "We do banking differently. We believe that people come first, \nand that everyone deserves a great experience \nevery step of the way – whether it’s face to face, \nover the phone, online or on our app.";
let index = 0;
const speed = 50; // Adjust typing speed (milliseconds)

function typeWriter() {
    if (index < text.length) {
        // Create a span to hold each character
        const span = document.createElement("span");
        span.classList.add("fade-in");
        span.textContent = text.charAt(index);
        document.getElementById("typed-text").appendChild(span);
        index++;
        setTimeout(typeWriter, speed);
    }
}

window.onload = function() {
    typeWriter();
};

