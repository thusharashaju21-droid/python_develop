chol = int(input("Enter cholesterol: "))

if chol < 200:
    print("Desirable")
elif chol <= 239:
    print("Borderline")
elif chol >= 240:
    print("High")
else:
    print("invalid")    