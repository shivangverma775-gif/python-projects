class Animal:
    pass
class pet(Animal):
    pass

class Dog(pet):
    @staticmethod
    def bark():
        return "Woof!"

d = Dog()
print(d.bark())