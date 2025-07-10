a = int(input("Enter the number1:"))
b = int(input("Enter the number2:"))
class calculator:
    def __init__(self):
        self.a = a
        self.b = b

    def add(self):
        sum = self.a + self.b
        print(sum)

    def sub(self):
        sub = self.a - self.b
        print(sub)

h = calculator()
h.add()
h.sub()