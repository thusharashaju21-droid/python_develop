num = int(input("Enter a number: "))
last_digit=num%10

if last_digit%2==0:
    print("Last digit is Even")
else:
    print("Last digit is Not Even")