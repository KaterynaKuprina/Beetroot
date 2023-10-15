class Dog:
    def __init__(self, human):
        self.age_factor = 7
        self.human = human

    def human_age(self):
        return self.human * self.age_factor


dog = Dog(3)

print(dog.human_age())