fw = open("Python\\File Operation\\leap_years.txt", "w")

for year in range(1800, 2029):
    if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        fw.write(str(year) + "\n")

print("completed....")

fw.close()
