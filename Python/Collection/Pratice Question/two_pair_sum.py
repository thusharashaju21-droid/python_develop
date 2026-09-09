arr=[2,3,4,5,11]
#    n
target=16

 #method1
# 2 stable 3,4,5,11 add (repeat)
for n1 in arr:
    for n2 in arr:
        total=n1+n2
    if total==target and n1!=n2:
        print(n1,n2)
        break    

 #method2 
 # target- n  to check array value
for n in arr:
    difference=target-n
    if difference in arr and difference!=n:
        print(difference,n)
        break   

