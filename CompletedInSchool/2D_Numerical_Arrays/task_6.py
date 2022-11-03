from array import *
numbers = array('i', [int(input("Enter a number")), int(input("Enter a number")), int(input("Enter a number")), int(input("Enter a number")), int(input("Enter a number"))])
print(sorted(numbers))
remove = int(input("What number do you want to remove"))
numbers.remove(remove)
print(sorted(numbers))