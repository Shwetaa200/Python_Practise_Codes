class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        area= self.length * self.breadth
        print(area)

a = Rectangle(10,20)
a.area()

