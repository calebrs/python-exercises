# get user inputs for the bill cost and the tip percent
bill_cost = int(input("What is the bill? "))
tip_percent = int(input("what is the tip percent? "))

tip = bill_cost * (tip_percent / 100)
total = round(tip + bill_cost, 2)

print(f"The tip is ${tip}")
print(f"The total is ${total}")