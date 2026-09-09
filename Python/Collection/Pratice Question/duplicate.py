arr = [10,1,15,16,11,10,12,11]

duplicate = set()

#method 1

for i in range(0,len(arr)):

    for j in range(0,len(arr)):
      
      if arr[i] == arr[j] and i!=j:
         
         duplicate.add(arr[i])

print(duplicate)

#method 2

for num in arr:
   if arr.count(num)>=2:
       duplicate.add(num)
print(duplicate)       






    