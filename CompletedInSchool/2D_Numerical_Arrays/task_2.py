from array import *
from random import randint

nums = array('i', [randint(1, 300), randint(1, 300), randint(1, 300), randint(1, 300), randint(1, 300)])

# Re-organise
nums = sorted(nums)

for x in nums:
  print(x)