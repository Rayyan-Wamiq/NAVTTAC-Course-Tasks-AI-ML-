class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def Intrduce(self):
        print("Hi I am",self.name,"and My grade is",self.grade)
Student1 = Student("Rayyan","A")
Student2 = Student("Muneeb","B")
print(Student1.name,Student1.grade)
print(Student2.name,Student2.grade)
Student1.Intrduce() 
