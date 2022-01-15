import flask
import database as data


def login(request_json):
    response = {
        "status": 0,
        "username": "",
        "cookie": 0
    }

    email = request_json["email"]
    password = request_json["password"]

    db = data.opendb("main")

    users = db.select("users", ["username", "id"], "email=\"" + email + "\" AND password=\"" + password + "\"")

    if len(users) is 0:
        response["status"] = 1
    else:
        user = users[0]
        response["username"] = user[0]
        response["cookie"] = user[1]  # TODO make a better cookie system omegalol

    db.close()
    return response
