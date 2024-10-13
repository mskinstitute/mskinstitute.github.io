document.addEventListener('DOMContentLoaded', function () {
    fetch('components/header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header').innerHTML = data;
        });
    fetch('components/footer.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer').innerHTML = data;
        });
    fetch('components/phone-footer.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('phone-footer').innerHTML = data;
        });
});