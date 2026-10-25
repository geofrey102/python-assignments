class Book:
    def __init__(self, title, author, price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    def calculate_stock_value(self):
        return self.price * self.copies

    def check_stock(self):
        if self.copies > 0:
            return "In Stock"
        else:
            return "Out of Stock"

book1 = Book("Python Basics", "John Simiyu", 1200, 5)
book2 = Book("Database Systems", "Mary Mueni", 2500, 0)

books = [book1, book2]

for book in books:
    print("Title:", book.title)
    print("Author:", book.author)
    print(f"Stock Value: KSh {book.calculate_stock_value():,.2f}")
    print("Availability:", book.check_stock())
    print()
