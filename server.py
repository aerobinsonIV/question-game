from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# This part hosts the whole JS folder or something
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")