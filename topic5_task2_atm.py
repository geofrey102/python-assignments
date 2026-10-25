account_balance = 50000

withdrawal_amount = int(input("Enter withdrawal amount: "))

if withdrawal_amount <= 0:
    print("Error: Withdrawal amount must be greater than zero.")
elif withdrawal_amount > account_balance:
    print("Error: Withdrawal amount exceeds the account balance.")
elif withdrawal_amount % 500 != 0:
    print("Error: Withdrawal amount must be a multiple of KSh 500.")
else:
    account_balance -= withdrawal_amount
    print("Withdrawal successful.")
    print(f"Remaining Balance: KSh {account_balance:,}")
