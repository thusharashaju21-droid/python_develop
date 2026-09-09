steps = int(input("Enter daily steps: "))

if steps < 5000:
    print("Sedentary")
elif steps < 10000:
    print("Moderately Active")
else:
    print("Active")