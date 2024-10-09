const addmission_form_submit_link = 'https://script.google.com/macros/s/AKfycbwFQhZbVTe7r0cC7lMGPo8Jv_wVXWXWvtqbSFxcnZ76PbBdes5iQNlI6_xvMiLdBA/exec';
const form = document.forms['addmission_form']

form.addEventListener('submit', e => {
    e.preventDefault()

    const now = new Date();
    const pad = (n) => n.toString().padStart(2, '0');

    // Format the current date and time as YYYYMMDDHHMMSS
    const Registration_No = now.getFullYear() +
        pad(now.getMonth() + 1) +
        pad(now.getDate()) +
        pad(now.getHours()) +
        pad(now.getMinutes()) +
        pad(now.getSeconds());

    document.getElementById('Registration_No_Copy').addEventListener('click', e => {
        e.preventDefault()
        navigator.clipboard.writeText(Registration_No);
    })
    document.getElementById('Admission_Time').value = now.toLocaleDateString() + " " + now.toLocaleTimeString();
    document.getElementById('Registration_No').value = Registration_No;

    fetch(addmission_form_submit_link, { method: 'POST', body: new FormData(form) })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        document.querySelector(".Registration_No_Show").innerHTML = "Success .\nYour Registration_No: " + Registration_No;
        document.querySelector("[data-modal-preview]").showModal()

        return navigator.clipboard.writeText(Registration_No);
    })
    .then(() => {
        console.log('Registration number copied to clipboard:', Registration_No);
        // window.location.href = 'add_pay.html';
    })
    .catch(error => {
        console.error('Error!', error.message);
    });
})

