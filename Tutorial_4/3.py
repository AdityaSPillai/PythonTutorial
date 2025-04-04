class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(f"Model: {self.model}, Year: {self.year}, Price: {self.price}")

car1 = Car("BMW", 2020, 1000000)
car2 = Car("Porche", 2022, 700000)
car1.cost()
car2.cost()