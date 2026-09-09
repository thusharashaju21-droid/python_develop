age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 59:
    print("Adult")
else:
    print("Senior")