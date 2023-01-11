intagersInError = int(input(""))
errorCodes = input("").split()
numberOfCodes = int(input(""))

errorCount = 0

for i in range(numberOfCodes):
    code = int([*input()][0])
    for i in range(len(errorCodes)):
        if code == int(errorCodes[i]):
            errorCount += 1

print(errorCount)