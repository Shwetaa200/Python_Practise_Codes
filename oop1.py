class Employee:
    name = "Shweta"
    language = "Python"
    salary = 1200000
    def __init__(self,name,salary,language):
         #dundor method which is automatically call
         self.name = name
         self.salary = salary
         self.language = language
         print("I am creating object")
    def getInfo(self):
        print(f"The name of Employee is {self.name} and the language is {self.language}")
    @staticmethod
    def greet():
        print("Good Morning!!")
shweta = Employee("Karan",5000000,"Sliding Wnidow")
print(shweta.name , shweta.salary)
shweta.getInfo()
shweta.greet()