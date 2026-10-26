product_name = input("Enter product name: ")
quantity_sold = int(input("Enter quantity sold: "))
total_sales = float(input("Enter total sales amount: "))

f = open("sales.txt", "a")

print(
    f"Product: {product_name}, Quantity: {quantity_sold}, "
    f"Total Sales: KSh {total_sales:.2f}",
    file=f
)

f.close()

print("Sales record saved successfully.")

# Append mode adds new records without deleting existing records.
print("Append mode is appropriate because it preserves existing sales records.")
