import mysql.connector


def opendb(name):
    if name == "questiongame" or name == "main":
        return Database("questiongame")
    return None


class Database:

    def __init__(self, name):
        self.db = mysql.connector.connect(
            host='localhost',
            user='python',
            passwd='!nnov4tion',
            database=name
        )
        self.cursorObject = self.db.cursor()
        self.open = True

    def close(self):
        self.db.close()
        self.open = False

    def select(self, rownames, tablename):
        if not self.open:
            raise Exception("database is not open!")

        rowstr = ""

        if type(rownames) is str:
            rowstr = rownames
        else:
            for row in rownames:
                rowstr += row
                rowstr += ", "
            rowstr = rowstr[:-2]

        self.cursorObject.execute("SELECT " + rowstr + " FROM " + tablename)
        return self.cursorObject.fetchall()
