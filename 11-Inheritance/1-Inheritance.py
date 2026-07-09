class Employee: #Parent class
    company = "Google"
    name = "Shivang"
    salary = 5000000
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
    
class Programmer(Employee): #Inherited class or child class
    company = "Microsoft"
    language = "Python"
    def getLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")

a = Employee()
b = Programmer()

print(a.company,b.company,b.language)

b.show()
b.getLanguage()




