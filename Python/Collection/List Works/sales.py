sales=[10000,20000,30000,40000,50000,600000]
#        0     1     2     3     4     5

print("=====March month sales=====")

march_mon_sale=sales[2]
print(march_mon_sale)

print("=====Update May month sale 105000=====")

sales[4]=105000
print(sales)


print("====All sales index====")

for i in range(0,len(sales)):
    print(sales[i])

print("=====sales>100000=====") 

for amount in sales:
    if amount>100000:
        print(amount)


