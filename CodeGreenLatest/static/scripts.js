// function showProgressBar() {
//     const progressBar = document.getElementById('progress-bar');
//     progressBar.style.display = 'block';

//     // Get the progress bar element within the container
//     const progressBarElement = progressBar.querySelector('.progress-bar');

//     // Reset progress to 0
//     progressBarElement.style.width = '0%';
//     progressBarElement.textContent = 'Processing your code...';

//     // Simulate progress with a timer
//     let progress = 0;
//     const increment = 5;
//     const interval = 20;
//     function updateProgressBar() {
//         progress += increment;
//         progressBarElement.style.width = `${progress}%`;

//         if (progress <= 20) {
//             progressBarElement.textContent = 'Processing your input...';
//         } else if (progress <= 80) {
//             progressBarElement.textContent = 'Checking security considerations...';
//         } else {
//             progressBarElement.textContent = 'Encrypting your code and getting results ready...';
//         }
    
//         if (progress < 100) {
//             setTimeout(updateProgressBar, interval);
//         }
//     }


//     // if (progress<100){
//     //     updateProgressBar()
//     // }
//     // else{
//     //     hideProgressBar()
//     // }
// }

function showProgressBar() {
    return new Promise(resolve => {
        const progressBar = document.getElementById('progress-bar');
        progressBar.style.display = 'block';
        

        const progressBarElement = progressBar.querySelector('.progress-bar');

        let progress = 0;
        const increment = 5;
        const interval = 300;

        function updateProgressBar() {
            progress += increment;
            progressBarElement.style.width = `${progress}%`;

            if (progress <= 20) {
                progressBarElement.textContent = 'Processing your input...';
            } else if (progress <= 80) {
                progressBarElement.textContent = 'Applying security checks...';
            } else {
                progressBarElement.textContent = 'Encrypting your code and getting results ready...';
            }

            if (progress < 100) {
                setTimeout(updateProgressBar, interval);
            } else {
                // Resolve the Promise when the progress reaches 100%
                resolve();
            }
        }

        updateProgressBar();
    });
}


function hideProgressBar() {
    const progressBar = document.getElementById('progress-bar');
    progressBar.style.display = 'none';
}


function processCode() {
    const userCode = document.getElementById('user-code').value;
    showProgressBar()
   

    // Call the Flask route to get the greener version using ChatGPT API
    // getOptimizedCode(userCode)
    //     .then(optimizedCode => {

          
    //         // Display the optimized code in the output textarea
    //         // document.getElementById('optimized-code').value=optimizedCode;
    //         localStorage.setItem("test_variable", optimizedCode);
         
    //         window.location = "optimized";
          
    //         // document.getElementById('optimized-code').value = optimizedcode;
    //     })
    //     .catch(error => {
    //         console.error('Error:', error);
    //         // Handle error, display a message to the user, etc.
    //     });
    //     .finally(() => {
    //         // Hide the progress bar whether the operation is successful or encounters an error
    //         hideProgressBar();
    //     });

    getOptimizedCode(userCode)
    .then(optimizedCode => {
        // Display the optimized code in the output textarea
        localStorage.setItem("test_variable", optimizedCode);
        window.location = "optimized";
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle error, display a message to the user, etc.
    })
    .finally(() => {
        // Hide the progress bar whether the operation is successful or encounters an error
        hideProgressBar();
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

// function getOptimizedCode(userCode) {
//     const apiUrl = '/api/greener-code';

//     return new Promise((resolve, reject) => {
//         fetch(apiUrl, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ code: userCode }),
//         })
//         .then(response => response.json())
//         .then(data => {
//             console.log('API Response:', data);
//             // Check if data is ready (you might need to adjust this condition)
//             if (data.optimizedCodeReady) {
//                 resolve(data.optimizedCode);
//             } else {
//                 // Retry after a delay or handle it based on your requirements
//                 setTimeout(() => getOptimizedCode(userCode).then(resolve).catch(reject), 1000);
//             }
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             reject('Error getting optimized code.');
//         });
//     });
// }