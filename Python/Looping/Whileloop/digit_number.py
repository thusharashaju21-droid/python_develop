num=int(input("Enter number:"))
count=0
while num!=0:
    digit=num%10
    count=count+1
    num=num//10
print("count is",count)