// TODO: import * as api from "../api.js"

let signupButton = document.getElementById("signup-button");
signupButton.addEventListener('click', (event) => {
    
    // Get form entries
    username = document.getElementById("username-input").value
    email = document.getElementById("email-input").value
    password = document.getElementById("password-input").value

    // Call API function  
    signup(username, email, password);
})