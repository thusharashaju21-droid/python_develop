num1=int(input("Enter a number"))
num2=int(input("Enter a number"))

option =input ("enter option min or max")

match option:

 case "min":
        if num1<num2:
                print("minumum is num1",num1)
        else:
             print("minumum is num2",num2)
 case "max":        
        if num1>num2:
            print("maximum is num1",num1)
        else:
          print("maximum is num2",num2)
             