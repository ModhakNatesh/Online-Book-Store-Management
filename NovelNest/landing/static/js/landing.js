function scrollToFeatures() {
    // Scroll to the element with id "features-id"
    const element = document.getElementById('features-id');
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}

function redirectToAccounts() {
    window.location.href = '/accounts/login'; // Adjust the URL as needed
}

function redirectTologout() {
    window.location.href = '/accounts/logout'; // Adjust the URL as needed
}