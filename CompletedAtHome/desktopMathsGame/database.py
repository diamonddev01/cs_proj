import csv


def getBest():
    file = open("Results.csv")
    reader = csv.reader(file)
    best = 0

    for row in reader:
        if int(row[0]) > best:
            best = int(row[0])

    return best


def saveScore(score):
    best = getBest()

    file = open("Results.csv", "a")
    new_data = f"{str(score)}\n"
    print(str(new_data))
    file.write(str(new_data))

    response = ""

    if score > best:
        response = 'New high score ' + str(score) + '!'
    else:
        response = 'Score: ' + str(score) + '\nHigh Score: ' + str(best)

    return response
