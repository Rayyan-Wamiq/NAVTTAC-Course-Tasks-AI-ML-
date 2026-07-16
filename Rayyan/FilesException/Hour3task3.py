
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def promote(self):
        self.grade+=1

Student1 = Student("Rayyan",5)
Student2 = Student("Muneeb",7)

print(Student1.promote())
print(Student2.promote())

print(Student1.name,Student1.grade,"Grade:")
print(Student2.name,Student2.grade,"Grade:")