def leap_years(start,stop):
    for year in range(start,stop+1):
        if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
            print(year)
leap_years(1998,2027)            