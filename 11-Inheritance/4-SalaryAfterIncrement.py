class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def SalaryAfterIncrement(self, increment):
        self.salary += increment
        return self.salary
    
e = employee("Shivang", 5000000)
print(f"The name of the employee is {e.name} and the salary is {e.salary}")

e.SalaryAfterIncrement(100000)
print(f"After increment, the salary is {e.salary}")