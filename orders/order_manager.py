import csv

from config import ORDER_FILE
from orders.order import Order


class OrderManager:
    def load_orders(self):
        orders = []
        try:
            with open(ORDER_FILE, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    order = Order(
                        row["OrderID"],
                        row["Customer ID"],
                        row["product ID"],
                        row["Quantity"],
                        row["Order Date"],
                        row["Amount"],
                    )
                    orders.append(order)
        except FileNotFoundError:
            pass
        return orders

    def save_orders(self, orders):
        with open(ORDER_FILE, "w", newline="", encoding="utf-8") as file:
            fieldnames = [
                "OrderID",
                "Customer ID",
                "product ID",
                "Amount",
                "Quantity",
                "Order Date",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for order in orders:
                writer.writerow(order.to_dict())

    def add_order(self):
        orders = self.load_orders()
        order_id = input("Enter order_id: ")
        for o in orders:
            if o.order_id == order_id:
                print("Order ID already exists.")
                return

        customer_id = input("Enter customer_id : ")
        product_id = input("Enter product_id : ")
        quantity = input("Enter quantity: ")
        order_date = input("Enter order_date: ")
        total_amount = input("Enter total_amount: ")

        new_order = Order(
            order_id, customer_id, product_id, quantity, order_date, total_amount
        )
        orders.append(new_order)
        self.save_orders(orders)
        print("Order Added Successfully.")

    def view_orders(self):
        orders = self.load_orders()
        if len(orders) == 0:
            print("There are no orders found")
        else:
            for order in orders:
                order.display()

    def search_order(self):
        search_id = input("Enter Order ID : ")
        orders = self.load_orders()
        for item in orders:
            if item.order_id == search_id:
                item.display()
                return
        print("Order Not Found")

    def update_order(self):
        orders = self.load_orders()
        user_input = input("What order would you like to update : ")
        for o in orders:
            if o.order_id == user_input:
                o.customer_id = input("Enter customer_id : ")
                o.product_id = input("Enter product_id : ")
                o.quantity = input("Enter quantity: ")
                o.order_date = input("Enter order_date: ")
                o.total_amount = input("Enter total_amount: ")
                self.save_orders(orders)
                print("Order Updated Successfully.")
                return

        print("Order not found")

    def delete_order(self):
        orders = self.load_orders()
        user_input = input("What order would you like to remove: ")
        for o in orders:
            if o.order_id == user_input:
                orders.remove(o)
                self.save_orders(orders)
                print("Order Removed")
                return
        print("Order not found")