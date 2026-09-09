attendance = ["p","p","a","a","o","o","h"]
attendence_set=set(attendance)
attendence_count={}
for a in attendence_set:
    attendence_count[a] = attendance.count(a)
print(attendence_count)    