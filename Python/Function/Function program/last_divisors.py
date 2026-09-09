num=int(input("Enter a number"))
#last_divisor=1
for i in range(1,num):
    if num%i==0:
        last_divisor=i
print(last_divisor)
