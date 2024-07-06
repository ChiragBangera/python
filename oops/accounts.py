class Accounts:
    """Simple class with balance"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for", self.name, "with balance", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            self.show_balance()
        else:
            print("Amount above account balance")

    def show_balance(self):
        print("Your balance is {}".format(self.balance))


if __name__ == "__main__":
    chirag = Accounts("Bangera", 0)
    chirag.deposit(1000000)

    chirag.withdraw(1000001)
