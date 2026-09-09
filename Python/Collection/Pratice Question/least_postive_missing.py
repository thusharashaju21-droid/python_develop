#missing number
arr=[1,2,3,4,6]
#    0 1 2 3 4
#          p c (-1)
#method1
max_num=max(arr)
total =0
for num in range(1,max_num+1):
    total+=num
current_arr_sum=sum(arr) 
difference=total-current_arr_sum   
print(difference)

#method2
arr.sort()
for p in range(0,len(arr)-1):
    c=p+1
    diiference=arr[c]-arr[p]
    if diiference!=1:
        print("missing is",arr[p]+1)
        break
