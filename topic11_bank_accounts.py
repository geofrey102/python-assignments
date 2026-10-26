class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def displayAccount(self):
        print("Account Number:", self.account_number)
        print(f"Balance: KSh {self.balance:,.2f}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculateInterest(self):
        return self.balance * self.interest_rate / 100

savings = SavingsAccount("SAV001", 50000, 5)

savings.displayAccount()
print("Interest Rate:", savings.interest_rate, "%")
print(f"Interest: KSh {savings.calculateInterest():,.2f}")
