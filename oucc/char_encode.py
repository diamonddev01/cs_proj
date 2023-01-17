INPUT = [*input("")]

output = ""
last = ""
last_itterated = 0

def isInBounds(n, a):
    if(n >= len(a)):
        return False
    return True

for k in range(len(INPUT)):
    CHAR = INPUT[k]
    if CHAR == last:
        last_itterated += 1
        if isInBounds(k + 1, INPUT) and INPUT[k + 1] != last:
            output += CHAR + str(last_itterated)
    else:
        last = CHAR
        last_itterated = 1
        if isInBounds(k + 1, INPUT) and INPUT[k + 1] != last:
            output += CHAR + str(last_itterated)

output += str(last) + str(last_itterated)

print(output)