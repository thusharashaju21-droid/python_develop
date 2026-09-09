number=int(input("Enter the number"))
x1,y1=10,12
x2,y2=12,14
x3,y3=14,16
slope_one = (y2-y1) / (x2-x1)
slope_two = (y3-y2) / (x3-x2)
if slope_one==slope_two:
    print("points can straight line")
else:
    print("points can't create straight line")   