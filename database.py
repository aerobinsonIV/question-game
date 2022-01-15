import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='python',
    passwd='!nnov4tion',
    database='questiongame'
)

cursorObject = db.cursor()

cursorObject.execute("SELECT * FROM users");
results = cursorObject.fetchall();

for x in results:
    print(x)

db.close()
