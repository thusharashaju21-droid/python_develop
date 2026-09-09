arr = [10,1,15,16,11,10,12,11]
most_frequent =arr[0]
for num in arr:
    if arr.count(num) > arr.count(most_frequent):
        most_frequent = num
print(most_frequent)        