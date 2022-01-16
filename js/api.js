//All API functions should return a promise that gives a JSON object

async function mom(text){
    var opts = {
        method: 'POST',
        headers: {
        	"Content-Type":"application/json"
        },
        // `` quotes allow us to insert stuff into the string with ${}
        body:`{"text":"${text}"}`
    };

    let url = 'api/mom';

    return fetch(url, opts).then((response) => {
    	return response.json();
    });
}

async function signup(username, email, password){
    // TODO: Add email validation

	var opts = {
		method: 'POST',
		headers: {
			"Content-Type":"application/json"
		},
		body:`{"username":"${username}","email":"${email}","password":"${password}"}`
	};

	let url = 'api/signup';

	return fetch(url, opts).then((response) => {
		return response.json();
	});
}

async function login(email, password){
	var opts = {
		method: 'POST',
		headers: {
			"Content-Type":"application/json"
		},
		body:`{"email":"${email}","password":"${password}"}`
	};

	let url = 'api/login';

	return fetch(url, opts).then((response) => {
		return response.json();
	});
}

async function matchmakingPing(){
	var opts = {
		method: 'GET',
	};

	let url = 'api/matchmaking-ping';

	return fetch(url, opts).then((response) => {
		return response.json();
	});
}

async function getQuestions(){
	var opts = {
		method: 'GET',
	};

	let url = 'api/questions';

	return fetch(url, opts).then((response) => {
		return response.json();
	});
}

