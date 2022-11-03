import csv

# Year
StartingYear = int(input("Starting Year"))
EndingYear = int(input("Ending Year"))

found = False

file = open("Books.csv")
reader = csv.reader(file)
for row in reader:
    year = row[2][1:]
    if int(year) >= StartingYear and int(year) <= EndingYear:
        found = True
        print(row[0] + ', written in ' + row[2][1:] + ' by ' + row[1][1:])

if not found:
    print('No results could be found')