"""
create a file placementcountcasestudy.py
store last 6 month placementcounts as 10,15,22,9,17,18

q) display feb month placementcount 

q) update jan month placementcount as 12

q) display placementcounts where count > 15

q) display highestplacementcount without using max()

q) display lowestplacementcount without using min()

q) display secondhighestplacement_count without using sorted()

"""

placement_count_case_study=[10,15,22,9,17,18]

print("========Feb Month Count========")
feb_month=placement_count_case_study[1]
print("feb month count=",feb_month)


print("======update jan month======")
placement_count_case_study[0]=12
print("jan month count=",placement_count_case_study)


print("=======count=======")
for count in placement_count_case_study:
    if count>15:
        print("count>15=",count)

print("======Highest======") 
max_count=placement_count_case_study[0] #10 15
for count in placement_count_case_study:#10 
    if count>max_count: #10>10 15>10 
        max_count=count
print("highest=",max_count)   


print("======Lowest======")
min_count=placement_count_case_study[0]
for count in placement_count_case_study:
    if count<min_count:
        min_count=count
print("lowest=",min_count)        

print("=======second highest=======")
first_max=0
second_max=0

for count in placement_count_case_study:
    if count>first_max:
        second_max=first_max
        first_max=count
    elif count>second_max:
        second_max=count 
print("second highest",second_max)           








