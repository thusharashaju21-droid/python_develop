number=int(input("Enter a number:"))
digit_count=len(str(number))
original_number=number #store number save
total=0
while number!=0:
    digit=number%10
    exponent=digit**digit_count
    total=total+exponent
    number=number//10
if total==original_number:  
     print("Armstrong number")
else:
    print("Not armstrong number")   