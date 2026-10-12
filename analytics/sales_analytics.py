import pandas as pd


def load_scores_data():
    try:
        sales = pd.read_csv("data/sales.csv")
        sales.columns = sales.columns.str.strip()

        if "SaleDate" in sales.columns:
            sales["SaleDate"] = pd.to_datetime(sales["SaleDate"], errors="coerce")

        print("Sales data loaded successfully!")
        print("Detected Columns:", list(sales.columns))
        return sales
    except FileNotFoundError:
        print("Error: Could not find 'data/sales.csv'. Please check the file path.")
        return None


def get_column(df, possible_names):
    cols_lower = {col.lower(): col for col in df.columns}
    for name in possible_names:
        if name.lower() in cols_lower:
            return cols_lower[name.lower()]
    return None


def analyze_sales(sales):
    amount_col = get_column(sales, ["TotalAmount", "Amount", "Total"])
    if not amount_col:
        print(f"Error: TotalAmount column not found. Available columns: {list(sales.columns)}")
        return None
    total = sales[amount_col].sum()
    print("Total sales:", total)
    return total


def monthly_sales(sales):
    date_col = get_column(sales, ["SaleDate", "Date"])
    amount_col = get_column(sales, ["TotalAmount", "Amount", "Total"])

    if not date_col or not amount_col:
        print(f"Error: Missing required columns. Available columns: {list(sales.columns)}")
        return None

    sales["Month"] = sales[date_col].dt.to_period("M")
    monthly = sales.groupby("Month")[amount_col].sum().reset_index()
    monthly["Month"] = monthly["Month"].astype(str)
    print(monthly)
    return monthly


def best_selling_product(sales):
    product_col = get_column(sales, ["ProductID", "productID", "product_id", "productid"])
    quantity_col = get_column(sales, ["Quantity", "qty", "quantity"])

    if not product_col or not quantity_col:
        print(f"Error: Could not find Product or Quantity column. Available columns: {list(sales.columns)}")
        return None

    best_products = (
        sales.groupby(product_col)[quantity_col]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    best_products = best_products.rename(columns={quantity_col: "TotalQuantity"})
    print(best_products)
    return best_products


def costumer_spending(sales):
    customer_col = get_column(sales, ["CustomerID", "customerID", "customer_id", "customerid"])
    amount_col = get_column(sales, ["TotalAmount", "Amount", "Total"])

    if not customer_col or not amount_col:
        print(f"Error: Could not find Customer or TotalAmount column. Available columns: {list(sales.columns)}")
        return None

    customer_spends = (
        sales.groupby(customer_col)[amount_col]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    customer_spends = customer_spends.rename(columns={amount_col: "TotalSpent"})
    print(customer_spends)
    return customer_spends


def productwise_revenue(sales):
    product_col = get_column(sales, ["ProductID", "productID", "product_id", "productid"])
    amount_col = get_column(sales, ["TotalAmount", "Amount", "Total"])

    if not product_col or not amount_col:
        print(f"Error: Could not find Product or TotalAmount column. Available columns: {list(sales.columns)}")
        return None

    product_revenue = (
        sales.groupby(product_col)[amount_col]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    product_revenue = product_revenue.rename(columns={amount_col: "TotalRevenue"})
    print(product_revenue)
    return product_revenue


def category_wise_sales(sales, products_df=None):
    if products_df is None:
        try:
            products_df = pd.read_csv("data/products.csv")
            products_df.columns = products_df.columns.str.strip()
        except FileNotFoundError:
            print("Error: Product data file missing for category mapping.")
            return None

    product_col_sales = get_column(sales, ["ProductID", "productID", "product_id", "productid"])
    product_col_prod = get_column(products_df, ["ProductID", "productID", "product_id", "productid"])
    category_col = get_column(products_df, ["Category", "category"])
    amount_col = get_column(sales, ["TotalAmount", "Amount", "Total"])

    if not product_col_sales or not product_col_prod or not category_col or not amount_col:
        print("Error: Missing matching product columns or Category in products.csv")
        return None

    merged_sales = sales.merge(
        products_df[[product_col_prod, category_col]],
        left_on=product_col_sales,
        right_on=product_col_prod,
        how="inner",
    )
    cat_sales = (
        merged_sales.groupby(category_col)[amount_col]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    print(cat_sales)
    return cat_sales