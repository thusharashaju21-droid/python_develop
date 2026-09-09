# replace odd numbers with "odd"
numbers=[2,5,8,7,10]
result=["odd" if  num%2!=0 else num for num in numbers]
print(result)