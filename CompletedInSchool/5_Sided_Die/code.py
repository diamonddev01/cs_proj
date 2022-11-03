def printLineEnd(isStart):
  if(not isStart):
    print('o       o')
  print('ooooooooo')
  if(isStart):
    print('o       o')
def generateFive():
  print('o #   # o')
  print('o   #   o')
  print('o #   # o')

def printFive():
  printLineEnd(True)
  generateFive()
  printLineEnd(False)

printFive()