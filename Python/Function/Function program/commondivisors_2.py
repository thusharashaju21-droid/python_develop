def common_divisors(num1,num2):
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            print(i)
common_divisors(12,18)            