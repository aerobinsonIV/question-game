// TODO: import * as api from "../api.js"

let loginButton = document.getElementById("login-button");
loginButton.addEventListener('click', (event) => {
    
    // Get form entries
    email = document.getElementById("email-input").value
    password = document.getElementById("password-input").value

    // Call API function  
    login(email, password).then((response) => {
        document.cookie = "login_cookie=" + response.cookie + "; path=/";
        window.location.replace("/matchmaking");
    });
})