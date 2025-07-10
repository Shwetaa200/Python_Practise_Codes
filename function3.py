# Returning function from function

def display():
    print("Hello")
    def printer():
        print("Welcome!")
    return printer

# printer = display() #printer
# printer()
d= display()
d()