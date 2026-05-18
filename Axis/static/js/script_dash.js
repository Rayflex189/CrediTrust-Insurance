// Toggle sidebar visibility
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const openBtn = document.getElementById('openSidebarBtn');
    if (!sidebar || !openBtn) return;

    if (sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
        openBtn.style.display = 'block';
    } else {
        sidebar.classList.add('open');
        openBtn.style.display = 'none';
    }
}

// Global toggle for main payment popup (single definition, no duplicate)
function togglePaymentPopup() {
    const popup = document.getElementById('paymentPopup');
    if (!popup) return;

    if (popup.classList.contains('show')) {
        popup.classList.remove('show');
        popup.classList.add('hide');
    } else {
        popup.classList.remove('hide');
        popup.classList.add('show');
    }
}

// Transfer button event (preserved)
const transferBtn = document.querySelector('.custom_tf');
if (transferBtn) {
    transferBtn.addEventListener('click', () => {
        togglePaymentPopup();
    });
}

// Deposit link (myLink) – prevent default navigation
const depositLink = document.getElementById('myLink');
if (depositLink) {
    depositLink.addEventListener('click', function(event) {
        event.preventDefault();
        // Your custom logic here (if any)
    });
}

// Toggle info popup (deposit instructions)
function toggleInfoPopup() {
    const popup = document.getElementById('infoPopup');
    if (!popup) return;

    if (popup.classList.contains('show')) {
        popup.classList.remove('show');
        popup.classList.add('hide');
        popup.addEventListener('animationend', () => {
            popup.style.display = 'none';
        }, { once: true });
    } else {
        popup.style.display = 'flex';
        popup.classList.remove('hide');
        popup.classList.add('show');
    }
}

// Deposit button event
const depositBtn = document.querySelector('.custom_dp');
if (depositBtn) {
    depositBtn.addEventListener('click', () => {
        toggleInfoPopup();
    });
}

// Toggle crypto popup
function toggleCryptoPopup() {
    const popup = document.getElementById('cryptoPopup');
    if (!popup) return;

    if (popup.classList.contains('show')) {
        popup.classList.remove('show');
        popup.classList.add('hide');
        popup.addEventListener('animationend', () => {
            popup.style.display = 'none';
        }, { once: true });
    } else {
        popup.style.display = 'flex';
        popup.classList.remove('hide');
        popup.classList.add('show');
    }
}

// Add icon (fa-plus) events – originally toggles crypto popup,
// but later also toggles payment popup. Preserving both.
const plusIcon = document.querySelector('.fa-plus');
if (plusIcon) {
    plusIcon.addEventListener('click', () => {
        toggleCryptoPopup();
    });
}

// Show specific payment form (PayPal, Zelle, etc.)
function showPaymentForm(formId) {
    const paymentPopup = document.getElementById('paymentPopup');
    const specificPopup = document.getElementById(formId);
    if (!paymentPopup || !specificPopup) return;

    paymentPopup.classList.remove('show');
    paymentPopup.classList.add('hide');
    specificPopup.style.display = 'flex';
    specificPopup.classList.add('show');
}

// Hide specific payment form and return to main payment popup
function hidePaymentForm(formId) {
    const specificPopup = document.getElementById(formId);
    if (!specificPopup) return;

    specificPopup.classList.remove('show');
    specificPopup.classList.add('hide');
    specificPopup.addEventListener('animationend', () => {
        specificPopup.style.display = 'none';
        const mainPopup = document.getElementById('paymentPopup');
        if (mainPopup) mainPopup.classList.add('show');
    }, { once: true });
}

// Payment success popup
function showPaymentSuccessPopup() {
    const successPopup = document.getElementById('paymentSuccessPopup');
    if (!successPopup) return;
    successPopup.style.display = 'flex';
    successPopup.classList.add('show');
}

function hidePaymentSuccessPopup() {
    const successPopup = document.getElementById('paymentSuccessPopup');
    if (!successPopup) return;
    successPopup.classList.remove('show');
    successPopup.classList.add('hide');
    successPopup.addEventListener('animationend', () => {
        successPopup.style.display = 'none';
    }, { once: true });
}

// Handle form submission success (called from forms)
function handlePaymentSuccess(event) {
    event.preventDefault();
    const form = event.target.closest('.payment-popup');
    if (form && form.id) {
        hidePaymentForm(form.id);
    }
    showPaymentSuccessPopup();
}

// Additional event: plus icon also toggles payment popup (original behavior)
if (plusIcon) {
    plusIcon.addEventListener('click', () => {
        togglePaymentPopup();
    });
}

// Google Translate initialization
function googleTranslateElementInit() {
    new google.translate.TranslateElement(
        { pageLanguage: 'en' },
        'google_translate_element'
    );
}

// Bounce animation for translate icon
const translateIcon = document.getElementById('translate-icon');
if (translateIcon) {
    translateIcon.addEventListener('mouseover', () => {
        translateIcon.style.animation = 'bounce 0.5s infinite alternate';
    });
    translateIcon.addEventListener('mouseleave', () => {
        translateIcon.style.animation = '';
    });
}

// Optional: vibrateBell function (if used elsewhere)
function vibrateBell() {
    const bell = document.querySelector('.fa-bell');
    if (bell) {
        bell.style.animation = 'none';
        setTimeout(() => {
            bell.style.animation = '';
        }, 10);
    }
}

// Ensure any duplicate event listeners do not cause errors
// (The original had two .fa-plus listeners – we preserve both)
