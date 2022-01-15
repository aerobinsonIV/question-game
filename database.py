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
                if type(val) is str:
                    valsstr += "\"" + val + "\""
                else:
                    valsstr += val
                valsstr += ", "
            valsstr = "(" + valsstr[:-2] + ")"

        varstr = ""

        if varnames is not None:
            if type(varnames) is str:
                varstr = "(" + varnames + ")"
            else:
                for val in varnames:
                    varstr += val
                    varstr += ", "
                varstr = "(" + varstr[:-2] + ")"

        query = "INSERT INTO " + tablename + " " + varstr + " VALUES " + valsstr
        self.cursorObject.execute(query)
        self.db.commit()

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
            temp = setting[1]
            if type(temp) is str:
                temp = "\"" + temp + "\""
            settingstr = setting[0] + "=" + temp
        else:
            for val in setting:
                temp = val[1]
                if type(temp) is str:
                    temp = "(" + temp + ")"
                settingstr += val[0] + "=" + temp + ", "
            settingstr = settingstr[:-2]

        query = "UPDATE " + tablename + " SET " + settingstr + " WHERE " + condition
        print(query)

        self.cursorObject.execute(query)
        self.db.commit()
