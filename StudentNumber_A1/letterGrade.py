score = float(input("Enter a real value score between 0.0 and 1.0: "))
# printing error message if user input is out of bounds
if score < 0.0 or score > 1.0:
    print("Error")
# boolean of which interval the user input falls under, must also include the max value it takes
else:
    if score >= 0.9:
        print("A")
    elif score >= 0.8 and score < 0.9: # B's range must be less than 0.9 (non-inclusive), applies for the following intervals as well
        print("B")
    elif score >= 0.7 and score < 0.8:
        print("C")
    elif score >= 0.6 and score < 0.7:
        print("D")
    else:
        print("F")
