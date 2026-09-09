num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

if num1 > num2 and num1 > num3:
    print("num1 is largest")
elif num2 > num1 and num2 > num3:
    print("num2 is largest")
elif num3 > num1 and num3 > num2:
    print("num3 is largest")
else:
    print("All numbers are equal or two numbers are equal")