
class Calculator:

    def add(self,num1,num2):
        print(num1,num2)
        
    def add(self,num1,num2,num3):
        print(num1,num2,num3)
    def add(self,num1,num2,num3,num4):
        print(num1,num2,num3,num4)

add_instance=Calculator()

add_instance.add(10,20,30,40)
add_instance.add(10,20,30) #error since doesnot support overloading