def is_prime(number):
    for i in range(2,number):
        if number%i==0:
            print("False")
            break

    else:
            print("True")

is_prime(7)  
is_prime(11)          
