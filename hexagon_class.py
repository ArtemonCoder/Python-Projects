class Hexagon:
    def __init__(self, a, b, c, d, e, f):
        self.aside = a
        self.bside = b
        self.cside = c
        self.dside = d
        self.eside = e
        self.fside = f

    def calculate_perimeter(self):
        return self.aside + self.bside + self.cside + self.dside + self.eside + self.fside

hex1 = Hexagon(1, 2, 3, 4, 5, 6)
print(hex1.calculate_perimeter())
