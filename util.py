import database

def get_username(uid):
    db = database.opendb("main")
    results = db.select("users", "*", "user_id=\"" + uid + "\"")
    db.close
    return results