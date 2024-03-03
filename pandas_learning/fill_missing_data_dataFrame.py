import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # Fill in missing values in the 'quantity' column with 0
    products['quantity'] = products['quantity'].fillna(0)
    return products

# Example usage:
data = {
    'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
    'quantity': [None, None, 779, 849],
    'price': [135, 821, 9319, 3051]
}
products_df = pd.DataFrame(data)

# Fill missing quantity values
updated_products = fillMissingValues(products_df)
updated_products

print(updated_products)