
function sendMatchmakingPingsUntilMatchFound(){
    matchmakingPing().then((response) => {
        console.log(response);
    })
}

sendMatchmakingPingsUntilMatchFound();

// setTimeout(() => {
//     console.log("this is the second message")
// }, 3000);