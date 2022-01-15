from urllib import request
from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api-test")
def api_test():
    return render_template("api-test.html")


# curl -d '{"text":"hello"}' -H "Content-Type: application/json" -X POST localhost/api/mom
@app.route("/api/mom", methods=['POST'])
def api_mom():    
    json = request.get_json()
    return json['text'] + " you're mom \n"

# This part hosts the whole JS folder or something
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

