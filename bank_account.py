class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print(f"Current Balance: KSh {self.balance:,.2f}")

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print(f"Balance: KSh {self.balance:,.2f}")

account = BankAccount("ACC1001", 10000, "25 October 2026", "Alice")

deposited_amount = account.deposit(2000)
print(f"Amount Deposited: KSh {deposited_amount:,.2f}")

withdrawn_amount = account.withdraw(1500)
print(f"Amount Withdrawn: KSh {withdrawn_amount:,.2f}")

account.check_balance()
account.customer_details()
