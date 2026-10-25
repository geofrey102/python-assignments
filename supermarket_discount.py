purchase_amount = float(input("Enter total purchase amount: "))

qualifies_for_discount = purchase_amount >= 10000

if qualifies_for_discount:
    discount = 0.15 * purchase_amount
else:
    discount = 0

final_amount = purchase_amount - discount

print(f"Purchase Amount: KSh {purchase_amount:.2f}")
print(f"Discount: KSh {discount:.2f}")
print(f"Final Amount: KSh {final_amount:.2f}")
