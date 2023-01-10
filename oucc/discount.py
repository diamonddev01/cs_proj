i = int(input(""))
discount = 0

# Calulate Discount
if(i > 50):
    discount += 10
if(i > 100):
    discount += 5
if(i > 200):
    discount += 5

# Return value
final_num = int(i * (1 - (discount / 100)))
print(final_num)