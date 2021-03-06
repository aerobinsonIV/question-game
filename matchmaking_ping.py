import flask
import util

logged_in_users = []

next_game_users = []

users_notified = [0, 0]

next_game_id = [-1, 0]

def already_in_array(new_uid):
    for uid in logged_in_users:
        if uid == new_uid:
            return True
    return False

def matchmaking_ping(uid):

    print("UID " + uid + " is looking for a match")

    ready = 0
    partner = ""
    game_id = -1

    # If this user isn't already in the array of logged in users, add them
    if (not uid in logged_in_users) and (not uid in next_game_users):
        logged_in_users.append(uid)

    # Store the pair of users we need to notify
    if len(logged_in_users) >= 2 and len(next_game_users) == 0:
        next_game_users.append(logged_in_users[0])
        next_game_users.append(logged_in_users[1])

        del logged_in_users[0:2]

        print("Pairing UIDs " + str(next_game_users))

    if len(next_game_users) != 0:
        
        # TODO: no clue why this has to be an array but it's 3:30am so prolly something dumb
        if next_game_id[0] == -1:
            next_game_id[0] = util.get_next_game_id()
            
        for i, matched_uid in enumerate(next_game_users):
            if uid == matched_uid:
                # Notify this user that they have been matched
                ready = 1
                partner = util.get_username(next_game_users[1 - i]) #Hacky way to get the other element since we know there are only 2
                users_notified[i] = 0
                game_id = next_game_id[0]

    # If both players have been notified, reset matchmaking stuff
    # TODO: maybe put this after response has been sent?
    if users_notified[0] == 1 and users_notified[1] == 1:
        next_game_users.clear()
        users_notified[0] = 0
        users_notified[1] = 0

    response = {
        "ready": ready,
        "partner": partner,
        "game_id": game_id
    }

    return flask.jsonify(response)