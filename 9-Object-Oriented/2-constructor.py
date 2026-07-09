class Student:
    name = "Shivang"
    sec = "A"
    grade = 10

    def __init__(self, name, sec, grade):#dunder method (which is called automatically when an object is created)
       print("Constructor called")
       self.name = name
       self.sec = sec
       self.grade = grade

d = Student("Alice", "B", 8)
print(d.name, d.sec, d.grade)
    