function processCode() {
    const userCode = document.getElementById('user-code').value;

    // Call the Flask route to get the greener version using ChatGPT API
    getOptimizedCode(userCode)
        .then(optimizedCode => {
            // Display the optimized code in the output textarea
            document.getElementById('optimized-code').value = optimizedCode;
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle error, display a message to the user, etc.
        });
}

function getOptimizedCode(userCode) {
    const apiUrl = '/api/greener-code';

    return fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: userCode }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('API Response:', data); // Log the entire response for debugging
        return data.optimizedCode;  // Adjust the property name based on what your server sends
    })
    .catch(error => {
        console.error('Error:', error);
        return 'Error getting optimized code.';
    });
}

