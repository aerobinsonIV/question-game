import database
import random

def get_username(uid):
    if uid:
        db = database.opendb("main")
        results = db.select("users", "username", "id=\"" + uid + "\"")
        db.close()
        return results[0][0]

def check_cookie(uid):
    if uid is None:
        return False
    db = database.opendb("main")
    results = db.select("users", "username", "id=\"" + uid + "\"")
    db.close()
    return len(results) > 0

def get_next_gameid():
    gameid = random.random(0, 999999999)
    print("Generated game ID " + gameid)
    return gameid