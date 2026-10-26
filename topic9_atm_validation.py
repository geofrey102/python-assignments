withdrawal_input = input("Enter withdrawal amount: ")

try:
    withdrawal_amount = int(withdrawal_input)
    print(f"Withdrawal Amount: KSh {withdrawal_amount:,}")
except ValueError:
    print("Invalid amount. Please enter a number.")
