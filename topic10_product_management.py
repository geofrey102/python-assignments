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

product = Product()
product.setProductDetails("Laptop", "PROD001", 75000, 4)
product.calculateStockValue()
product.displayProductDetails()
