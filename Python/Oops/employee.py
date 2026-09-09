class Employee:
    id:int
    name:str
    salary:int
    phone:int
    department:str

    def __init__(self,id,name,salary,phone,department):

        self.id=id
        self.name=name
        self.salary=salary
        self.phone=phone
        self.department=department

    def get_employee(self):

        print(self.id,self.name,self.salary,self.phone,self.department)

employee1=Employee(101,"Thushara",45000,"8891369580","IT")
employee2=Employee(102,"Sooraj",50000,7012219886,"Generalist")

employee1.get_employee()
employee2.get_employee()