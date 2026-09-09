#single
"""
Common 2D Shapes and Formulas
Rectangle:Multiply length (l) by width (w) (A = l × w)
Square: Multiply the side length (a) by itself (A = a²)
Circle: Multiply pi (π) by the radius squared (A = π r²)
Parallelogram: Multiply base (b) by vertical height (h) (A = bh).
Trapezium: Add parallel sides (a + b), multiply by height (h), and divide by two (\(A = \frac{1}{2}(a + b)h\2)).
"""
class Shape:

    name:str

    def __init__(self,name):

        self.name=name

class Parallelogram(Shape):

    base:int
    height:int 

    def __init__(self, name,base,height):
        super().__init__(name)   
        self.base=base
        self.height=height

    def area(self):

        print("area of",self.name,"=",self.base*self.height)

p_instance=Parallelogram("Parallelogram",12,24)

p_instance.area()

class Rectangle(Shape):
    length=int
    width=int
    def __init__(self,name,length,width):
        super().__init__(name)
        self.length=length
        self.width=width

    def area(self):
        print("area of",self.name,"=",self.length*self.width)    

r_instance =Rectangle("Rectangle",10,5) 

r_instance.area()
        
class Square(Shape):
    side:str

    def __init__(self, name,side):
        super().__init__(name)
        self.side=side

    def area(self):
        print("area of",self.name,"=",self.side**2)

s_instance=Square("Square",8)            
s_instance.area()

class Circle(Shape):
    radius:int

    def __init__(self, name,radius):
        super().__init__(name)
        self.radius=radius

    def area(self):
        print("area of",self.name,"=",3.14*self.radius*self.radius) 

c_instance=Circle("Circle",7)         
c_instance.area()

class Trapezium(Shape):
    side1=int
    side2=int
    height=int

    def __init__(self, name,side1,side2,height):
        super().__init__(name)
        self.side1=side1
        self.side2=side2
        self.height=height

    def area(self):
        print("area of",self.name,"=",self.side1+self.side2*self.height/2)    

t_instance=Trapezium("Trapezium",10,20,3)
t_instance.area()

