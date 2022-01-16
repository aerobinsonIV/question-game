import flask
uids_done = [-1, -1]

def other_player_finished_ping(uid, game_id):
    otherFinished = 0

    if(uids_done[0] != -1 and uids_done[1] != -1):
        otherFinished = 1
    
    response = {
        "finished": otherFinished
    }

    return flask.jsonify(response)

def accept_answers(uid, game_id, request_json):
    print(f"Got answers from uid {uid}, game id {game_id}")
    
    if(uids_done[0] == -1):
        uids_done[0] == uid
    else:
        uids_done[1] == uid

    print(f"set uids_done to {str(uids_done)}")

    return other_player_finished_ping(uid, game_id)