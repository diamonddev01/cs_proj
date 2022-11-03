def runTaskTwo():
    newBookName = input("Give the name of a book.")
    newBookAuthour = input("Who wrote " + newBookName + "?")
    newBookReleased = input("When was " + newBookName + " written?")

    file = open("Books.csv", "a")
    newBookData = f"{newBookName}, {newBookAuthour}, {newBookReleased}\n"
    file.write(str(newBookData))

    print(f"Wrote\n{newBookData}\nto: Books.csv")

itemCount = int(input("How many items do you want to add"))
added = 0

while added < itemCount:
    runTaskTwo()
    added += 1