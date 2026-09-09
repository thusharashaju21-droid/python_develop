year=2025
while year<=2050:
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(year)
    year=year+1    