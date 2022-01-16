console.log("in questions.js")

getQuestions().then((response) => {
    renderQuestions(response);
})

/*
setTimeout(() => {
    sendWaitingPingsUntilQuestionsAnswered();
}, 1000);

function sendWaitingPingsUntilQuestionsAnswered() {
    questionsPing().then((response) => {

        if(response.ready === 1){
            console.log("All questions answered!")
            document.cookie = "game_id=" + response.game_id + "; path=/";
            window.location.href = "/results";
        }else{
        //Rerun this function and ping again asking for a match
        setTimeout(() => {
            sendWaitingPingsUntilQuestionsAnswered();
        }, 1000);
        }
    })
}
*/
function renderQuestions(data) {
    let questions =[];

    for (let i = 0; i < data.questions.length; i++) {
        let thisQuestion = {};
        thisQuestion.question = data.questions[i].question;
        let choices = [];
        for (let j = 0; j < data.questions[i].answers.length; j++) {
            choices.push(data.questions[i].answers[j].value)
        }
        thisQuestion.choices = choices;
        questions.push(thisQuestion);
    }

    let questions2 = questions;

    for (let i = 0; i < questions.length; i++) {
        let C = document.createElement("div");
        document.getElementById("mine").appendChild(C);
        //C.style = 'transform: scale(0.65); position: relative; top: -100px;';
        C.appendChild(document.createElement("br"));
        let q = document.createElement("h3");
        C.appendChild(q);
        q.textContent = questions[i].question;
        for (let j = 0; j < questions[i].choices.length; j++){
            a = document.createElement("div");
            a.style ="padding: 10px";
            lab = document.createElement("label");
            lab.for =i.toString()+j.toString();
            lab.style='padding:5px;'
            lab.innerText=questions[i].choices[j];
            choice = document.createElement("input");
            C.appendChild(choice);
            C.appendChild(lab);
            choice.type='radio';
            choice.className = 'choice';
            choice.name=i.toString();
            choice.id=i.toString()+"+"+j.toString();
            style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;';
            C.appendChild(document.createElement("br"));
        }
        document.createElement("hr");
    }
    for (let i = 0; i < questions2.length; i++) {
        let C = document.createElement("div");
        document.getElementById("theirs").appendChild(C);
        //C.style = 'transform: scale(0.65); position: relative; top: -100px;';
        //C.appendChild(document.createElement("br"));
        let q = document.createElement("h3");
        C.appendChild(q);
        q.textContent = questions2[i].question;
        q.question_id = questions2[i].question_id;
        for (let j = 0; j < questions2[i].choices.length; j++){
            a = document.createElement("div");
            a.style ="padding: 10px";
            lab = document.createElement("label");
            lab.for =i.toString()+j.toString()+"t";
            lab.style='padding:5px;'
            lab.innerText=questions2[i].choices[j];
            choice = document.createElement("input");
            C.appendChild(choice);
            C.appendChild(lab);
            choice.type='radio';
            choice.name=i.toString()+"t";
            choice.id=i.toString()+"+"+j.toString()+"t";
            choice.className = 'choice';
            choice.question_id=questions2[i].question_id;
            choice.index = j;
            choice.mine = false;
            style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;';
            C.appendChild(document.createElement("br"));
        }
        document.createElement("hr");
    }
}

function getResponses(){
    let answers = document.getElementsByClassName('choice');
    let myResponses = [];
    let myGuesses = [];
    for (let i = 0; i < answers.length; i++){
        if (answers[i].checked){
            let id = answers[i].id;
            let questionID = id[0];
            let answerID = id[2];
            resp = {};
            resp.questionID = questionID;
            resp.answerID = answerID;
            if (id.length > 3) {
                myGuesses.push(resp);
            } else {
                myResponses.push(resp)
            }

        }
    }
    console.log(myResponses);
    console.log(myGuesses);
}