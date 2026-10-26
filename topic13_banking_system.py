class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited KSh {amount:,.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance. Withdrawal cancelled.")
        else:
            self.balance -= amount
            print(f"Withdrawn KSh {amount:,.2f}")

    def displayAccount(self):
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print(f"Updated Balance: KSh {self.balance:,.2f}")
        print()

def performTransaction(account, transaction_type):
    try:
        amount = float(input(f"Enter amount to {transaction_type}: "))

        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)
    except ValueError:
        print("Invalid transaction amount. Please enter a number.")

account1 = BankAccount("ACC001", "Alice Wanjiku", 20000)
account2 = BankAccount("ACC002", "Brian Otieno", 15000)

print("Transaction for Alice:")
performTransaction(account1, "deposit")

print("Transaction for Brian:")
performTransaction(account2, "withdraw")

account1.displayAccount()
account2.displayAccount()

f = open("accounts.txt", "w")

for account in [account1, account2]:
    print(f"Account Number: {account.account_number}", file=f)
    print(f"Customer Name: {account.customer_name}", file=f)
    print(f"Updated Balance: KSh {account.balance:.2f}", file=f)
    print(file=f)

f.close()

print("Account details saved to accounts.txt.")
