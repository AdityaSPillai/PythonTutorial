class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def dataprint(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

s1 = Student("Adith", 10)
s2 = Student("Aditya", 14)
s3 = Student("Aljo", 23)
s1.dataprint()
s2.dataprint()
s3.dataprint()