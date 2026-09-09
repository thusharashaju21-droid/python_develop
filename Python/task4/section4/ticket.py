age = int(input("Enter age: "))

if age < 5:
    print("Free")
elif age <= 18:
    print("Fare = ₹10")
elif age <= 60:
    print("Fare = ₹20")
elif age>60:
    print("Fare=15")
else:
    print("invalid")