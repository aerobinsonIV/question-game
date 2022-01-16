import json
from urllib import response
import questions

import flask


def get_questions(game_id, num):
    allQuestions = questions.readQuestionsFile("questions.json")
    ret = {"questions": []}
    ids = []

    while len(ids) < num:
        game_id = int(game_id * 8754)
        game_id <<= 2
        game_id = int(game_id % 5000)
        question_id = game_id % len(allQuestions)
        if question_id in ids:
            continue
        ids.append(question_id)

    for myid, i in zip(ids, range(len(ids))):
        add = {"question": allQuestions[myid].question, "answers": [], "question_id": i}

        for answer in allQuestions[myid].answers:
            add["answers"].append({"value": answer})

        ret["questions"].append(add)

    return flask.jsonify(ret)
