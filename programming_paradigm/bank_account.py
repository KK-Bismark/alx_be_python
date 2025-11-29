# BankAccount class that encaspulated bannking operations.


class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance = 0

    # function that handles depositing of money into the bank account.
    def deposit(self, amount):
        self.account_balance += amount

    # function that handles withdrawal of money
    def withdraw(self, amount):
        self.account_balance -= amount

    # function that handles the displaying of the account balance.
    def display_balance(self):
        return f"Current Balance: {self.account_balance}"
