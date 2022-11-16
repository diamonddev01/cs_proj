def ver(n):
  if n > 3 or n < 1:
    return "Invalid"
  
  return "Thank You" if n == 1 else "Well done" if n == 2 else "Correct"

print(ver(int(input("Enter a number")))) # TASK 7

def f():
  _1 = int(input("Enter your first number"))
  _2 = int(input("Enter your second number"))
  
  print(f"{_2}  {_1}" if _1 > _2 else f"{_1}  {_2}")

f() # TASK 1
