class Sales:
    def __init__(self, order_id, customer_id, product_id, quantity, sale_date, total_amount):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.sale_date = sale_date
        self.total_amount = total_amount

    def display(self):
        print(
            f"Order ID: {self.order_id}, Customer ID: {self.customer_id}, "
            f"Product ID: {self.product_id}, Quantity: {self.quantity}, "
            f"Sale Date: {self.sale_date}, Total Amount: {self.total_amount}"
        )

    def to_dict(self):
        return {
            "OrderID": self.order_id,
            "CustomerID": self.customer_id,
            "ProductID": self.product_id,
            "Quantity": self.quantity,
            "SaleDate": self.sale_date,
            "TotalAmount": self.total_amount,
        }