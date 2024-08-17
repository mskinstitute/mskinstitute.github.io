
const isAndroid = /Android/i.test(navigator.userAgent);

if (isAndroid) {
    document.getElementById("upiLogos").classList.remove('hideOnLaptop');
    document.getElementById("PaymentContainer").classList.remove('hideOnLaptop');
} else {
    document.getElementById("note").classList.remove('hideOnPhone');
    
}

var roll_no = document.getElementById('roll_no').value;
var student_name = document.getElementById('student_name').value;
var pay_button = document.getElementById('Pay_Button');

function generateLink() {
    document.getElementById("result").classList.remove('hideOnLaptop');
    var amount = document.getElementById('amount').value;
    var amountNumber = parseFloat(amount);   // Convert the value to a number
    var discount = 0;
    // Percentage: a * b / 100;
    if (amountNumber > 1000 & amountNumber < 2000) {
        discount = amountNumber * 1 / 100;  // Calculate the discount amount (1% of the original amount)
    }
    else if (amountNumber >= 2000 & amountNumber < 3000) {
        discount = amountNumber * 2 / 100;  // Calculate the discount amount (2% of the original amount)
    }
    else if (amountNumber >= 3000 & amountNumber < 4000) {
        discount = amountNumber * 3 / 100;  // Calculate the discount amount (3% of the original amount)
    }
    else if (amountNumber >= 4000 & amountNumber < 6000) {
        discount = amountNumber * 4 / 100;  // Calculate the discount amount (1.5% of the original amount)
    }
    else if (amountNumber >= 6000 & amountNumber < 8000) {
        discount = amountNumber * 6 / 100;  // Calculate the discount amount (2% of the original amount)
    }
    else if (amountNumber >= 8000 & amountNumber < 10000) {
        discount = amountNumber * 8 / 100;  // Calculate the discount amount (2.5% of the original amount)
    }
    else if (amountNumber >= 10000 & amountNumber <= 15000) {
        discount = amountNumber * 10 / 100;  // Calculate the discount amount (3% of the original amount
    }
    else {
        var discount = 0;
    }

    var total_payment = amountNumber - discount;
    var upiLink = `upi://pay?pn=MSK%20Institute&am=${total_payment}&mode=01&pa=mskinstitute@jio&tn=${roll_no}%20${student_name}%20Total%20Payment%20Course%20Fee%20${amountNumber}`;

    // Function to display the generated link
    if (pay_button.style.display === 'none') {
        pay_button.style.display = 'block'; // Show the link
    }
    pay_button.href = upiLink;


    generateQRCode(upiLink, "MSK Institute");
}

function generateQRCode(text) {
    var qrContainer = document.getElementById('qrcode');
    qrContainer.innerHTML = "";  // Clear previous QR code
    new QRCode(qrContainer, text);  // Generate new QR code
    // Set the tooltip with the receiver's name
    qrContainer.title = "Paying to " + "MSK Institute";
}

function admissionFeeLinkGenerate() {
    var upiLink = `upi://pay?pn=MSK%20Institute&am=1000&mode=01&pa=mskinstitute@jio&tn=${roll_no}%20${student_name}%20Total%20Payment%20Course%20Fee%20${amountNumber}`;
    var pay_button = document.getElementById('Pay_Button');
    pay_button.href = upiLink;

}

