const registrationForm = document.getElementById('registration-form');
registrationForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const gender = document.getElementById('gender').value;
    const style = document.getElementById('style').value;
    const hairColor = document.getElementById('hairColor').value;
    const skinColor = document.getElementById('skinColor').value;
    const size = document.getElementById('size').value;

    // Send data to Flask using AJAX (replace with your Flask endpoint)
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name,
            age,
            gender,
            style,
            hairColor,
            skinColor,
            size
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) { 
            console.log("fthft")
            window.location.href = '/recommendation';
            
        } else {
            console.error(data.error); // Handle errors
        }
    })
    .catch(error => console.error(error));
});