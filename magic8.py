import random

name = "Nemanja"
question = "Will I have a decent girlfriend?"
answer = ""

try:
    random_number = random.randint(1, 9)
    responses = {
        1: "Yes - definitely",
        2: "It is decidedly so",
        3: "Without a doubt",
        4: "Reply hazy, try again",
        5: "Ask again later",
        6: "Better not tell you now",
        7: "My sources say no",
        8: "Outlook not so good",
        9: "Very doubtful"
    }
    answer = responses.get(random_number, "Error")

    if not name and not question:
        print("You did not input question and name.")
    elif not name:
        print("Question: " + question + "?")
    elif not question:
        print("You should input the question!")
    else:
        print(name + " asks: " + question + "?")
        print("Magic 8-Ball's answer: " + answer)

except Exception as e:
    print("An error occurred:", e)
