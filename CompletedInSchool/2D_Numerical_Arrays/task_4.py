from array import *
from random import randint

repeated = randint(10, 300)
arr = array('i', [repeated, randint(10, 300), randint(10, 300), repeated, randint(10, 300)])

print(arr)

checkFor = int(input("What number do you want to find"))
repeates = 0
for x in arr:
  if x == checkFor:
    repeates += 1

print(repeates)