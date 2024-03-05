function proceed() {
    // Add code here to handle the action when the button is clicked
    // For example, redirecting to the homepage
    window.location.href = '/';
}

document.addEventListener("DOMContentLoaded", function() {
    // Bind an event listener to the quantity input field
    var quantityInput = document.getElementById('quantity');
    quantityInput.addEventListener('input', calculateSubtotal);
});

function calculateSubtotal() {
    var quantity = document.getElementById('quantity').value;
    var bookPrice = parseFloat('{{ book_price }}'); // Parse the book price to float
    var shippingCost = 50; // Change this to your actual shipping cost
    
    var subtotal = (quantity * bookPrice) + shippingCost;
    document.getElementById('subtotal').innerHTML = '₹ ' + subtotal.toFixed(2); // Convert subtotal to string with 2 decimal places
}

