num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
operation=input("enter operation add,subtract,divide,multiple,divide,")

match operation:
    case "add": 
        print(num1+num2)
    case "subtract": 
        print(num1-num2)
    case "divide":
        print(num1/num2) 
    case "multiple": 
      print(num1*num2)
    case _:
        print("INVALID")

