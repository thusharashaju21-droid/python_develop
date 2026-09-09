year=int(input("Enter a year"))
is_leap=(year%100!=0 and year%4==0) or (year%100==0 and year%4==0)
print(is_leap)