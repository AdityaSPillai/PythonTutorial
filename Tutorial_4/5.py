class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

p1 = Person("Adith", 20, 60000)
p2 = Person("Aditya", 21, 80000)
p3 = Person("Aljo", 23, 50000)
p1.display()
p2.display()
p3.display()