import datetime
import pytz


class Accounts:
    """Simple class with balance"""

    @staticmethod
    def _current_time():
        utc_time = pytz.utc.localize(datetime.datetime.now())
        return utc_time

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transactions = [(Accounts._current_time(), self._balance)]
        print("Account created for", self._name, "with balance", self._balance)

    def deposit(self, amount):
        if amount > 0:
            self._transactions.append((Accounts._current_time(), amount))
            self._balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if self._balance >= amount > 0:
            self._balance -= amount
            self._transactions.append((Accounts._current_time(), amount * -1))
        else:
            print("Amount above account balance")
        self.show_balance()

    def show_balance(self):
        print("Your balance is {}".format(self._balance))

    def show_transactions(self):
        for date, amount in self._transactions:
            if amount > 0:
                tran_type = "Credited"
            else:
                tran_type = "Debited"
                amount *= -1
            print("{} was {} on {}".format(amount, tran_type, date))


if __name__ == "__main__":
    chirag = Accounts("Bangera", 0)
    chirag.deposit(100)
    chirag.withdraw(100)
    chirag.show_transactions()

    ban = Accounts("Bangera", 800)
    ban.deposit(200)
    ban.withdraw(100)
    ban.show_transactions()
