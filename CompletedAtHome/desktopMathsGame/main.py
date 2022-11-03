import tkinter as tk
import Config as conf
import random
import database
import math

# Variables
qs = 1
pts = 0
toAsk = conf.questions

window = tk.Tk()
window.title("Super cool maths game")
window.geometry(str(conf.width) + 'x' + str(conf.height))
window.configure(bg="black", highlightcolor="white")


def createQuestion():
    number1 = 0
    number2 = 0

    types = ['*', '+', '/', '-']
    type = types[random.randint(0, 3)]

    if type == '*':
        number1 = random.randint(1, 20)
        number2 = random.randint(1, 12)
    elif type == '+' or type == '-':
        number1 = random.randint(1, 1000)
        number2 = random.randint(1, 1000)
    else:
        number1 = random.randint(1, 200)
        number2 = random.randint(1, 12)

    ans = round(eval(f"number1 {type} number2") * 100) / 100

    v = {
        "q": f"{number1}{type}{number2}",
        "a": ans
    }

    return v


def submit():
    global uLabel
    global entryBox
    global question
    global pts
    global qs
    global extraLabel

    correct = False

    content = entryBox.get()
    answer = question['a']
    contents_as_number = float(content)
    content_rounded = math.floor(contents_as_number * 100) / 100
    answer_rounded = math.floor(answer * 100) / 100

    if content_rounded == answer_rounded:
        pts += 1
        correct = True

    qs += 1

    if qs > toAsk:
        #  END
        response = database.saveScore(pts)
        uLabel.destroy()
        uLabel = tk.Label(text=response)
        uLabel["bg"] = "black"
        uLabel["fg"] = "white"
        uLabel.place(x=conf.width / 2 - (300 / 2), y=conf.height / 2 - 25 - (25 / 2), width=300, height=25)

        extraLabel.destroy()
        extraLabel = tk.Label(text=f"{f'Correct answer was {answer_rounded}' if not correct else ''}")
        extraLabel["bg"] = "black"
        extraLabel["fg"] = "white"
        extraLabel.place(x=conf.width / 2 - (300 / 2), y=conf.height / 2 - 50 - (25 / 2), width=300, height=25)

        entryBox.destroy()
        submitButton.destroy()

        return

    question = createQuestion()

    uLabel.destroy()
    uLabel = tk.Label(text=f"Question {(qs - 1)} | {question['q']} To Two DP | {pts}/{(qs - 1)} ({pts/(qs - 1) * 100 if (qs - 1) >= 1 else 0}%)")
    uLabel["bg"] = "black"
    uLabel["fg"] = "white"
    uLabel.place(x=conf.width / 2 - (300 / 2), y=conf.height / 2 - 25 - (25 / 2), width=300, height=25)
    entryBox.delete(0, tk.END)
    extraLabel.destroy()
    extraLabel = tk.Label(text=f"{f'Correct answer was {answer_rounded}' if not correct else ''}")
    extraLabel["bg"] = "black"
    extraLabel["fg"] = "white"
    extraLabel.place(x=conf.width / 2 - (300 / 2), y=conf.height / 2 - 50 - (25 / 2), width=300, height=25)


question = createQuestion()
uLabel = tk.Label(text=f"Question 1 | {question['q']} To Two DP | {pts}/{qs - 1} ({pts/(qs - 1) * 100 if (qs - 1) >= 1 else 0}%)")
uLabel["bg"] = "black"
uLabel["fg"] = "white"
uLabel.place(x=conf.width / 2 - (300 / 2), y=conf.height / 2 - 25 - (25/2), width=300, height=25)

extraLabel = tk.Label(text="")
extraLabel["bg"] = "black"
extraLabel["fg"] = "white"
extraLabel.place(x=conf.width / 2 - (300 / 2), y=conf.height / 2 - 50 - (25/2), width=300, height=25)

entryBox = tk.Entry()
entryBox.place(x=conf.width / 2 - (300 / 2), y=conf.height / 2 - (25 / 2), width=300, height=25)
entryBox.focus_set()  # Ensures the entryBox is selected.

submitButton = tk.Button(text="Submit", command=submit)
submitButton["bg"] = "black"
submitButton["fg"] = "white"
submitButton.place(x=conf.width / 2 - (300 / 2), y=conf.height / 2 + 25 - (25/2), width=300, height=25)

window.mainloop()
