#comprehension  - it is an easy way for creating a collection from sequence

#list
#[returm value iteration condition]
arr=[2,3,4,5,6,7,8]

squares=[num**2 for num in arr]
print("square",squares)

cube=[num**3 for num in arr]
print("cube",cube)

add_five=[num+5 for num in arr]
print("add five",add_five)

#condition 
evens=[num for num in arr if num%2==0]
print("even",evens)

odds=[num for num in arr if num%2!=0]
print("odd",odds)

num_greather_than_5=[num for num in arr if num>5]
print("greather than five",num_greather_than_5)