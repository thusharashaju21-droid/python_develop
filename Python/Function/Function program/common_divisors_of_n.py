def common_divisors_of_n(number):
    for i in range(1,number+1):
        if number%i==0:
            print(i)
common_divisors_of_n(20)            