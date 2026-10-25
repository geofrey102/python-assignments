customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
quantity = int(input("Enter quantity purchased: "))
price = float(input("Enter price per item: "))

# Calculate the total cost by multiplying the quantity by the price per item.
total_cost = quantity * price

print(f"Customer Name: {customer_name}")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Price per Item: KSh {price:.3f}")
print(f"Total Cost: KSh {total_cost:.3f}")
