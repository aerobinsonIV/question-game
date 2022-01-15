let coolButton = document.getElementById("coolButton");
coolButton.addEventListener('click', (event) => {
    text = document.getElementById("coolTextBox").value
    outputText = document.getElementById("text");

    mom(text).then((response) => {
        console.log(response);
        outputText.innerHTML = response.text;
    });
})