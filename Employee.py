class Employee:
    def __init__(self, name, salary, increment):
        self.name = name
        self.salary = salary
        self.increment = increment  # Increment as a percentage

    @property
    def salary_after_increment(self):
        return self.salary + (self.salary * self.increment / 100)

    def apply_increment(self):
        """Apply increment to salary"""
        self.salary = self.salary_after_increment

    def display(self):
        print(f"Employee: {self.name}, Salary: {self.salary}, Increment: {self.increment}%")

# Example usage
emp1 = Employee("John", 50000, 10)
emp1.display()
print("Salary after increment:", emp1.salary_after_increment)

# Applying increment
emp1.apply_increment()
emp1.display()
