document.getElementById('feeForm').addEventListener('submit', function (event) {
    event.preventDefault();
    
    const regNo = document.getElementById('reg_no').value;
    const url = 'https://script.google.com/macros/s/AKfycbz5-w5loM3tSfmyKrJNpl1Ny3aFjBGm9bMlD3thnHEIszGLtgTFK3urH0_fjP6GRkw/exec?registration_no=' + regNo;
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const student = data[regNo];
            if (student) {
                displayStudentData(student);
                generateQRCode(regNo);
            } else {
                alert('No student found with this Registration Number.');
            }
        })
        .catch(error => console.error('Error:', error));
});

function displayStudentData(student) {
    const studentDiv = document.getElementById('studentData');
    studentDiv.innerHTML = `
        <p><strong>Name:</strong> ${student.Name}</p>
        <p><strong>Father's Name:</strong> ${student.Father_Name}</p>
        <p><strong>Date of Birth:</strong> ${new Date(student.Bate_of_Birth).toLocaleDateString()}</p>
        <p><strong>Contact Number:</strong> ${student.Contact_Number}</p>
        <p><strong>Course:</strong> ${student.Course}</p>
    `;
    studentDiv.style.display = 'block';
}

function generateQRCode(regNo) {
    const qrDiv = document.getElementById('qrCode');
    const upiUrl = `upi://pay?pa=mskinstitute@airtel&pn=MSK%20Institute&tn=${regNo}%20|%20Admission%20Fee%20&am=1000&cu=INR&mode=02`;
    const qrApiUrl = `https://api.qrserver.com/v1/create-qr-code/?data=${encodeURIComponent(upiUrl)}`;
    
    qrDiv.innerHTML = `<img src="${qrApiUrl}" alt="QR Code for UPI Payment">`;
    qrDiv.style.display = 'block';
    document.getElementById('payButton').style.display = 'block';
    document.getElementById('payButton').setAttribute("href" , upiUrl );
}

function generateHiddenFormForSaveData(student) {
    const hidden_Tag = document.createElement('form');
    hidden_Tag.id = 'hiddenForm';
    const fee_amount = document.getElementById('fee_amount');
    hidden_Tag.innerHTML = `
    <input type="text" id="fee_amount" name="Fee_Amount" value="${fee_amount}">    
    `
    
}




document.getElementById('pasteButton').addEventListener('click', function () {
    navigator.clipboard.readText()
        .then(text => {
            document.getElementById('reg_no').value = text; // Paste the text into the input field
        })
        .catch(err => {
            console.error('Failed to read clipboard contents: ', err);
        });
});
