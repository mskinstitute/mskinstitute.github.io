// Function to auto-detect country code
function autoDetectCountry() {
    // Set the default country code to United Kingdom (GB)
    var defaultCountryCode = "GB";

    // Update the country code in the dropdown after the document is fully loaded
    document.addEventListener("DOMContentLoaded", function () {
        var countryCodeDropdown = document.getElementById("countryCode");

        // Set the value directly
        countryCodeDropdown.value = defaultCountryCode;
    });
}

// Call the auto-detect function when the page loads
window.onload = autoDetectCountry;

function validateMobileNumber() {
    var mobileNumber = document.getElementById("mobileNumber").value;
    //var regex = /^[0-9]{10}$/; // regular expression to match 10 digit number
    var regex = /^\d{7,20}$/; // regular expression to match 7 to 20 digit number
    if (!regex.test(mobileNumber)) {
        //alert("Please enter a valid 10 digit mobile number");
        alert("Please enter a valid mobile number.");
        return false;
    }
    return true;
}

function sendWhatsApp() {
    if (!validateMobileNumber()) {
        return;
    }
    var countryCode = document.getElementById("countryCode").value;
    var mobileNumber = document.getElementById("mobileNumber").value;
    var message = document.getElementById("message").value;
    var url = "whatsapp://send?phone=" + countryCode + mobileNumber + "&text=" + encodeURIComponent(message);
    window.open(url);
}

function sendBusinessWhatsApp() {
    if (!validateMobileNumber()) {
        return;
    }
    var countryCode = document.getElementById("countryCode").value;
    var mobileNumber = document.getElementById("mobileNumber").value;
    var message = document.getElementById("message").value;
    var url = "https://api.whatsapp.com/send?phone=" + countryCode + mobileNumber + "&text=" + encodeURIComponent(message);
    window.open(url);
}

// Function to clear all form fields
function clearForm() {
    document.getElementById("countryCode").selectedIndex = 0; // Reset country code dropdown
    document.getElementById("mobileNumber").value = ""; // Clear mobile number input
    document.getElementById("message").value = ""; // Clear message textarea
}

// Function to update character count in the message textarea
function updateCharCount() {
    var message = document.getElementById("message").value;
    var charCount = message.length;
    document.getElementById("charCount").textContent = charCount + "/300"; // Assuming a max limit of 300 characters
}

// Call the updateCharCount function when the message textarea is changed
document.getElementById("message").addEventListener("input", updateCharCount);
