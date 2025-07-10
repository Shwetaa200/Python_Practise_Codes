class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        """Overloading the + operator for complex number addition"""
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        """Overloading the * operator for complex number multiplication"""
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __str__(self):
        """Overloading str() to display complex numbers properly"""
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"

# Example Usage
c1 = Complex(3, 2)
c2 = Complex(1, 7)

print(f"c1: {c1}")
print(f"c2: {c2}")

# Adding two complex numbers
c3 = c1 + c2
print(f"c1 + c2 = {c3}")

# Multiplying two complex numbers
c4 = c1 * c2
print(f"c1 * c2 = {c4}")
