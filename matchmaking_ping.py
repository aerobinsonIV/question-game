import flask

logged_in_users = []

def matchmaking_ping(uid):

    print("uid " + uid + " is looking for a match")

    ready = 0
    other_uid = 0

    if(len(logged_in_users) != 0):
        ready = 1
        other_uid = logged_in_users[0]
        logged_in_users.clear()
    else:
        logged_in_users.append(uid)

    response = {
        "ready": ready,
        "other-player-uid": other_uid
    }

    return flask.jsonify(response)