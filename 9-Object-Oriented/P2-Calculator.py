class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num * self.num

    def cube(self):
        return self.num * self.num * self.num

    def square_root(self):
        return self.num ** 0.5

    def cube_root(self):
        return self.num ** (1/3)
    
    @staticmethod
    def greet():
        print("Hello, welcome to the calculator!")

Number = float(input("please enter a number: "))
calc = calculator(Number)
calc.greet()
print("Square:", calc.square())
print("Cube:", calc.cube())
print("Square Root:", round(calc.square_root(), 2))
print("Cube Root:", round(calc.cube_root(), 2))