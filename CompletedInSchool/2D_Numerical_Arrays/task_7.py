from array import *
from random import randint

numbers = array('f', [randint(10, 10000)/100, randint(10, 10000)/100, randint(10, 10000)/100, randint(10, 10000)/100, randint(10, 10000)/100, randint(10, 10000)/100, randint(10, 10000)/100, randint(10, 10000)/100, randint(10, 10000)/100, randint(10, 10000)/100, randint(10, 10000)/100, randint(10, 10000)/100, randint(10, 10000)/100])
print(sorted(numbers))

def divideArray(n):
  arr = array('f', [])
  for x in numbers:
    arr.append(x / n)
  
  return arr

out = divideArray(int(input("What would you like to divide by")))
print(sorted(out))