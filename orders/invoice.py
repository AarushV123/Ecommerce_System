from datetime import datetime

class Invoice:
    def __init__(self, order):
        self.order = order

    def generate_invoice(self):
        invoice_number = "INV-" + str(self.order.order_id)
        invoice_date = datetime.now().strftime("%Y-%m-%d")
        total_amount = self.order.total_amount

        print("=" * 50)
        print("             SALES INVOICE")
        print("=" * 50)
        print(f"Invoice Number : {invoice_number}")
        print(f"Invoice Date   : {invoice_date}")
        print(f"Order ID       : {self.order.order_id}")
        print(f"Customer ID    : {self.order.customer_id}")
        print(f"Product ID     : {self.order.product_id}")
        print(f"Quantity       : {self.order.quantity}")
        print(f"Total Amount   : {total_amount}")
        print("=" * 50)

        filename = f"invoice_{self.order.order_id}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Invoice Number: {invoice_number}\n")
            file.write(f"Date: {invoice_date}\n")
            file.write(f"Order ID: {self.order.order_id}\n")
            file.write(f"Customer ID: {self.order.customer_id}\n")
            file.write(f"Product ID: {self.order.product_id}\n")
            file.write(f"Quantity: {self.order.quantity}\n")
            file.write(f"Total Amount: {total_amount}\n")

        print(f"Invoice saved as {filename}")