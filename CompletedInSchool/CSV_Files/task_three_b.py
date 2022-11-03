import csv

authName = input("What author do you want to search?")

found = False

file = open("Books.csv")
reader = csv.reader(file)
for row in reader:
    authorName = row[1][1:]
    if authorName.lower() == authName.lower():
        found = True
        print(row[0] + ', written in ' + row[2])

if not found:
    print('No results could be found')