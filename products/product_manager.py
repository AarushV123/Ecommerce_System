import csv
from config import PRODUCT_FILE
from products.product import Product

class ProductManager:
    def load_products(self):
        products=[]
        try:  
            with open(PRODUCT_FILE, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    product = Product(row["ProductID"], row["ProductName"], row["Category"], row["Price"], row["Stock"])
                    products.append(product)
        except FileNotFoundError:
            pass
        return products
    
    def save_products(self, products):
        with open(PRODUCT_FILE, "w", newline="") as file:
            fieldnames = [
                "ProductID",
                "ProductName",
                "Category",
                "Price",
                "Stock"
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for product in products:
                writer.writerow(product.to_dict())
