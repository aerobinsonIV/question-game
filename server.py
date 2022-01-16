import flask

# API path scripts:
from mom import mom
from signup import signup
from login import login
import util

app = flask.Flask(__name__)

# For all API paths, JSON parsing should happen in this script
# All API functions should take in one parameter which is a dictionary

# Page routes:

@app.route("/")
def index_page():
    return flask.render_template("index.html")

@app.route("/api-test")
def api_test():
    return flask.render_template("api-test.html")

@app.route("/signup")
def signup_page():
    return flask.render_template("signup.html")

@app.route("/login")
def login_page():
    return flask.render_template("login.html")

@app.route("/matchmaking")
def matchmaking_page():
    return flask.render_template("matchmaking.html", username=util.get_username(flask.request.cookies.get("login_cookie")))

@app.route("/chat")
def chat_page():
    return flask.render_template("chat.html")

@app.route("/questions")
def questions_page():
    return flask.render_template("questions.html")

@app.route("/results")
def results_page():
    return flask.render_template("results.html")

# API routes:

# curl -d '{"text":"hello"}' -H "Content-Type: application/json" -X POST localhost/api/mom
@app.route("/api/mom", methods=['POST'])
def api_mom():
    return mom(flask.request.get_json())

@app.route("/api/signup", methods=['POST'])
def api_signup():
    return signup(flask.request.get_json())

@app.route("/api/login", methods=['POST'])
def api_login():
    return login(flask.request.get_json())

# This part hosts the whole JS folder or something
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
@app.route('/js/<path:path>')
def js(path):
    return flask.send_from_directory('js', path)

@app.route('/css/<path:path>')
def css(path):
    return flask.send_from_directory('css', path)

