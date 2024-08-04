document.addEventListener("DOMContentLoaded", function () {
    let form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        let answer = document.getElementById('answer').value;

        fetch('/verify_answer/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Function to get CSRF token
            },
            body: JSON.stringify({ answer: answer })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Correct answer!");
            } else {
                alert("Incorrect answer.");
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});


document.addEventListener("DOMContentLoaded", function () {
    let form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        let answer = document.getElementById('answer').value;
        let csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch('/verify_answer/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ answer: answer })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Correct answer!");
            } else {
                alert("Incorrect answer.");
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});
