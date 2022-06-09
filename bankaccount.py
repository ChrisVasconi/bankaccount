

class BankAccount:
    bank_name = "First national Bank"
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient funds:Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self

    def user_account(self, user):
        self.user_account = user


citi = BankAccount(0.01, 0)
pnc = BankAccount(0.10, 0)
citi.deposit(100)
citi.yield_interest()
citi.withdraw(250)
print(citi.balance)
pnc.display_account_info()
pnc.deposit(50)
pnc.yield_interest()
pnc.withdraw(450)
print(pnc.balance)
pnc.display_account_info()
