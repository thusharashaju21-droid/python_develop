year = int(input("Enter a year: "))

if year % 100 != 0 and year % 4 == 0:
    print("True")
else:
    print("False")