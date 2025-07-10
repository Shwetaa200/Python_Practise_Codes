# Base class
class Animal:
    def voice(self):
        print("Voice of pet")

# Intermediate class inheriting from Animal
class Pet(Animal):
    pass  # Placeholder since we are not adding anything new

# Derived class inheriting from Pet
class Dog(Pet):
    def voice(self):  # Overriding the voice method
        print("Bark")

# Creating instances
a = Animal()
a.voice()  # Calls method from Animal class

b = Dog()
b.voice()  # Calls overridden method from Dog class
