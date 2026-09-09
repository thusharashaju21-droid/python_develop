num=int(input("enter a number"))
match num:
    case 1 : 
        print("One")
    case 2 : 
        print("Two")
    case 3 :
        print("Three")
    case 4 :
        print("Four")
    case 5 :
        print("Five")
    case _: 
       print("Invalid")