import database

def get_username(uid):
    db = database.opendb("main")
    results = db.select("users", "username", "id=\"" + uid + "\"")
    db.close()
    return results[0][0]