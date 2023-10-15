class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        return f"Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old"


person = Person("Dima", "Astapov", 29)
print(person.talk())