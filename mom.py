import flask

def mom(request):
    request_text = request.get_json()['text']

    response_body = {
        "text": f"{request_text} you're mom"
    }

    return flask.jsonify(response_body)