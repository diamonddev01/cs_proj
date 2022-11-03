import math

def calculatePitVolume(radius, height):
  return math.pi * (radius ** 2) * height

def calculateBallVolume(radius):
  return math.pi * (radius ** 3)

# All measurements are in cm
BallPitRadius = int(input("Radius (Pit)"))
BallPitHeight = int(input("Height (Pit)"))
BallRadius = int(input("Radius (Ball)"))

BallVolume = calculateBallVolume(BallRadius)
PitVolume = calculatePitVolume(BallPitRadius, BallPitHeight)

print(str(math.ceil(PitVolume / BallVolume)) + ' balls will be required')