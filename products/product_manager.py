import csv
from config import PRODUCT_FILE
from products.product import Product


class ProductManager:
    def load_products(self):
        products = []
        try:
            with open(PRODUCT_FILE, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    product = Product(
                        row["ProductID"],
                        row["ProductName"],
                        row["Category"],
                        row["Price"],
                        row["Stock"],
                    )
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
                "Stock",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for product in products:
                writer.writerow(product.to_dict())

    def add_product(self):
        products = self.load_products()
        product_id = input("Enter Product ID : ")
        for p in products:
            if p.product_id == product_id:
                print("Product ID already exists.")
                return
        name = input("Enter Product Name : ")
        category = input("Enter Category : ")
        price = float(input("Enter Price : "))
        stock = int(input("Enter Stock : "))
        new_product = Product(product_id, name, category, price, stock)
        products.append(new_product)
        self.save_products(products)
        print("Product Added Successfully.")

    def view_products(self):
        products = self.load_products()
        if len(products) == 0:
            print("There are no products found")
        else:
            for product in products:
                product.display()
    
    def search_product(self):
        search_id = input("Enter Product ID : ")
        products = self.load_products()
        for item in products:
            if item.product_id == search_id:
                item.display()
                return
        print("Product Not Found")
    
    def update_product(self):
        products = self.load_products()
        user_input = input("What product would you like to update : ")
        for p in products:
            if p.product_id == user_input:
                p.name = input("Enter New Name : ")
                p.category = input("Enter New Category : ")
                p.price = float(input("Enter New Price : "))
                p.stock = int(input("Enter New Stock : "))
                self.save_products(products)
                print("Product Updated Successfully.")
                return
            
        print("Product not found")

    def delete_product(self):
        products = self.load_products()
        user_input = input("What product would you like to remove: ")
        for p in products:
            if p.product_id == user_input:
                products.remove(p)
                self.save_products(products)
                print("Product Removed")
                return
        print("Product not found")
