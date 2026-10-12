import pandas as pd

def get_current_stock(products_df):
    return products_df

def get_low_stock(products_df, threshold=5):
    return products_df[products_df['Stock'] <= threshold]

def get_out_of_stock(products_df):
    return products_df[products_df['Stock'] == 0]

def get_stock_value(products_df):
    # Calculates total stock value using Stock and Price columns
    return (products_df['Stock'] * products_df['Price']).sum()

def get_dead_stock(products_df, sales_df, high_stock=10):
    product_sales = sales_df.groupby('ProductID')['Quantity'].sum().reset_index()
    merged = products_df.merge(product_sales, on='ProductID', how='left').fillna({'Quantity': 0})
    
    return merged[(merged['Stock'] >= high_stock) & (merged['Quantity'] == 0)]