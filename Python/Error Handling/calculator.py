num1= int(input("Enter a num1"))
num2= int(input("Enter a num2"))

operations= input("select operation + - * / ")

result=0 

try:


    if operations =="+" :

        result = num2+num1


    elif operations =="-" :

        result = num2-num1    


    elif operations =="*" :

        result = num2*num1    

    elif operations =="/" :

        result = num2/num1    

    else:

        print("invalid operation ")

except Exception as e:

    print(e)

else:

    print(result)    