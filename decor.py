def decor(func):
    def inner():
        func()
        print("Welcome")
    return inner

def hello():
    print("Welcome")
    print("Welcome")

inner = decor(hello)
inner()