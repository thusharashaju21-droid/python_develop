def gcd_of_two(num1,num2):
    gcd=1
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            gcd=i
    print(gcd)
gcd_of_two(12,24)        
gcd_of_two(18,24)
