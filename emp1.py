class Employee:
    def __init__(self,name,age,addr,salary):
        self.name = name
        self.age = age
        self.addr = addr
        self.salary = salary
    def person_detail(self):
        print(f"Name of Employee is : {self.name}")
        print(f"Age of Employee is:  {self.age}")
        print(f"Address of Employee is {self.addr}")

    def salary1(self):
        print(f"Salary of Employee is  {self.salary}")

a = Employee("Shweta",21,"Kukana",700000)
a.person_detail()
a.salary1()
