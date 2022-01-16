let submitButton = document.getElementById("submit-button");
submitButton.addEventListener('click', (event) => {
    
    postAnswers("poggers").then((response) => {
        console.log(response);
    })
})