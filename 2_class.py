class Rectangle:
    def __init__(self, a, b):
        self.aside = a
        self.bside = b
    def calculate_perimeter(self):
        return self.aside* 2 + 2 * self.bside

class Square:
    def __init__(self, a):
        self.a = a
    def calculate_perimeter(self):
        return self.a *4

a_rectangle = Rectangle (3, 5)
a_square = Square(4)
print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())
