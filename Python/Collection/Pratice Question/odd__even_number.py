lst=[10,11,12,15,14,17,18]
print("======odds======")
odds=[]
for num in lst:
    if num%2!=0:
       odds.append(num)
print(odds) 

print("=======evens======")
evens=[]
for num in lst:
    if num%2==0:
        evens.append(num)
print(evens)        