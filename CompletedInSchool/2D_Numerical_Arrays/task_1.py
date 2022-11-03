from array import *

nums = array('i', [])
while(len(nums) < 5):
  num = int(input("Enter a whole number"))
  nums.append(num)

nums = sorted(nums)
nums.reverse()
print(nums)