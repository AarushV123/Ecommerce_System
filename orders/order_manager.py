import csv
from config import ORDER_FILE
from orders.order import Order
from sales.sales_manager import SalesManager


class OrderManager:
    def __init__(self):
        self.sales_manager = SalesManager()

    def load_orders(self):
        orders = []
        try:
            with open(ORDER_FILE, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    order = Order(
                        row.get("OrderID"),
                        row.get("CustomerID") or row.get("Customer ID"),
                        row.get("productID") or row.get("product ID"),
                        row.get("Quantity"),
                        row.get("Order Date") or row.get("SaleDate"),
                        row.get("TotalAmount") or row.get("Amount"),
                    )
                    orders.append(order)
        except FileNotFoundError:
            pass
        return orders

    def save_orders(self, orders):
        with open(ORDER_FILE, "w", newline="", encoding="utf-8") as file:
            fieldnames = [
                "OrderID",
                "CustomerID",
                "productID",
                "Quantity",
                "Order Date",
                "TotalAmount",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for order in orders:
                writer.writerow(order.to_dict())

    def add_order(self):
        orders = self.load_orders()
        order_id = input("Enter order_id: ").strip()
        for o in orders:
            if getattr(o, "order_id", None) == order_id or getattr(o, "OrderID", None) == order_id:
                print("Order ID already exists.")
                return

        customer_id = input("Enter customer_id : ").strip()
        product_id = input("Enter product_id : ").strip()
        quantity = input("Enter quantity: ").strip()
        order_date = input("Enter order_date: ").strip()
        total_amount = input("Enter total_amount: ").strip()

        new_order = Order(
            order_id, customer_id, product_id, quantity, order_date, total_amount
        )
        orders.append(new_order)
        self.save_orders(orders)
        
        self.sales_manager.record_sale(new_order)
        print("Order Added and Sale Recorded Successfully.")

    def view_orders(self):
        orders = self.load_orders()
        if not orders:
            print("There are no orders found.")
        else:
            for order in orders:
                order.display()

    def search_order(self):
        search_id = input("Enter Order ID : ").strip()
        orders = self.load_orders()
        for item in orders:
            order_id = getattr(item, "order_id", getattr(item, "OrderID", None))
            if order_id == search_id:
                item.display()
                return
        print("Order Not Found")

    def update_order(self):
        orders = self.load_orders()
        user_input = input("What order would you like to update : ").strip()
        for o in orders:
            order_id = getattr(o, "order_id", getattr(o, "OrderID", None))
            if order_id == user_input:
                o.customer_id = input("Enter customer_id : ").strip()
                o.product_id = input("Enter product_id : ").strip()
                o.quantity = input("Enter quantity: ").strip()
                o.order_date = input("Enter order_date: ").strip()
                o.total_amount = input("Enter total_amount: ").strip()
                self.save_orders(orders)
                print("Order Updated Successfully.")
                return

        print("Order not found")

    def delete_order(self):
        orders = self.load_orders()
        user_input = input("What order would you like to remove: ").strip()
        for o in orders:
            order_id = getattr(o, "order_id", getattr(o, "OrderID", None))
            if order_id == user_input:
                orders.remove(o)
                self.save_orders(orders)
                print("Order Removed")
                return
        print("Order not found")