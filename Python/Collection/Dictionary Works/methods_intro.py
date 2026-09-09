"""
values add (key)
{key:value},dictionary()
{"name":"iphone16","brand":"apple","price":65000}
mutable
ordered
duplicate-key not allowed

methods: 

keys() - all keys display
values() - values display
items() - key & values display
get(key) - key value display (none)-no key



"""

daily_calories={"monday":1500,"tuesday":1800,"wednesday":2000,"thursday":2100,"friday":1900,"saturday":2200,"sunday":1600}
sat_consumed_calorie=daily_calories["saturday"]
print(sat_consumed_calorie)

print("=======update value =======")
daily_calories["friday"]=1700
print(daily_calories)

print("=====All Keys=====")
for k in daily_calories.keys():
    print(k)


print("======All Values======")
for v in daily_calories.values():
    print(v)    

print("=======key and values(items)=======")
for k,v in daily_calories.items():
    print(k,v)


total_calorie=daily_calories.get("total",0) #0 -default value
print(total_calorie)   

print("======total======")
total_calorie=0
for v in daily_calories.values():
    total_calorie+=v
print(total_calorie)
daily_calories["total_calorie"]=total_calorie
print(daily_calories)


     

