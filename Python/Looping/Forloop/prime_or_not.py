is_prime=True
num=int(input("enter a number"))
for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
print("prime")