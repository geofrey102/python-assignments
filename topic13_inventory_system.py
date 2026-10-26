class Product:
    def __init__(self):
        self.name = ""
        self.code = ""
        self.price = 0.0
        self.quantity = 0

    def setProductDetails(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    def calculateStockValue(self):
        return self.price * self.quantity

    def displayProductDetails(self):
        print("Product Name:", self.name)
        print("Product Code:", self.code)
        print(f"Price: KSh {self.price:,.2f}")
        print("Quantity:", self.quantity)
        print(f"Stock Value: KSh {self.calculateStockValue():,.2f}")
        print()

products = []

for number in range(1, 4):
    print(f"Enter details for product {number}")
    name = input("Product name: ")
    code = input("Product code: ")

    while True:
        try:
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("Invalid price or quantity. Please enter numeric values.")

    product = Product()
    product.setProductDetails(name, code, price, quantity)
    products.append(product)

total_stock_value = 0

for product in products:
    product.displayProductDetails()
    total_stock_value += product.calculateStockValue()

print(f"Total Stock Value: KSh {total_stock_value:,.2f}")

f = open("inventory.txt", "w")

for product in products:
    print(f"Product Name: {product.name}", file=f)
    print(f"Product Code: {product.code}", file=f)
    print(f"Price: KSh {product.price:.2f}", file=f)
    print(f"Quantity: {product.quantity}", file=f)
    print(f"Stock Value: KSh {product.calculateStockValue():.2f}", file=f)
    print(file=f)

print(f"Total Stock Value: KSh {total_stock_value:.2f}", file=f)

f.close()

print("Inventory details saved to inventory.txt.")
