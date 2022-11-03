def Discount(Total, Rate):
  return Total - (Total * Rate/100)

num1 = int(input("What is your starting value"))
num2 = int(input("What discount would you like to apply"))

print(Discount(num1, num2))