def is_armstrong_number(number):
    digit_count = len(str(number))
    orginal_number=number
    total=0
    while number!=0:
        digit=number%10
        exponent=digit**digit_count
        total=total+exponent
        number=number//10
    print(orginal_number==total)
is_armstrong_number(123)    



