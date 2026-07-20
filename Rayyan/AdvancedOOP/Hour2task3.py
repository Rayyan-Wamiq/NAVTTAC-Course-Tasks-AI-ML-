class University:
    class Department:
        def __init__(self, name, head_of_department):
            self.name = name
            self.head_of_department = head_of_department

        def info(self):
            return f' "Department: {self.name} HOD: {self.head_of_department}" '

    def __init__(self,University_name):
        self.University_name = University_name
        self.department = []

    def add_department(self, name, head_of_department):
        self.department.append(University.Department(name, head_of_department))

Uni = University("SSUET")
Uni.add_department("Software Engineering","Sir Naseem")
Uni.add_department("Computer Engineering","Sir Imran Saleem")
for Department in Uni.department:
    print(Department.info())
