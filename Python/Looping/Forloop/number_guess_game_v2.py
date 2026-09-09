from random import randint

print("Welcome to number guessing name")
secret_number=randint(1,20)
for attempt in range(1,5):
    number=int(input("guess the number"))
    if number==secret_number:
        print("Congrulatioons")
        break
    elif number <=secret_number:
        print("Too low")
    elif number>=secret_number:
        print ("Too high")
    else:
        print("")    
