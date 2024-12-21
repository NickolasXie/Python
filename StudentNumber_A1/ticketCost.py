totalCost = 0;
# converting the weight value to float
weight = float(input("Enter the weight of your luggage in kilograms: "))
difference = weight - 20
# boolean for determining extra charge based on user input's weight
if difference>0:
    totalCost = round(120 + difference*0.015, 2)
else:
    totalCost = 120
print(f"The total cost will be ${totalCost}.")
