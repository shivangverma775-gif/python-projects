class programmer:
    def __init__(self, name, department, company):
        self.name = name
        self.department = department
        self.company = company

Employee1 = programmer("Shivang", "It", "Google")
Employee2 = programmer("Alice", "Account", "Microsoft")

print(Employee1.name, Employee1.department, Employee1.company)
print(Employee2.name, Employee2.department, Employee2.company)