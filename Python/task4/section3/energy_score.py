energy = int(input("Enter energy score: "))

if energy <= 3:
    print("Low")
elif energy <= 7:
    print("Moderate")
elif energy <= 10:
    print("High")
else:
    print("invalid")
        