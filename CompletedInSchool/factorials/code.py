import math
import textwrap

def convertMultiLine(n, w = 10):
  nStr = str(n)
  strA = textwrap.wrap(nStr, w)
  wrap = "\n".join(strA)
  return wrap

toCalc = int(input('Factorial of? '))
charPerLine = int(input("Line Length (50) "))
charPerLine = charPerLine if charPerLine else 50

fac = math.factorial(toCalc)

print(convertMultiLine(fac, charPerLine))
print(len(str(fac)), 'char long (' + str(math.ceil(len(str(fac)) / charPerLine)), ' lines)')