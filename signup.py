import flask
import database
def signup(request_json):

    response = {"status": 0}
    username = request_json['username']
    password = request_json['password']
    email = request_json['email']

    print(f"Added user {username}")

    db = database.opendb("main")
    results = db.select("users", "*", "username=\"" + username + "\"")

    if len(results) is not 0:
        response["status"] = 1
        return flask.jsonify(response)

    results = db.select("users", "*", "email=\"" + email + "\"")

    if len(results) is not 0:
        response["status"] = 2
        return flask.jsonify(response)

    db.insert("users", [username, password, email], ["username", "password", "email"])

    db.close()

    return flask.jsonify(response)
