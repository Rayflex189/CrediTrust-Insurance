// Toggle sidebar visibility
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const openBtn = document.getElementById('openSidebarBtn');
    if (sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
        openBtn.style.display = 'block'; // Show the open button
    } else {
        sidebar.classList.add('open');
        openBtn.style.display = 'none'; // Hide the open button
    }
}

// Function to toggle the payment popup visibility
function togglePaymentPopup() {
    const popup = document.getElementById('paymentPopup');
    if (popup.classList.contains('show')) {
        popup.classList.remove('show');
        popup.classList.add('hide');
    } else {
        popup.classList.remove('hide');
        popup.classList.add('show');
    }
}

// Add event listener to Transfer button
document.querySelector('.custom_tf').addEventListener('click', () => {
    togglePaymentPopup();
});

document.getElementById('myLink').addEventListener('click', function(event) {
    event.preventDefault(); // Prevents the default action (navigation)
    // Your custom logic here
});


// Function to toggle the info popup visibility
function toggleInfoPopup() {
    const popup = document.getElementById('infoPopup');
    if (popup.classList.contains('show')) {
        popup.classList.remove('show');
        popup.classList.add('hide');
        // After the animation ends, hide the popup completely
        popup.addEventListener('animationend', () => {
            popup.style.display = 'none';
        }, { once: true });
    } else {
        popup.style.display = 'flex';
        popup.classList.remove('hide');
        popup.classList.add('show');
    }
}

// Add event listener to Deposit button
document.querySelector('.custom_dp').addEventListener('click', () => {
    toggleInfoPopup();
});

// Function to toggle the crypto popup visibility
function toggleCryptoPopup() {
    const popup = document.getElementById('cryptoPopup');
    if (popup.classList.contains('show')) {
        popup.classList.remove('show');
        popup.classList.add('hide');
        // After the animation ends, hide the popup completely
        popup.addEventListener('animationend', () => {
            popup.style.display = 'none';
        }, { once: true });
    } else {
        popup.style.display = 'flex';
        popup.classList.remove('hide');
        popup.classList.add('show');
    }
}

// Add event listener to Add icon or button
document.querySelector('.fa-plus').addEventListener('click', () => {
    toggleCryptoPopup();
});

// Toggle payment options popup
function togglePaymentPopup() {
    const popup = document.getElementById('paymentPopup');
    popup.classList.toggle('show');
}

// Show specific payment form
function showPaymentForm(formId) {
    const paymentPopup = document.getElementById('paymentPopup');
    const specificPopup = document.getElementById(formId);
    paymentPopup.classList.remove('show');
    paymentPopup.classList.add('hide');
    specificPopup.style.display = 'flex';
    specificPopup.classList.add('show');
}

// Hide specific payment form
function hidePaymentForm(formId) {
    const specificPopup = document.getElementById(formId);
    specificPopup.classList.remove('show');
    specificPopup.classList.add('hide');
    specificPopup.addEventListener('animationend', () => {
        specificPopup.style.display = 'none';
        document.getElementById('paymentPopup').classList.add('show');
    }, { once: true });
}

// Show payment success popup
function showPaymentSuccessPopup() {
    const successPopup = document.getElementById('paymentSuccessPopup');
    successPopup.style.display = 'flex';
    successPopup.classList.add('show');
}

// Hide payment success popup
function hidePaymentSuccessPopup() {
    const successPopup = document.getElementById('paymentSuccessPopup');
    successPopup.classList.remove('show');
    successPopup.classList.add('hide');
    successPopup.addEventListener('animationend', () => {
        successPopup.style.display = 'none';
    }, { once: true });
}

// Handle form submission and show success popup
function handlePaymentSuccess(event) {
    event.preventDefault();
    // Hide the form popup
    hidePaymentForm(event.target.closest('.payment-popup').id);
    // Show the payment success popup
    showPaymentSuccessPopup();
}

// Attach event listener to open payment popup
document.querySelector('.fa-plus').addEventListener('click', () => {
    togglePaymentPopup();
});

        function googleTranslateElementInit() {
            new google.translate.TranslateElement(
                {pageLanguage: 'en'},
                'google_translate_element'
            );
        }
        // Get the translate icon element
const translateIcon = document.getElementById('translate-icon');

// Add bounce animation
translateIcon.addEventListener('mouseover', () => {
    translateIcon.style.animation = 'bounce 0.5s infinite alternate';
});

// Reset animation when mouse leaves
translateIcon.addEventListener('mouseleave', () => {
    translateIcon.style.animation = '';
});