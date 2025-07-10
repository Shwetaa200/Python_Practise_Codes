class Maxfinder:
    def __init__(self,numbers):
        self.numbers= numbers
    def find_max(self):
        if not self.numbers:
            return "List is Empty!"
        return max ( self.numbers)
        
f = Maxfinder([1,2,3,4])
print(f"The Largest number is : {f.find_max()}")
        
