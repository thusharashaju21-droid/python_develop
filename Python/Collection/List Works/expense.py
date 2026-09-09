expense=[12000,13000,15000,16000,17000,18000]
#          0     1     2     3     4     5
#          i


print("=======15000expenses=======")
#display all expenses one by one
march_month_expense=expense[2]
print(march_month_expense)

print("======update jan month======")
#update jan month expense as 15000
expense[0]=15000
print(expense)


print("===========index===========")
for i in range(0,len(expense)):
    print(expense[i])

print("===========in============")
for amount in expense:
    print(amount)   

 