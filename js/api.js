async function asyncFunction(){

    text = document.getElementById("coolTextBox").value

    var opts = {
        method: 'POST',
        headers: {
          "Content-Type":"application/json"
        },
        // `` quotes allow us to insert stuff into the string with ${}
        body:`{"text":"${text}"}`
      };

    let url = 'api/mom';

    fetch(url, opts).then((response) => {
        // return response.json();
        return response.text();
    }).then((body) => {
        outputText = document.getElementById("text");
        console.log(body);
        outputText.innerHTML = body;
        // console.log(body)
        // callback(body);
    });
}
