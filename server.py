import flask
import endgame
from get_questions import get_questions

# API path scripts:
from mom import mom
from signup import signup
from login import login
from matchmaking_ping import matchmaking_ping
import util

app = flask.Flask(__name__)

# For all API paths, JSON parsing should happen in this script
# All API functions should take in one parameter which is a dictionary

# Page routes:

def page_if_logged_in(render_template_line):
    cookie = flask.request.cookies.get("login_cookie")
    if util.check_cookie(cookie):
        return render_template_line
    else:
        return flask.render_template("redirect.html")

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
    return flask.render_template("login.html") #TODO IF YOU ARE ALREADY LOGGED IN, REDIRECT TO MATCHMAKING

@app.route("/matchmaking")
def matchmaking_page():
    return page_if_logged_in(flask.render_template("matchmaking.html", username=util.get_username(flask.request.cookies.get("login_cookie"))))

@app.route("/chat")
def chat_page():
    return page_if_logged_in(flask.render_template("chat.html"))

@app.route("/questions")
def questions_page():
   return page_if_logged_in(flask.render_template("questions.html"))

@app.route("/results")
def results_page():
    return page_if_logged_in(flask.render_template("results.html"))

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

@app.route("/api/matchmaking-ping")
def api_matchmaking_ping():
    return matchmaking_ping(flask.request.cookies.get("login_cookie"))

@app.route("/api/questions")
def api_get_questions():
    return get_questions(flask.request.cookies.get("game_id"), 5)

@app.route("/api/answers", methods=['POST'])
def api_accept_answers():
    return endgame.accept_answers(flask.request.cookies.get("login_cookie"), flask.request.cookies.get("game_id"), flask.request.get_json())

@app.route("/api/other-player-finished-ping")
def api_other_player_finished_ping():
    return endgame.other_player_finished_ping(flask.request.cookies.get("login_cookie"), flask.request.cookies.get("game_id"))


# This part hosts the whole JS folder or something
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
@app.route('/js/<path:path>')
def js(path):
    return flask.send_from_directory('js', path)

@app.route('/css/<path:path>')
def css(path):
    return flask.send_from_directory('css', path)

