class Triangle:
    def __init__(self, b, h):
        self.b = b
        self.height = h
        print("Создано")

    def area(self):
        return self.b * self.height * 0.5

tr1 = Triangle(13, 3)
print(tr1.area())
