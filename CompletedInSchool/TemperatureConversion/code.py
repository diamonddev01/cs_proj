def CelToFar(cel):
  return (cel * 1.8) + 32
def FarToCel(far):
  return (far / 1.8) - 32

C = 10
F = 30
ConF = CelToFar(C)
ConC = FarToCel(F)

print(C, 'as Far is', ConF)
print(F, 'as Cel is', ConC)