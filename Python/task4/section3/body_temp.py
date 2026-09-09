temp = float(input("Enter body temperature: "))

if temp < 36:
    print("Low")
elif temp <= 37.5:
    print("Normal")
else:
    print("Fever")