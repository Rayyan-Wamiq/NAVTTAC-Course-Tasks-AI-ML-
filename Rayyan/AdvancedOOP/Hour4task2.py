class Shape:
    def area(self):
        return  0
    
    def describe(self):
        print(f"The shape has an area of {self.area()}")
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side**2
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

s1 = Square(7)
c1 = Circle(9)

s1.describe()
c1.describe()