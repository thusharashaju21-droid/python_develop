arr=[3,5,7,9,11,13,15,4,8,]

prime_number=[]

for num in arr:

    for i in range(2,num):

        if num%i==0:

            break
    else:
        
        prime_number.append(num)

print(prime_number)            