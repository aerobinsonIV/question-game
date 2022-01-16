function sendMatchmakingPingsUntilMatchFound(){
    
    matchmakingPing().then((response) => {
        console.log(response);

        if(response.ready === 1){
            console.log("Match found with " + response.partner)
            document.cookie = "game_id=" + response.gameid + "; path=/";
            window.location.replace("/questions");
        }else{
        //Rerun this function and ping again asking for a match
        setTimeout(() => {
            sendMatchmakingPingsUntilMatchFound();
        }, 1000);
        }
    })
}

setTimeout(() => {
    sendMatchmakingPingsUntilMatchFound();
}, 1000);