import flask
uids_done = []

def other_player_finished_ping(uid, game_id):
    otherFinished = 0

    if(len(uids_done) == 2):
        otherFinished = 1
    
    response = {
        "finished": otherFinished
    }

    return flask.jsonify(response)

def accept_answers(uid, game_id, request_json):
    print(f"Got answers from uid {uid}, game id {game_id}")
    
    uids_done.append(uid)

    print(f"set uids_done to {str(uids_done)}")

    return other_player_finished_ping(uid, game_id)