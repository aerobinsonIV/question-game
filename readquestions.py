import json

filename = input("whats the name of the input file: ")
outputname = input("whats the name of the json file: ")

questions = {"questions": []}

with open(filename, "r") as file:
    lines = file.readlines()

    for line in lines:
        loc = line.find("//")
        print("question: " + line[:loc])
        print("comment: " + line[loc:])

        answers = []
        answer = input("how many answers?")
        for i in range(int(answer)):
            ans = input("answer " + str(i))
            answers.append({"value": ans})

        questions["questions"].append({"question": line[:loc], "answers": answers})

print(questions)

with open(outputname, 'w') as f:
    # where data is your valid python dictionary
    json.dump(questions, f)
