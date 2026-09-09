num = int(input("Enter a number: "))

while num > 0:
    digit = num % 10
    cube = digit ** 3
    print("Cube of", digit, "=", cube)
    num = num // 10