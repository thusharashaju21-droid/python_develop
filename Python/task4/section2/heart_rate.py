rate = int(input("Enter heart rate: "))

if rate < 60:
    print("Low")
elif rate <= 100:
    print("Normal")
else:
    print("High")