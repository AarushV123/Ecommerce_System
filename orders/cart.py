
class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product_id, product_name, price, quantity=1):
        if price < 0:
            print("Price cannot be negative.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if product_id in self.items:
            self.items[product_id]["quantity"] += quantity
        else:
            self.items[product_id] = {
                "product_name": product_name,
                "price": price,
                "quantity": quantity
            }

        print("Product added to cart successfully.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return

        print("\n" + "=" * 70)
        print("SHOPPING CART")
        print("=" * 70)

        print(
            f"{'Product ID':<15}"
            f"{'Product Name':<20}"
            f"{'Price':<10}"
            f"{'Quantity':<10}"
            f"{'Subtotal':<10}"
        )

        print("-" * 70)

        for product_id, item in self.items.items():
            subtotal = item["price"] * item["quantity"]

            print(
                f"{product_id:<15}"
                f"{item['product_name']:<20}"
                f"{item['price']:<10.2f}"
                f"{item['quantity']:<10}"
                f"{subtotal:<10.2f}"
            )

        print("-" * 70)
        print(f"Total Amount: {self.calculate_total():.2f}")

    def update_quantity(self, product_id, quantity):
        if product_id not in self.items:
            print("Product not found in cart.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        self.items[product_id]["quantity"] = quantity
        print("Cart quantity updated successfully.")

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            print("Product removed from cart.")
        else:
            print("Product not found in cart.")

    def calculate_total(self):
        total = 0

        for item in self.items.values():
            total += item["price"] * item["quantity"]

        return total

    def clear_cart(self):
        self.items.clear()
        print("Cart cleared successfully.")

    def get_items(self):
        return self.items.copy()
