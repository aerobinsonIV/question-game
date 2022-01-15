// TODO: import * as api from "../api.js"

let signupButton = document.getElementById("signup-button");
loginButton.addEventListener('click', (event) => {
    
    // Get form entries
    username = document.getElementById("username-input").value
    email = document.getElementById("email-input").value
    password = document.getElementById("password-input").value

    // Call API function  
    signup(username, email, password).then((response) => {
        console.log(response);
        outputText.innerHTML = response.text;
    });
})