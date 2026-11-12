
import matplotlib.pyplot as plt
import os

from analytics import sales_analytics as analytics


class ChartGenerator:

    def __init__(self, sales_data):

        self.sales = sales_data

        plt.style.use(
            "seaborn-v0_8-pastel"
            if "seaborn-v0_8-pastel" in plt.style.available
            else "default"
        )

    # Common method to save or display charts
    def display_chart(self, save_path=None):

        plt.tight_layout()

        if save_path:

            folder = os.path.dirname(save_path)

            if folder:
                os.makedirs(folder, exist_ok=True)

            plt.savefig(save_path, bbox_inches="tight")
            print(f"Chart saved successfully: {save_path}")

        else:
            plt.show()

        plt.close()

    # 1. Monthly Sales Trend - Line Chart
    def plot_monthly_sales_trend(self, save_path=None):

        monthly_df = analytics.monthly_sales(self.sales)

        if monthly_df is None or monthly_df.empty:
            print("No monthly sales data available.")
            return

        plt.figure(figsize=(10, 5))

        plt.plot(
            monthly_df["Month"],
            monthly_df.iloc[:, 1],
            marker="o",
            color="#2b5c8f",
            linewidth=2.5,
            markersize=6
        )

        plt.title("Monthly Sales Trend", fontsize=14, fontweight="bold")
        plt.xlabel("Month")
        plt.ylabel("Total Sales ($)")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.xticks(rotation=45)

        self.display_chart(save_path)

    # 2. Top 10 Products by Revenue - Bar Chart
    def plot_top_products_revenue(self, save_path=None):

        revenue = analytics.productwise_revenue(self.sales)

        if revenue is None or revenue.empty:
            print("No product revenue data available.")
            return

        top_products = revenue.head(10)

        plt.figure(figsize=(10, 5))

        plt.bar(
            top_products.iloc[:, 0].astype(str),
            top_products["TotalRevenue"],
            color="#4CAF50"
        )

        plt.title("Top 10 Products by Revenue", fontsize=14, fontweight="bold")
        plt.xlabel("Product ID")
        plt.ylabel("Revenue ($)")
        plt.xticks(rotation=45)

        self.display_chart(save_path)

    # 3. Category-wise Sales - Pie Chart
    def plot_category_distribution_pie(self, save_path=None):

        cat_df = analytics.category_wise_sales(self.sales)

        if cat_df is None or cat_df.empty:
            print("No category sales data available.")
            return

        plt.figure(figsize=(7, 7))

        plt.pie(
            cat_df.iloc[:, 1],
            labels=cat_df.iloc[:, 0],
            autopct="%1.1f%%",
            startangle=140,
            shadow=False
        )

        plt.title("Sales Distribution by Category", fontsize=14, fontweight="bold")

        self.display_chart(save_path)

    # 4. Customer Spending - Bar Chart
    def plot_customer_spending(self, save_path=None):

        customer_df = analytics.costumer_spending(self.sales)

        if customer_df is None or customer_df.empty:
            print("No customer spending data available.")
            return

        top_customers = customer_df.head(10)

        plt.figure(figsize=(10, 5))

        plt.bar(
            top_customers.iloc[:, 0].astype(str),
            top_customers["TotalSpent"],
            color="#FF9800"
        )

        plt.title("Top 10 Customers by Spending", fontsize=14, fontweight="bold")
        plt.xlabel("Customer ID")
        plt.ylabel("Total Spending ($)")
        plt.xticks(rotation=45)

        self.display_chart(save_path)

    # 5. Best Selling Products - Bar Chart
    def plot_best_selling_products(self, save_path=None):

        best_products = analytics.best_selling_product(self.sales)

        if best_products is None or best_products.empty:
            print("No product sales data available.")
            return

        top_products = best_products.head(10)

        plt.figure(figsize=(10, 5))

        plt.bar(
            top_products.iloc[:, 0].astype(str),
            top_products["TotalQuantity"],
            color="#9C27B0"
        )

        plt.title("Top 10 Best Selling Products", fontsize=14, fontweight="bold")
        plt.xlabel("Product ID")
        plt.ylabel("Quantity Sold")
        plt.xticks(rotation=45)

        self.display_chart(save_path)
