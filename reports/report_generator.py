import csv
import os
from datetime import datetime
from config import SALES_FILE


class ReportGenerator:

    def __init__(self):
        self.sales_data = []

    def load_sales_data(self):
        """Load sales records from the CSV file."""
        try:
            with open(
                SALES_FILE, "r", newline="", encoding="utf-8"
            ) as file:
                reader = csv.DictReader(file)
                self.sales_data = list(reader)

            print("Sales data loaded successfully.")
            return True

        except FileNotFoundError:
            print("Sales file not found.")
            self.sales_data = []
            return False

        except OSError as error:
            print(f"Error loading sales data: {error}")
            self.sales_data = []
            return False

    def calculate_total_sales(self):
        """Calculate total revenue from sales records."""
        total = 0.0

        for sale in self.sales_data:
            amount = (
                sale.get("TotalSales")
                or sale.get("TotalAmount")
                or sale.get("Amount")
                or "0"
            )

            try:
                total += float(amount)
            except (ValueError, TypeError):
                print(f"Skipping invalid sales amount: {amount}")

        return total

    def count_sales(self):
        """Return the number of sales records."""
        return len(self.sales_data)

    def monthly_sales(self):
        """Calculate revenue grouped by month."""
        monthly_totals = {}

        for sale in self.sales_data:
            date = (
                sale.get("SaleDate")
                or sale.get("Order Date")
                or sale.get("OrderDate")
                or ""
            )

            amount = (
                sale.get("TotalSales")
                or sale.get("TotalAmount")
                or sale.get("Amount")
                or "0"
            )

            try:
                parsed_date = datetime.strptime(
                    date.strip(), "%Y-%m-%d"
                )
                value = float(amount)

                month = parsed_date.strftime("%Y-%m")
                monthly_totals[month] = (
                    monthly_totals.get(month, 0) + value
                )

            except (ValueError, TypeError):
                continue

        return monthly_totals

    def display_report(self):
        """Display a summary report."""
        if not self.sales_data:
            print("No sales data available. Load the data first.")
            return

        print("\n" + "=" * 50)
        print("          SALES SUMMARY REPORT")
        print("=" * 50)

        print(f"Total Sales Records : {self.count_sales()}")
        print(f"Total Revenue      : {self.calculate_total_sales():.2f}")

        print("\nMONTHLY SALES")
        print("-" * 40)

        monthly_data = self.monthly_sales()

        if monthly_data:
            for month, amount in sorted(monthly_data.items()):
                print(f"{month:<15} {amount:>15.2f}")
        else:
            print("No valid monthly sales data found.")

        print("=" * 50)

    def export_report(self, filename="sales_report.txt"):
        """Save the summary report to a text file."""
        if not self.sales_data:
            print("No sales data available.")
            return

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("SALES SUMMARY REPORT\n")
                file.write("=" * 40 + "\n")
                file.write(
                    f"Generated on: {datetime.now():%Y-%m-%d %H:%M}\n"
                )
                file.write(
                    f"Total Sales Records: {self.count_sales()}\n"
                )
                file.write(
                    f"Total Revenue: {self.calculate_total_sales():.2f}\n"
                )

                file.write("\nMONTHLY SALES\n")
                file.write("-" * 40 + "\n")

                for month, amount in sorted(
                    self.monthly_sales().items()
                ):
                    file.write(f"{month}: {amount:.2f}\n")

            print(f"Report exported successfully: {os.path.abspath(filename)}")

        except OSError as error:
            print(f"Error exporting report: {error}")
