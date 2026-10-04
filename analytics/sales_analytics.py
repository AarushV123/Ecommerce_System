import pandas as pd
def load_scores_data():
    sales = pd.read_csv("data/sales.csv")
    sales["SaleDate"] = pd.to_datetime(sales["SaleDate"],errors="coerce")

    return sales

def analyze_sales(sales):
    total = sales["TotalAmount"].sum()
    print("Total sales:", total)

    return total

def monthly_sales(sales):
    sales["Month"] = sales["SaleDate"].dt.to_period("M")
    monthly = (sales.groupby("Month")["TotalAmount"].sum().reset_index())
    monthly["Month"] = monthly["Month"].astype(str)
    print(monthly)
    return monthly

def best_selling_product(sales):
    best_products = (sales.groupby("ProductID")["Quantity"].sum().sort_values(ascending=False).reset_index())
    best_products = best_products.rename(columns={"Quantity": "TotalQuantity"})
    print(best_products)
    return best_products

def costumer_spending(sales):
    customer_spends = (sales.groupby("CustomerID")["TotalAmount"].sum().sort_values(ascending=False).reset_index())
    customer_spends = customer_spends.rename(columns={"TotalAmount": "TotalSpent"})
    print(customer_spends)
    return customer_spends

def productwise_revenue(sales):
    product_revenue = (sales.groupby("productID")["TotalAmount"].sum().sort_values(ascending=False).reset_index())
    product_revenue = (product_revenue.rename(columns={"TotalAmount": "TotalRevenue"}))
    print(product_revenue)
    return product_revenue

def category_wise_sales(sales, products):
    merged_sales = sales.merge(products[["ProductID", "Category"]], on="ProductID", how="inner")
    cat_sales = (
        merged_sales.groupby("Category")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    print(cat_sales)
    return cat_sales

#explore different pandas things