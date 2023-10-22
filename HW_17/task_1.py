class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Animals can't talk")

class Cat(Animal):
    def talk(self):
        print("Meow")

class Dog(Animal):
    def talk(self):
        print("Woof woof")

animals = [Cat("Harley"), Dog("Marvel")]

for animal in animals:
    animal.talk()