# Passing Function As an Argument
# We can pass any valid python objects as an argument to the function.
# since function are valid python objects
# We pass functins as an argument to the other function

def getname():
    nm=input("Enter the First Name: ")
    lm=input("Enter the last name: ")
    return nm + " " + lm

def display(func):
    print(func)

display(getname)

display(getname())
