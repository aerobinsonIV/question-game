import database
import random
import math

def get_username(uid):
    if uid:
        db = database.opendb("main")
        results = db.select("users", "username", "id=\"" + uid + "\"")
        db.close()
        if len(results) > 0:
            return results[0][0]

def check_cookie(uid):
    if uid is None:
        return False
    db = database.opendb("main")
    results = db.select("users", "username", "id=\"" + uid + "\"")
    db.close()
    return len(results) > 0

def get_next_game_id():
    game_id = math.floor(random.random() * 10000000000000000)
    print("Generated game ID " + str(game_id))
    return game_id