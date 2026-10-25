customer = (
    "John Simiyu",
    "CUS101",
    "0712345678",
    "john@example.com"
)

print("Complete Customer Tuple:", customer)
print("Customer Name:", customer[0])
print("Telephone Number:", customer[2])
print("Number of Items:", len(customer))

try:
    customer[2] = "0798765432"
except TypeError:
    print("The telephone number cannot be modified because tuples are immutable.")
