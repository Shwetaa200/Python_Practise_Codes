class calculator:
    n = int(input("Enter the number"))

    def __init___(self,n):
        self.n = n

    def square(self):
        square = self.n*self.n
        print(square)

    def cube(self):
        cube = self.n*self.n*self.n
        print(cube)

a = calculator()
a.square()
a.cube()