class Mobile:
    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Company: {self.company}, Model: {self.model}, Price: {self.price}")

m = Mobile()
m.set_details("Samsung", "Galaxy S25", 180000)
m.display_details()