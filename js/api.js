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
        return response.text();
    });
}
