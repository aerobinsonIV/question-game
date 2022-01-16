let submitButton = document.getElementById("submit-button");

function sendOtherPlayerFinishedPings() {
    questionsPing().then((response) => {

        if(response.finished === 1){
            console.log("All questions answered!")
            document.cookie = "game_id=" + response.game_id + "; path=/";
            // window.location.href = "/results";
        }else{
        //Rerun this function and ping again asking for a match
        setTimeout(() => {
            sendOtherPlayerFinishedPings();
        }, 1000);
        }
    })
}

function handleQuestionSubmitResponse(response){
    if(response.finished === 1){
        console.log("All questions answered!")
        document.cookie = "game_id=" + response.game_id + "; path=/";
        // window.location.href = "/results";
    }else{
    //Rerun this function and ping again asking for a match
    setTimeout(() => {
        sendOtherPlayerFinishedPings();
    }, 1000);
    }
}

setTimeout(() => {
    sendOtherPlayerFinishedPings();
}, 1000);

submitButton.addEventListener('click', (event) => {
    
    postAnswers("poggers").then((response) => {
        console.log(response);
        handleQuestionSubmitResponse(response)
    })
})