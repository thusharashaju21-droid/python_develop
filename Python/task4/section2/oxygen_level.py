oxygen = int(input("Enter oxygen level: "))

if oxygen >= 95:
    print("Normal")
elif oxygen >= 90:
    print("Mild Concern")
else:
    print("Critical")