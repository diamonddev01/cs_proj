from array import *
from random import randint

generated = array('i', [randint(1, 5000), randint(1, 5000), randint(1, 5000), randint(1, 5000), randint(1, 5000)])
entered = array('i', [int(input("Enter Number")), int(input("Enter Number")), int(input("Enter Number"))])

for x in generated:
  entered.append(x)

print(sorted(entered))