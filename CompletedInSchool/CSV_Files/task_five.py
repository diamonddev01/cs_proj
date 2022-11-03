import csv

file = open("Books.csv")
reader = csv.reader(file)
n = 0
for row in reader:
    print(f"Row {n}: {row[0]} by {row[1][1:]} in {row[2][1:]}")
    n += 1