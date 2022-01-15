import flask

# API path scripts:
from mom import mom

app = flask.Flask(__name__)

# For all API paths, JSON parsing should happen in this script
# All API functions should take in one parameter which is a dictionary

# Page routes:

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/api-test")
def api_test():
    return flask.render_template("api-test.html")

# API routes:

# curl -d '{"text":"hello"}' -H "Content-Type: application/json" -X POST localhost/api/mom
@app.route("/api/mom", methods=['POST'])
def api_mom():
    return mom(flask.request.get_json())

# This part hosts the whole JS folder or something
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
@app.route('/js/<path:path>')
def send_js(path):
    return flask.send_from_directory('js', path)

