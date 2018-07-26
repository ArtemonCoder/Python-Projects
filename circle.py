import math
class Circle:
    def __init__(self, r):
        self.radius = r
        print("Создано")
        
    def area(self):
        return self.radius ** 2 * math.pi
    
ci1 = Circle(13)
print(ci1.area())
