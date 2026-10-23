class InventoryItem:
    def __init__(self, product_id, product_name, stock, low_stock_threshold=5):
        self.product_id = product_id
        self.product_name = product_name
        self.stock = int(stock)
        self.low_stock_threshold = int(low_stock_threshold)

    @property
    def status(self):
        """Returns the current stock health status."""
        if self.stock == 0:
            return "Out of Stock"
        elif self.stock <= self.low_stock_threshold:
            return "Low Stock"
        return "In Stock"

    def display(self):
        print(
            f"Product ID: {self.product_id} | Name: {self.product_name} | "
            f"Stock: {self.stock} | Status: {self.status}"
        )

    def to_dict(self):
        return {
            "ProductID": self.product_id,
            "ProductName": self.product_name,
            "Stock": self.stock,
            "Threshold": self.low_stock_threshold,
        }
