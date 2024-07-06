class Accounts:
    """Simple class with balance"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for", self.name)

    def deposit(self, amount):
        self.balance += amount
        return "Your updated balance for acc {} is {}".format(self.name, self.balance)


chirag = Accounts("Chirag", 100000)
print(chirag.balance)

print(chirag.deposit(5000))
print(chirag.balance)
