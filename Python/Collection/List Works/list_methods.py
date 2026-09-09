"""
append(object) appends object at end of the list
insert(index,object) specific index
pop(index) ()- end list remove
remove(value)-first occurance
index(value)- returns index position of first occurance of value
count(value)-return frquency of value
reverse()
sort()
copy() -diiference object
"""
#add color
print("=========add to end===========")
colors=["red","white","blue","purple","black","violet"]
#         0      1       2      3        4        5
colors.append("red")
print(colors)

#insert 
print("=======insert specific index======")
colors.insert(2,"orange")
print(colors)

#remove
print("========remove=======")
colors.pop(4) 
print(colors)
colors.pop() #last list remove
print(colors)

print("=======remove first occurance=======")
colors1=["white","red","white","blue","purple","black","violet"]
colors1.remove("white")
print(colors1)
colors.remove("white")
print(colors)

print("========index position =========")
blue_index=colors.index("blue") 
print(blue_index) 

print("========frequency=========")
white_count=colors1.count("white")
print(white_count)

print("=======reverse=======")
colors.reverse()
print(colors)


print("=====Asending Order,sorted=====")
colors.sort()
print(colors)

print("======Desending order======")
colors.sort(reverse=True)
print(colors)

print("======different=========")
fvrt_food1=["shawarma","mandhi","Biriyani"]
fvrt_food2=fvrt_food1.copy()
fvrt_food2[2]="Loaded Fries"
print(fvrt_food1)
print(fvrt_food2)
