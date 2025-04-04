class r:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def a(self):
        return self.length * self.breadth

rect = r(5, 3)
print("Area of Rectangle:", rect.a())