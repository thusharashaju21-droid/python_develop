sleep = int(input("Enter sleep hours: "))

if sleep < 6:
    print("Sleep Deprived")
elif sleep <= 8:
    print("Healthy Sleep")
else:
    print("Oversleeping")