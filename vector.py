# Taking user input
n = int(input("Enter the number for n: "))
m = int(input("Enter the number for m: "))
o = int(input("Enter the number for o: "))

# Defining the 2D Vector class
class TwoDvector:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def twovec(self):
        print(f"{self.n}i + {self.m}j")

# Defining the 3D Vector class, inheriting from TwoDvector
class ThreeDvector(TwoDvector):
    def __init__(self, n, m, o):
        super().__init__(n, m)  # Calling parent class constructor
        self.o = o  # Defining the additional third component

    def threevec(self):
        print(f"{self.n}i + {self.m}j + {self.o}k")

# Creating objects with required arguments
p = TwoDvector(n, m)
p.twovec()

q = ThreeDvector(n, m, o)
q.threevec()
