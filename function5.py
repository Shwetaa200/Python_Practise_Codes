# Higher Order function

def add(n1,n2):
    return n1+n2

def display(func):
    def func():
        print("code here")
    return func

display(add)
a=add(10,20)
print(a)