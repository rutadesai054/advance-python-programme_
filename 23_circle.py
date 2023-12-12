class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

    def perimeter(self):
        return 2*self.radius*3.14


New_Circle = Circle(89)
print(New_Circle.area())
print(New_Circle.perimeter())
