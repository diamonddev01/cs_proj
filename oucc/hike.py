input_array = []
ar_len = int(input())

for i in range(ar_len):
    data = int(input())
    input_array.append(data)

ARR_LEN = ar_len
DISTANCE_UPHILL = 0

for i in range(ARR_LEN):
    # Reaosn for using range(len()) is number based inumeration
    if (i + 1) == ARR_LEN:
        continue

    __next = input_array[(i + 1)]
    curr = input_array[i]

    if __next > curr:
        DISTANCE_UPHILL += 100

print(DISTANCE_UPHILL)
