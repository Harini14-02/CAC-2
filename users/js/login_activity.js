// login_activity.js

function logLoginActivity(username, success) {
    // Retrieve existing login activity from local storage
    var loginActivity = JSON.parse(localStorage.getItem('loginActivity')) || [];

    // Add the new login activity entry
    loginActivity.unshift({
        username: username,
        status: success ? 'Success' : 'Failed',
        timestamp: new Date().toLocaleString()
    });

    // Store the updated login activity in local storage
    localStorage.setItem('loginActivity', JSON.stringify(loginActivity));
}

function displayLoginActivity(targetElementId) {
    // Retrieve login activity from local storage
    var loginActivity = JSON.parse(localStorage.getItem('loginActivity')) || [];

    // Display login activity on the specified target element
    var targetElement = document.getElementById(targetElementId);
    targetElement.innerHTML = '<h2>Login Activity</h2>';
    targetElement.innerHTML += '<table border="1"><tr><th>Timestamp</th><th>Username</th><th>Status</th></tr>';

    var space = document.createTextNode(' ');
    var newLine = document.createElement('br');

    for (var i = 0; i < loginActivity.length; i++) {
        targetElement.innerHTML +=  loginActivity[i].username+' '+' ';

    }

    targetElement.innerHTML += '</table>';
}
