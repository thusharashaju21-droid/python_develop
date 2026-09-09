
stress = int(input("Enter stress level (1-10): "))

if stress <= 3:
    print("Low Stress")
elif stress <= 6:
    print("Moderate Stress")
else:
    print("High Stress")