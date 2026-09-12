import csv
from config import SALES_FILE


class SalesManager:

    def import_orders(self, orders):
        sales = self.load_sales()

        for order in orders:
            sale = {
                "OrderID": order.order_id,
                "CustomerID": order.customer_id,
                "productID": order.product_id,  # Lowercase 'p' matches save_sales fieldnames
                "Quantity": order.quantity,
                "SaleDate": order.order_date,
                "TotalAmount": order.total_amount,
            }
            sales.append(sale)

        self.save_sales(sales)
        print("Existing orders added to sales successfully.")

    def load_sales(self):
        sales = []
        try:
            with open(SALES_FILE, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    sales.append(row)
        except FileNotFoundError:
            pass
        return sales

    def save_sales(self, sales):
        fieldnames = [
            "OrderID",
            "CustomerID",
            "productID",
            "Quantity",
            "SaleDate",
            "TotalAmount",
        ]
        with open(SALES_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for sale in sales:
                sale_dict = sale.to_dict() if hasattr(sale, "to_dict") else sale
                writer.writerow(sale_dict)

    def record_sale(self, order):
        sales = self.load_sales()
        sale_data = order.to_dict() if hasattr(order, "to_dict") else order
        sales.append(sale_data)
        self.save_sales(sales)
        print("Sale recorded successfully.")

    def view_sales(self):
        sales = self.load_sales()
        if not sales:
            print("No sales found.")
            return

        print("\n" + "=" * 70)
        print("SALES RECORDS")
        print("=" * 70)
        for sale in sales:
            print(
                f"Order ID: {sale.get('OrderID')}, "
                f"Customer ID: {sale.get('CustomerID')}, "
                f"Product ID: {sale.get('productID')}, "
                f"Quantity: {sale.get('Quantity')}, "
                f"Date: {sale.get('SaleDate')}, "
                f"Amount: ₹{sale.get('TotalAmount')}"
            )

    def search_sale(self):
        search_id = input("Enter Order ID: ").strip()
        sales = self.load_sales()

        for sale in sales:
            if sale.get("OrderID") == search_id:
                print("\nSale Found")
                print("-" * 40)
                print(f"Order ID     : {sale.get('OrderID')}")
                print(f"Customer ID  : {sale.get('CustomerID')}")
                print(f"Product ID   : {sale.get('productID')}")
                print(f"Quantity     : {sale.get('Quantity')}")
                print(f"Sale Date    : {sale.get('SaleDate')}")
                print(f"Total Amount : ₹{sale.get('TotalAmount')}")
                return

        print("Sale not found.")

    def calculate_total_sales(self):
        sales = self.load_sales()
        if not sales:
            print("No sales available.")
            return

        total = sum(float(sale.get("TotalAmount", 0)) for sale in sales)
        print(f"\nTotal Sales = ₹{total:.2f}")