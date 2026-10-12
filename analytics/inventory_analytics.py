import pandas as pd

def get_current_stock(products):
    return products

def get_low_stock(products, threshold=5):
    return [p for p in products if p['stock'] <= threshold]

def get_out_of_stock(products):
    return [p for p in products if p['stock'] == 0]

def get_stock_value(products):
    total = sum(p['stock'] * p['price'] for p in products)
    return total

def get_dead_stock(products, sales):
    return [p for p in products if p['stock'] >= 10 and sales.get(p['id'], 0) == 0]