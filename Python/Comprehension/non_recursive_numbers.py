arr=[10,11,1,10,11,2,3]
unique_number=[num for num  in arr if arr.count(num)==1]
print("unique number",unique_number)

#set
duplicate_number={num for num in arr if arr.count(num)>1}
print("duplicate number",duplicate_number)

