age = int(input("enter a age"))

if age < 18:

    raise Exception ("invalid age")

else:

    print("eligible for vote")