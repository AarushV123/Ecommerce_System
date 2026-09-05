class Order:
    def __init__(self, order_id, customer_id, product_id, quantity, order_date, total_amount):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.order_date = order_date
        self.total_amount = total_amount

    def display(self):
        print(
            f"OrderID: {self.order_id}, Customer ID: {self.customer_id}, product ID: {self.product_id}, Quantity: {self.quantity}, Order Date: {self.order_date}, Amount: {self.total_amount}"
        )

    def to_dict(self):
        return {
            "OrderID": self.order_id,
            "Customer ID": self.customer_id,
            "product ID": self.product_id,
            "Amount": self.total_amount,
            "Quantity": self.quantity,
            "Order Date": self.order_date,
        }