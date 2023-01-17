INPUT_COUNT = int(input(""))
submissions = []

for i in range(INPUT_COUNT):
    submissions.append(input(""))

def Array(l):
    arr = []
    for _ in range(l):
        arr.append(0)
    
    return arr

FINAL_DATA = Array(10)
current_top = 0


def sort(array, _current_top):
    for element in range(len(array)):
        if array[element] > array[_current_top]:
            _current_top = element   
    return _current_top


for x in submissions:
    numbers = [*x]
    for y in numbers:
        k = int(y)
        FINAL_DATA[k] = FINAL_DATA[k] + 1
    current_top = sort(FINAL_DATA, current_top)

print(current_top)
