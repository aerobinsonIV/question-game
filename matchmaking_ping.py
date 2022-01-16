from asyncore import read
import flask
import util

logged_in_users = []

next_game_users = []

users_notified = [0, 0]

def already_in_array(new_uid):
    for uid in logged_in_users:
        if uid == new_uid:
            return True
    return False

def matchmaking_ping(uid):

    print(uid + " is looking for a match")

    ready = 0
    partner = ""

    # If this user isn't already in the array of logged in users, add them
    if not uid in logged_in_users:
        logged_in_users.append(uid)
    
    print("Logged_in_users is " + logged_in_users)

    # Store the pair of users we need to notify
    if len(logged_in_users) >= 2 and len(next_game_users == 0):
        next_game_users[0] = logged_in_users[0]
        next_game_users[1] = logged_in_users[1]

        logged_in_users.remove[0]
        logged_in_users.remove[0]

        print("Next game pairing is " + next_game_users)

    if len(next_game_users) != 0:
        for i, matched_uid in enumerate(next_game_users):
            if uid == matched_uid:
                # Notify this user that they have been matched
                ready = 1
                partner = util.get_username(next_game_users[1 - i]) #Hacky way to get the other element since we know there are only 2
                users_notified[i] = 0

    # If both players have been notified, reset matchmaking stuff
    # TODO: maybe put this after response has been sent?
    if users_notified[0] == 1 and users_notified[1] == 1:
        next_game_users.clear()
        users_notified[0] = 0
        users_notified[1] = 0

    response = {
        "ready": ready,
        "partner": partner
    }

    return flask.jsonify(response)