class Arith:
    def read(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

arith = Arith()
arith.read(10, 20)
print("Sum:", arith.add())