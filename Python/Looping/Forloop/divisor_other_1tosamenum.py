num=int(input("Enter a number"))
for i in range(2,num+1):
    if num%i==0 and i!=0:
        print(i)
        break
    else:
        print("no divisor exit")

