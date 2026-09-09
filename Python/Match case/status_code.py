status_code=int(input("enter a status code 2,3,4,5: "))
match status_code:
    case 2: 
        print("success")
    case 3:
        print("redirect")
    case 4:
        print("client server") 
    case 5:
        print("server error") 
    case _:
        print("invalid status code")              
        
        