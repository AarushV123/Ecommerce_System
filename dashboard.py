# dashboard.py
import pandas as pd
import plotly.express as px
import streamlit as st
from analytics import inventory_analytics as inv
# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="E-Commerce Business Dashboard", page_icon="📊", layout="wide"
)


# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------


@st.experimental_memo
def load_data():
    sales = pd.read_csv("data/sales.csv")
    sales.columns = sales.columns.str.strip()

    products = pd.read_csv("data/products.csv")
    products.columns = products.columns.str.strip()

    customers = pd.read_csv("data/customers.csv")
    customers.columns = customers.columns.str.strip()

    return sales, products, customers


sales, products, customers = load_data()


# -------------------------------------------------
# PAGE TITLE
# -------------------------------------------------

st.title("📊 E-Commerce Business Dashboard")
st.markdown("### Sales and Business Performance Overview")


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.header("Dashboard Filters")

categories = products["Category"].dropna().unique()

selected_category = st.sidebar.multiselect(
    "Select Category", categories, default=list(categories)
)


# -------------------------------------------------
# MERGE SALES WITH PRODUCTS
# -------------------------------------------------

sales_data = sales.merge(
    products[["ProductID", "ProductName", "Category"]],
    on="ProductID",
    how="left",
)


# -------------------------------------------------
# FILTER DATA
# -------------------------------------------------

filtered_sales = sales_data[sales_data["Category"].isin(selected_category)]


# -------------------------------------------------
# KPI CALCULATIONS
# -------------------------------------------------

total_sales = filtered_sales["TotalAmount"].sum()
total_orders = filtered_sales["OrderID"].nunique()
total_customers = filtered_sales["CustomerID"].nunique()
total_products = filtered_sales["ProductID"].nunique()
total_stock_value = inv.get_stock_value(products)


# -------------------------------------------------
# KPI CARDS
# -------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Sales", f"₹{total_sales:,.2f}")

with col2:
    st.metric("Total Orders", total_orders)

with col3:
    st.metric("Customers", total_customers)

with col4:
    st.metric("Products Sold", total_products)

with col5:
    st.metric("Stock Value", f"₹{total_stock_value:,.2f}")


st.markdown("---")

# -------------------------------------------------
# MONTHLY SALES
# -------------------------------------------------

st.subheader("📈 Monthly Sales")

filtered_sales["SaleDate"] = pd.to_datetime(filtered_sales["SaleDate"])

monthly_sales = (
    filtered_sales.groupby(filtered_sales["SaleDate"].dt.to_period("M"))[
        "TotalAmount"
    ]
    .sum()
    .reset_index()
)

monthly_sales["SaleDate"] = monthly_sales["SaleDate"].astype(str)

fig_monthly = px.line(
    monthly_sales,
    x="SaleDate",
    y="TotalAmount",
    markers=True,
    title="Monthly Sales Trend",
)

fig_monthly.update_layout(xaxis_title="Month", yaxis_title="Sales")

st.plotly_chart(fig_monthly, use_container_width=True)


# -------------------------------------------------
# TWO-COLUMN SECTION
# -------------------------------------------------

col1, col2 = st.columns(2)


# -------------------------------------------------
# CATEGORY-WISE SALES
# -------------------------------------------------

with col1:
    st.subheader("📊 Category-wise Sales")

    category_sales = (
        filtered_sales.groupby("Category")["TotalAmount"]
        .sum()
        .reset_index()
        .sort_values("TotalAmount", ascending=False)
    )

    fig_category = px.pie(
        category_sales,
        names="Category",
        values="TotalAmount",
        hole=0.3,
        title="Sales by Category",
    )

    st.plotly_chart(fig_category, use_container_width=True)


# -------------------------------------------------
# PRODUCT REVENUE
# -------------------------------------------------

with col2:
    st.subheader("🏆 Product Revenue")

    product_revenue = (
        filtered_sales.groupby("ProductName")["TotalAmount"]
        .sum()
        .reset_index()
        .sort_values("TotalAmount", ascending=False)
        .head(10)
    )

    fig_products = px.bar(
        product_revenue,
        x="ProductName",
        y="TotalAmount",
        title="Top 10 Products by Revenue",
    )

    fig_products.update_layout(xaxis_title="Product", yaxis_title="Revenue")

    st.plotly_chart(fig_products, use_container_width=True)


# -------------------------------------------------
# INVENTORY ANALYTICS SECTION
# -------------------------------------------------

st.markdown("---")
st.subheader("📦 Inventory Analytics & Alerts")

inv_col1, inv_col2 = st.columns(2)

with inv_col1:
    st.markdown("#### ⚠️ Low Stock Products")
    low_stock_df = inv.get_low_stock(products)
    st.dataframe(low_stock_df[["ProductID", "ProductName", "Stock"]])

    st.markdown("#### ❌ Out of Stock Products")
    out_of_stock_df = inv.get_out_of_stock(products)
    st.dataframe(out_of_stock_df[["ProductID", "ProductName", "Stock"]])

with inv_col2:
    st.markdown("#### 💤 Dead Stock (High Stock & Zero Sales)")
    dead_stock_df = inv.get_dead_stock(products, sales)
    st.dataframe(dead_stock_df[["ProductID", "ProductName", "Stock"]])


# -------------------------------------------------
# SALES DATA TABLE
# -------------------------------------------------

st.subheader("📋 Sales Details")

df_display = sales_data.copy()
for col in df_display.columns:
    if pd.api.types.is_datetime64_any_dtype(df_display[col]):
        df_display[col] = df_display[col].dt.strftime("%Y-%m-%d")

st.dataframe(df_display)


# -------------------------------------------------
# DOWNLOAD BUTTON
# -------------------------------------------------

csv_data = filtered_sales.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Sales Data",
    data=csv_data,
    file_name="filtered_sales.csv",
    mime="text/csv",
)