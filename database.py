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

    def select(self, tablename, rownames, condition="true"):
        if not self.open:
            raise Exception("Database is not open!")

        rowstr = ""

        if type(rownames) is str:
            rowstr = rownames
        else:
            for row in rownames:
                rowstr += row
                rowstr += ", "
            rowstr = rowstr[:-2]

        self.cursorObject.execute("SELECT " + rowstr + " FROM " + tablename + " WHERE " + condition)
        return self.cursorObject.fetchall()

    def insert(self, tablename, vals, varnames=None):
        if not self.open:
            raise Exception("Database is not open!")

        valsstr = ""

        if type(vals) is str:
            valsstr = vals
        else:
            for val in vals:
                valsstr += val
                valsstr += ", "
            valsstr = valsstr[:-2]

        varstr = ""

        if varnames is not None:
            if type(varnames) is str:
                varstr = "(" + varnames + ")"
            else:
                for val in varnames:
                    varstr += val
                    varstr += ", "
                varstr = "(" + varstr[:-2] + ")"

        self.cursorObject.execute("INSERT INTO " + tablename + " " + varstr + " VALUES " + valsstr)

    def rawCommand(self, command):
        self.cursorObject.execute(command)
        return self.cursorObject.fetchall()

    def update(self, tablename, setting, condition):
        if not self.open:
            raise Exception("Database is not open!")

        settingstr = ""

        if type(setting) is str:
            settingstr = setting
        elif type(setting) is tuple:
            settingstr = setting[0] + "=" + setting[1]
        else:
            for val in setting:
                settingstr += val
                settingstr += ", "
            settingstr = settingstr[:-2]

        self.cursorObject.execute("UPDATE " + tablename + " SET " + settingstr + " WHERE " + condition)
