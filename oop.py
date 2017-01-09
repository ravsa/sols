class Customer(object):

    bank = "SBI"

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            raise RuntimeError("Amount greater than the available bal")
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    @staticmethod
    def location():
        return "Jaipur"

    @classmethod
    def

c = Customer('ravindra', 100)
print c.location()
