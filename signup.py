import flask
import database as data


def signup(request_json):
    
    response = {"status": 0}
    username = request_json['username']
    password = request_json['password']
    email = request_json['email']

    print("useranem is " + username)
    print("password is " + password)
    print("email is " + email)

    db = data.opendb("main")
    results = db.select("users", "*", "username=\"" + username + "\"")

    if len(results) is not 0:
        response["status"] = 1
        return flask.jsonify(response)

    results = db.select("users", "*", "email=\"" + email + "\"")

    if len(results) is not 0:
        response["status"] = 2
        return flask.jsonify(response)

    db.insert("users", [username, password, email], ["username", "password", "email"])

    return flask.jsonify(response)
