import flask

def mom(request_json):
    request_text = request_json['text']
    
    response_body = {
        "text": f"{request_text} you're mom"
    }

    return flask.jsonify(response_body)