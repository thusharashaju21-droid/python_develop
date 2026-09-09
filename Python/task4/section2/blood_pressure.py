bp = int(input("Enter systolic blood pressure: "))

if bp < 120:
    print("Normal")
elif bp <= 129:
    print("Elevated")
elif bp <= 139:
    print("High BP Stage 1")
else:
    print("High BP Stage 2")