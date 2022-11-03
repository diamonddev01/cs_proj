from array import *

numbers = array('i', [])

while len(numbers) < 5:
  number = int(input("Enter a number between 10 and 20"))
  if number < 10 or number > 20:
    print('Out of range')
    continue
  
  numbers.append(number)

print('Thank you')