#print((18/100)*100)
#print((18/100)*250)
numbers= [100,250,500,800]

result = [num+((18/100)*num) for num in numbers]

print(result)