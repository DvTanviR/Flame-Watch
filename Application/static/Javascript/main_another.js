// function togglePrediction(element) {
//     const toggleShow = element.nextElementSibling;
//     // const icon = element.querySelector('.toggle i');
//     if (toggleShow.style.display === "block") {
//         toggleShow.style.display = "none";
//         rotation += 45; // Increase rotation by 45 degrees
//         box.style.transform = `rotate(${rotation}deg)`;
//     } else {
//         toggleShow.style.display = "block";
//     }
// }
let rotation = 0; // Initialize rotation angle

function togglePrediction(element) {
    const toggleShow = element.nextElementSibling;
    const icon = element.querySelector('.faq-icon');

    if (toggleShow.style.display === "block") {
        toggleShow.style.display = "none";
        icon.classList.remove('toggle-roted');

    } else {
        icon.classList.add('toggle-roted');
        toggleShow.style.display = "block";
    }
}

document.getElementById('searchButton').addEventListener('click', function () {
    const input = document.getElementById('searchText').value.trim();
    const [lat, lon] = input.split(',').map(item => item.trim());

    // Basic validation
    if (!lat || !lon || isNaN(lat) || isNaN(lon)) {
        alert("Please enter coordinates in the format: latitude,longitude");
        return;
    }
    console.log('Coordinates:', lat, lon);

    fetch('https://flamewatch.send-up.co/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // CSRF token for Django
        },
        body: JSON.stringify({ lat: lat, lon: lon })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Prediction result:', data);

        const resultDiv = document.querySelector('.predict-img h1');
        let secondsPassed = 10;
        const interval = setInterval(() => {
            secondsPassed -= 1;
            resultDiv.textContent = `Please wait... ${secondsPassed} seconds`;

            if (secondsPassed <= 5) {
                clearInterval(interval);
                resultDiv.textContent = `Prediction: ${data.wildfire_probability}% chance of wildfire`;
            }
        }, 1000); // update every 10 seconds
        // You can update your page with the result here
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Helper function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}