class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def my_salary(self):
        return f'Teacher {self.name} {self.age} years old has a salary {self.salary}'

class Student(Person):
    def __init__(self, name, age, lessons):
        super().__init__(name, age)
        self.lessons = lessons

    def my_lessons(self):
        return f'Teacher {self.name} {self.age} years old has a lesson {self.lessons}'


my_salary = Teacher("Dmitro", 29, 50000)
print(my_salary.my_salary())

my_lessons = Student("Kateryna", 35, "Python")
print(my_lessons.my_lessons())

# Рома, прости)))))
