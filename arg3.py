#Default argument on mutable datatypes

def details(name="Janhavi", age=20):
    print(f"Name is {name} and age is {age}")
details("shweta",21)
details()
print(details.__defaults__)
details()
print(details.__defaults__)

print("-------------------------------------------------------------------------------------------")

def add_item(name,employee_data=[]):
    employee_data.append(name)
    print(f"Updated Data is:  {employee_data}")

add_item("Vijaya")
print(add_item.__defaults__)
add_item("Trimbak")
print(add_item.__defaults__)
add_item("Pramod")
print(add_item.__defaults__)
add_item("Rekha")
print(add_item.__defaults__)
add_item("Gaurav")
print(add_item.__defaults__)
add_item("Shweta")
print(add_item.__defaults__)
add_item("Karan")
print(add_item.__defaults__)

print("---------------------------------------------------------------------------")

def add_item(name,employee_data=None):
    if(employee_data is None):
        employee_data=[]
    employee_data.append(name)
    print(f"Updated Data is:  {employee_data}")

add_item("Vijaya")
print(add_item.__defaults__)
add_item("Trimbak")
print(add_item.__defaults__)
add_item("Pramod")
print(add_item.__defaults__)
add_item("Rekha")
print(add_item.__defaults__)
add_item("Gaurav")
print(add_item.__defaults__)
add_item("Shweta")
print(add_item.__defaults__)
add_item("Karan")
print(add_item.__defaults__)



