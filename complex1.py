class complex:

    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def shownum(self):
        print(self.real , "  + " , self.imag , " i ")

    def add(self,num2):
        newreal = self.real + num2.real
        newimag = self.imag + num2.imag
        return complex(newreal,newimag)

    def sub(self,num2):
        newreal = self.real - num2.real
        newimag = self.imag - num2.imag
        return complex(newreal,newimag)

    def mul(self,num2):
        newreal = self.real * num2.real - self.imag * num2.imag
        newimag = self.imag * num2.imag + self.imag * num2.real
        return complex(newreal,newimag)


num1 = complex(2,3)
num1.shownum()

num2 = complex(4,3)
num2.shownum()
print("Addition")
num3 = num1.add(num2)
num3.shownum()
print("Subtraction")
num4 = num1.sub(num2)
num4.shownum()
print("Multiplication")
num5 = num1.mul(num2)
num5.shownum()

