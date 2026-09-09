age=int(input("enter a age:"))

if age>18:
    test=input("if test passed yes /no" )
    if test=="yes":
        print("License Approved")
    else:
        print("Test not cleared") 
else:
    print("not eligible due to age")
