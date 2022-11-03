def calculateEnergyBill(units_used, charge, calorific_value):
  kWh = units_used * 1.022 * calorific_value
  cost = kWh * charge
  
  return cost

charge = None
if bool(input("(True | False) Do you have a specific charge or use default (2.84)? ")):
    charge = int(input("Charge (2.84) "))

chal = None
if bool(input("(True | False) Do you have a specific chalorific value or use default (2.84)? ")):
    chal = int(input("Chalorific Value (39.3) "))

print("£", calculateEnergyBill(int(input("Units Used ")), charge if charge else 2.84, chal if chal else 39.3))