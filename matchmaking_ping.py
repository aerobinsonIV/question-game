import flask
import util

logged_in_users = []

def matchmaking_ping(uid):

    username = util.get_username(uid)
    print(username + " is looking for a match")

    ready = 0
    other_username = 0

    if(len(logged_in_users) != 0):
        ready = 1
        other_username = logged_in_users[0]
        logged_in_users.clear()
    else:
        logged_in_users.append(username)

    response = {
        "ready": ready,
        "partner": other_username
    }

    return flask.jsonify(response)