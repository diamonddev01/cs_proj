import math
import random
import database

# random = random.randInt(mn, mx)

def createQuestion():
  #number1 = random.randint(1, 100)
  #number2 = random.randint(1, 100)
  
  number1 = 0
  number2 = 0
  
  types = ['*', '+', '/', '-']
  type = types[random.randint(0, 3)]
  
  if type == '*':
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 12)
  elif type == '+' or type == '-':
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)
  else:
    number1 = random.randint(1, 200)
    number2 = random.randint(1, 12)
  
  ans = round(eval(f"number1 {type} number2") * 100) / 100
  
  v = {
    "q": f"{number1}{type}{number2}",
    "a": ans
  }
  
  return v

qs = 0
pts = 0

while qs < 5:
  qdata = createQuestion() 
  ans = float(input(f"What is {qdata['q']} (To two dp)"))
  
  if ans == qdata['a']:
    print('Correct answer :)')
    pts += 1
  else:
    print("Incorrect, the correct answer was", qdata['a'])
  
  qs += 1

# STORE
database.saveScore(pts)