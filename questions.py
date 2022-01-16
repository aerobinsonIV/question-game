import json


def readQuestionsFile(filename):
    allQuestions = []
    with open(filename, "r") as file:
        data = json.load(file)

        for question in data["questions"]:
            answers = []
            for answer in question["answers"]:
                answers.append(answer["value"])

            allQuestions.append(Question(question["question"], answers))

    return allQuestions


class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers
