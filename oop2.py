class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,pin,mob_no):
        self.name = name
        self.salary = salary
        self.pin = pin
        self.mob_no = mob_no

shweta = Programmer("Shweta ",1200000,424344,9403839276)
print("Employee Information")
print("**********************************************")
print("NAME   SALARY    PIN      MOB_NO")
print(shweta.name,shweta.salary,shweta.pin,shweta.mob_no)
        