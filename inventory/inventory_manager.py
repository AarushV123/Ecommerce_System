
import csv
from config import PRODUCT_FILE
from inventory.inventory import InventoryItem


class InventoryManager:
    def load_inventory(self):
        """Loads all products as InventoryItem objects."""
        items = []
        try:
            with open(PRODUCT_FILE, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    item = InventoryItem(
                        row.get("ProductID"),
                        row.get("ProductName"),
                        row.get("Stock", 0),
                    )
                    items.append(item)
        except FileNotFoundError:
            print("Error: Product data file not found.")
        return items

    def check_availability(self, product_id, requested_qty):
        """Checks if the requested quantity is available in stock."""
        try:
            with open(PRODUCT_FILE, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row.get("ProductID") == str(product_id):
                        current_stock = int(row.get("Stock", 0))
                        if current_stock >= int(requested_qty):
                            return True, current_stock
                        else:
                            return False, current_stock
        except FileNotFoundError:
            print("Error: Product file not found.")
        return False, 0

    def deduct_stock(self, product_id, ordered_qty):
        """Deducts ordered quantity from product stock upon order completion."""
        products = []
        updated = False

        try:
            with open(PRODUCT_FILE, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row.get("ProductID") == str(product_id):
                        current_stock = int(row.get("Stock", 0))
                        new_stock = max(0, current_stock - int(ordered_qty))
                        row["Stock"] = str(new_stock)
                        updated = True
                    products.append(row)

            if updated:
                with open(PRODUCT_FILE, "w", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(products)
                return True
        except FileNotFoundError:
            print("Error: Product file not found.")
        return False

    def get_low_stock_items(self, threshold=5):
        """Returns items where stock is at or below the warning threshold."""
        items = self.load_inventory()
        return [item for item in items if item.stock <= threshold]
