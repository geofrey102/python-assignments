class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def displayAccount(self):
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print(f"Current Balance: KSh {self.balance:,.2f}")

account = BankAccount("ACC001", "Alice Wanjiku", 10000)

account.deposit(5000)
account.withdraw(2000)
account.displayAccount()
