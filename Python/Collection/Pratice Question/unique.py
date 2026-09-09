arr = [10,1,15,16,11,10,12,11]
unique = []
for num in arr:
    if arr.count(num)==1:
        unique.append(num)
print(unique)        