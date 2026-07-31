class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock = int(stock)

    def display(self):
        print(f"'product ID: '{self.product_id}, 'category:' {self.name}, 'price: '{self.price}, 'stock: '{self.stock}")

    def to_dict(self):
        return {
            "ProductID": self.product_id,
            "ProductName": self.name,
            "Category": self.category,
            "Price": self.price,
            "Stock": self.stock
        }
