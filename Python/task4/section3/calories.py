calories = int(input("Enter calories: "))

if calories < 1500:
    print("Low")
elif calories <= 2500:
    print("Balanced")
else:
    print("Excess")